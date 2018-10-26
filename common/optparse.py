#!/usr/bin/env python
# -*- coding:utf-8 -*-
#########################################################
# (C)  zii .All rights Reserved#
#########################################################
import argparse
import sys


def parse_option():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", dest="url", help="please specify a url to scan", required=True)
    parser.add_argument("-p", "--port", dest="port", action='store_true', help="Whether to scan the port")
    options = parser.parse_args()
    option = Option()
    url = options.url
    if not (url.startswith('http://') or url.startswith('https://')):
        url = 'http://' + url
    option.url = url
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
