# __*__coding:utf-8__*__
#######################
# 扫描端口插件
#######################
from common.plugin import Plugin
from common.log.logUtil import LogUtil as logging
from libnmap.process import NmapProcess
from libnmap.parser import NmapParser, NmapParserException


logger = logging.getLogger(__name__)


class CifyPlugin(Plugin):

    def __init__(self):
        super(CifyPlugin, self).__init__()
        self._id = 10000

    def _run(self):
        logger.info("We are executing nmap,please wait a moment")
        try:
            wurl = self.wharehouse.wurl
            url=wurl.hostname
            report = self.do_scan(url)
            self.print_scan(report)
        except PermissionError as e:
            logger.error(e)

    def do_scan(self, targets, options='-sV'):
        parsed = None
        nmproc = NmapProcess(targets, options)
        rc = nmproc.run()
        if rc != 0:
            print("nmap scan failed: {0}".format(nmproc.stderr))
        print(type(nmproc.stdout))

        try:
            parsed = NmapParser.parse(nmproc.stdout)
        except NmapParserException as e:
            print("Exception raised while parsing scan: {0}".format(e.msg))

        return parsed

    def print_scan(self, nmap_report):

        print("Starting Nmap {0} ( http://nmap.org ) at {1}".format(
            nmap_report.version,
            nmap_report.started))
        for host in nmap_report.hosts:
            if len(host.hostnames):
                tmp_host = host.hostnames.pop()
            else:
                tmp_host = host.address

        print("Nmap scan report for {0} ({1})".format(
            tmp_host,
            host.address))
        print("Host is {0}.".format(host.status))
        print("  PORT     STATE         SERVICE")

        for serv in host.services:
            pserv = "{0:>5s}/{1:3s}  {2:12s}  {3}".format(
                str(serv.port),
                serv.protocol,
                serv.state,
                serv.service)
            if len(serv.banner):
                pserv += " ({0})".format(serv.banner)
            print(pserv)

        print(nmap_report.summary)


'''
    def do_scan(self, targets, options="-sS", is_back=False):
        nm = NmapProcess(targets, options)

        if not is_back:
            rc = nm.run()
        else:
            nm.run_background()

            while nm.is_alive():
                logger.info("Host Scan running: ETC: {0} DONE: {1}%".format(nm.etc, nm.progress))
                time.sleep(2)
            rc = nm.rc

        if rc != 0:
            logger.info("scan failed: %s" % (nm.stderr))

        parsed = ''
        try:
            parsed = NmapParser.parse(nm.stdout)
        except NmapParserException as e:
            logger.info("Exception raised while parsing scan: %s" % (e.msg))

        return parsed

'''
if __name__ == '__main__':
    c = CifyPlugin()
    c._run()
    logger.info(c.id)
