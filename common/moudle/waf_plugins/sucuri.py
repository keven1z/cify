#!/usr/bin/env python

NAME = 'Sucuri WAF'


def is_waf(self):
    return self.match_header(('X-Sucuri-ID', '.+'))
