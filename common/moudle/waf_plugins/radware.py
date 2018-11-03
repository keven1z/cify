#!/usr/bin/env python

NAME = 'Radware AppWall'

def is_waf(self):
    return self.match_header(('X-SL-CompState', '.'))
