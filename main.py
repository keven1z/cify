# -*- coding:utf-8 -*-

# @name:    cify - Web infomation Scanner
# @author:  zii
import common.optparse as opt_parse
import common.config_init as init
from common.moudle_manager import MoudleManager
from common.net.url import WrappedUrl


class Scanner(object):
    def __init__(self):
        self.wharehouse = None
        self.module = MoudleManager()

    def _run(self):
        init.banner()
        self.wharehouse = init.read()

        option = opt_parse.parse_option()
        self.wharehouse.wurl = WrappedUrl(option.url)
        init.init_result(self.wharehouse.wurl.hostname)
        ip = init.cdn_check(self.wharehouse.wurl.hostname)
        waf = init.waf_check(self.wharehouse)
        self.wharehouse.ip = ip
        self.module.load_moudle(self.wharehouse)


if __name__ == '__main__':
    scanner = Scanner()
    scanner._run()
