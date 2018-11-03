#!/usr/bin/env python

NAME = 'BlockDoS'


def is_waf(self):
    return self.match_header(('server', "BlockDos\.net"))
