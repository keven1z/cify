#!/usr/bin/env python

NAME = 'FortiWeb'

def is_waf(self):
    return self.match_cookie('FORTIWAFSID=')
