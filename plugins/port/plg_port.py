# __*__coding:utf-8__*__
#######################
# 扫描端口插件
#######################
from common.plugin import Plugin
from common.log.logUtil import LogUtil as logging
from libnmap.process import NmapProcess
from libnmap.parser import NmapParser, NmapParserException
import time

logger = logging.instance().getLogger()


class CifyPlugin(Plugin):

    def __init__(self):
        super(CifyPlugin, self).__init__()
        self._id = 10000

    def _run(self):
        logger.info("We are executing nmap,please wait a moment")
        try:
            self.do_scan('39.108.133.111')
        except PermissionError as e:
            logger.error(e)

    def do_scan(self, targets, options="-sV -O --top-ports 300", is_back=False):
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


if __name__ == '__main__':
    c = CifyPlugin()
    c._run()
    logger.info(c.id)
