#!/usr/bin/env python


NAME = '(安全宝)anquanbao'


def is_waf(self):
    return self.match_header(('X-Powered-By-Anquanbao', '.+'))
