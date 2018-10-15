# -*- coding:utf-8 -*-
#!/usr/bin/python
######################
###  xml 解析    #####
######################
from xml.dom.minidom import parse

class Xml():
    def __init__(self):
        pass

    def _parse(self, xmlpath):
        dom = parse("../configuration/config.xml")
        # 获取文件元素对象
        document = dom.documentElement
        document.getElementsByTagName('test')
        return document


