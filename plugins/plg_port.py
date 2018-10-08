# __*__coding:utf-8__*__
#######################
# 扫描端口插件
#######################
from common.plugin import Plugin
import common.cmd.cmdUtil as shell
from common.log.logUtil import LogUtil as logging

logging = logging.instance().getLogger()


class CifyPlugin(Plugin):

    def __init__(self):
        super(CifyPlugin, self).__init__()
        self._id = 10000

    def _run(self, wurl):
        logging.info("We are executing nmap,please wait a moment")
        cmd = "netstat -ano"
        print(shell.execute(cmd))


if __name__ == '__main__':
    c = CifyPlugin()
    c._run()
    logging.info(c.id)
