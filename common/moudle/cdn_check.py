#########################################################
# (C)  zii .All rights Reserved#
#########################################################
from dns import resolver, rdtypes
import os
import sys
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

    def _server_load(self):
        try:
            with open(os.path.abspath(os.path.dirname(__file__)) + '/data/cdn_server.txt', 'r') as f:
                for server in f.readlines():
                    self.cdn_list.append(server.strip())
        except NotADirectoryError as e:
            logger.error(str(e))
        except FileNotFoundError as e:
            logger.error(str(e))
        finally:
            return None

    def _check(self):
        self._server_load()
        ip_list, server_list = self._get_ip_server_list()
        if len(ip_list) > 1:
            cdn_name = 'UNKNOWN'
            # for cdn in self.cdn_list:
            # if cdn in server_list:
            #
            return True, None, cdn_name
        return False, ip_list.pop(), None

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
            error('CDN check failed')
            logger.error('cdn check failed')
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
    cdn = CDNDetect("www.ghostz.com.cn")
    print(cdn._check())
