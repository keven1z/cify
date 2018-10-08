#!/usr/bin/env python
# -*- coding:utf-8 -*-
######################
选项
######################
def parse_option():
    optparser = argparse.ArgumentParser()
    optparser.add_option("-u", "--url", dest="url", type="string", help="please specify a url to scan" , required=True)
    