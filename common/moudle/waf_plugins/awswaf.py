#!/usr/bin/env python

NAME = 'AWS WAF'


def is_waf(self):
    return self.match_header(('Server', 'awselb/2\\.0'), attack=True)
