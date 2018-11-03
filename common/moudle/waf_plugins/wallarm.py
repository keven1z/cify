#!/usr/bin/env python

NAME = 'Wallarm'

def is_waf(self):
    return self.match_header(('Server', "nginx-wallarm"))

