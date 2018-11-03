#!/usr/bin/env python


NAME = 'ChinaCache-CDN'


def is_waf(self):
    return self.match_header(('Powered-By-ChinaCache', '.+'))
