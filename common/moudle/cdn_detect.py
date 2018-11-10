#########################################################
# (C)  zii .All rights Reserved#
#########################################################
from dns import resolver, rdtypes
import os
import sys
from data.config import *
from common.utils.print import *
from common.log.logUtil import LogUtil as logging

logger = logging.getLogger(__name__)


class CDNDetect(object):
    dns_list = ["8.8.8.8", "114.114.114.114", "202.181.224.2", "223.5.5.5", "180.76.76.76", "123.123.123.123"]

    def __init__(self, host):
        self.ip_list = []
        self.server_list = []
        self.cdn_list = []
        self.host = host
        self.probability = 0

    def _server_load(self):  # load cdn_server.txt
        try:
            with open(os.path.abspath(os.path.dirname(__file__)) + '/../../'+CDN_SERVER_PATH, 'r') as f:
                for server in f.readlines():
                    server = server.strip()
                    servers = server.split('#')
                    if len(servers) == 3:
                        self.cdn_list.append(servers)
        except NotADirectoryError as e:
            logger.error(str(e))
        except FileNotFoundError as e:
            logger.error(str(e))
        finally:
            return None

    def run(self):  # detect CDN
        info('Detecting CDN')
        self._server_load()
        ip_list, server_list = self._get_ip_server_list()
        cdn_en = ''
        cdn_zh = ''
        if len(ip_list) > 1:
            self.probability += 30
        for cdns in self.cdn_list:
            cdn_url = cdns[0]
            p_cdn_en = cdns[1]
            p_cdn_zh = cdns[2]
            for target in self.server_list:
                if target.find(cdn_url) != -1:
                    cdn_en = p_cdn_en
                    cdn_zh = p_cdn_zh
                    self.probability += 70
                    break
        if self.probability > 80:
            warn(self.host + ' is using ' + cdn_zh + '(' + cdn_en + ')' + ' CDN')
            logger.warn(self.host + ' is using ' + cdn_zh + '(' + cdn_en + ')' + ' CDN')
            sys.exit(0)

        elif self.probability > 60:
            warn(self.host + 'is very likely to use a CDN')
            logger.warn(self.host + 'is very likely to use a CDN')
            sys.exit(0)
        else:
            ip = self.ip_list.pop(0)
            info('Not detect CDN,ip:' + ip)
            logger.info('Not detect CDN,ip:' + ip)
            return ip

    def _get_ip_server_list(self):

        for server in self.dns_list:
            self._parse_ip(self.host, server)
        return set(self.ip_list), set(self.server_list)

    def _parse_ip(self, host, dns_sever):
        try:
            rel = resolver.Resolver()
            rel.namesevers = dns_sever
            ans = rel.query(host, "A")
        except ValueError as v:
            error('CDN check failed,reason:' + str(v))
            logger.error('CDN check failed,reason:' + str(v))
            sys.exit(0)
        except AttributeError as e:
            error('CDN check failed,reason:' + str(e))
            logger.error('CDN check failed,reason:' + str(e))
            sys.exit(0)
        except resolver.NXDOMAIN as m:
            error('CDN check failed,reason:' + str(m))
            logger.error('CDN check failed,reason:' + str(m))
            sys.exit(0)

        for i in ans.response.answer:
            for j in i.items:
                if isinstance(j, rdtypes.IN.A.A):
                    ip = j.address
                    self.ip_list.append(ip)
                elif isinstance(j, rdtypes.ANY.CNAME.CNAME):
                    cname = j.to_text()
                    self.server_list.append(cname)


if __name__ == '__main__':
    cdn = CDNDetect("www.freebuf.com")
    cdn.run()
