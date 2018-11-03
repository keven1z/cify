#!/usr/bin/env python

NAME = 'Naxsi'

def is_waf(self):
    return self.match_header(('X-Data-Origin', '^naxsi'))
