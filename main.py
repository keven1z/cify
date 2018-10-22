# -*- coding:utf-8 -*-

# @name:    cify - Web infomation Scanner
# @author:  zii
import common.optparse as opt_parse
import common.config_init as init
import common.workdistributor as wd
from common.net.url import WrappedUrl


class Scanner(object):
    def __init__(self):
        self.wharehouse = None

    def _run(self):
        init.banner()
        self.wharehouse = init.read()
        wurl = WrappedUrl('http://www.baidu.com')
        self.wharehouse.wurl = wurl
        ip = init.cdn_check(wurl.hostname)
        self.wharehouse.ip = ip
        wd.work_port(self.wharehouse)

        option = opt_parse.parse_option()


if __name__ == '__main__':
    scanner = Scanner()
    scanner._run()
