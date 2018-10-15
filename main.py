# -*- coding:utf-8 -*-

# @name:    cify - Web infomation Scanner
# @author:  zii
import common.optparse as opt_parse
import common.init as init
import common.workdistributor as wd
from common.systeminfo import System
from common.net.url import WrappedUrl


class Scanner(object):
    def __init__(self):
        self.system = None

    def _run(self):
        init.banner()
        self.system = init.read()
        wd.work_port(self.system)
        wurl = WrappedUrl('http://www.ghostz.com.cn')
        System.wurl = wurl
        option = opt_parse.parse_option()


if __name__ == '__main__':
    scanner = Scanner()
    scanner._run()
