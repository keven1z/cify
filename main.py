# -*- coding:utf-8 -*-
# Copyright:zii
# version：1.0
import common.optparse as optparse
import common.init as init
import common.workdistributor as wd


class Scanner(object):
    def __init__(self):
        self.system = None

    def _run(self):
        init.banner()
        self.system = init.read()
        wd.work_port(self.system)
        option = optparse.parse_option()


if __name__ == '__main__':
    scanner = Scanner()
    scanner._run()
