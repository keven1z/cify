#!/usr/bin/env python


NAME = '360WangZhanBao(360网站卫士)'


def is_waf(self):
    return self.match_header(('X-Powered-By-360WZB', '.+'))
