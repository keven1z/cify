#!/usr/bin/env python
# -*- coding:utf-8 -*-
#########################################################
# (C)  zii .All rights Reserved#
#########################################################
import argparse
import sys


def parse_option():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", dest="url", help="please specify a url to scan", required=False)
    parser.add_argument("-p", "--port", dest="port", action='store_true', help="Whether to scan the port")
    options = parser.parse_args()
    option = Option()
    option.url = options.url
    option.port = options.port
    return option


class Option(object):
    def __init__(self):
        self._url = None
        self._port = False

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    @property
    def port(self):
        return self._url

    @port.setter
    def port(self, port):
        self._port = port
