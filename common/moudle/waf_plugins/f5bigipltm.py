#!/usr/bin/env python


NAME = 'F5 BIG-IP LTM'


def is_waf(self):
    detected = False
    if self.match_cookie('^BIGipServer'):
        return True
    elif self.match_header(('X-Cnection', '^close$'), attack=True):
        return True
    else:
        return False
