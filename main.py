# coding=utf-8
# copyright:zii
# version：1.0
import common.optparse as optparse
from xml.dom.minidom import parse
from common.systeminfo import *


class Scanner(object):
    def __init__(self):
        self.system = System()

    def banner(self):
        banner = "       _____ ________ \n" + "__________(_)___  __/_____  __\n" + "_  ___/__  / __  /_  __  / / /\n" + "/ /__  _  /  _  __/  _  /_/ / \n" + "\___/  /_/   /_/     _\__, /  \n" + "                     /____/  "
        banner = banner + '\n\n\tCopyright by zii @2018.9-2018.11'
        print(banner)

    def config_init(self):
        dom = parse("config.xml")
        # 获取文件元素对象
        document = dom.documentElement
        nodes = document.getElementsByTagName('plugins')[0]
        for element in nodes.childNodes:
            if element.nodeType == element.ELEMENT_NODE:
                for node in element.childNodes:
                    if node.nodeType == node.ELEMENT_NODE:
                        if node.nodeName == 'id':
                            port_plugin_id = node.childNodes[0].data
                            self.system.config.port_plugin_id = port_plugin_id

    def _run(self):
        self.banner()
        self.config_init()
        # option = optparse.parse_option()
        # if option.port:
        # pass


if __name__ == '__main__':
    scanner = Scanner()
    scanner._run()
