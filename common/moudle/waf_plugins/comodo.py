#!/usr/bin/env python

NAME = 'Comodo WAF'


def is_waf(self):
    return self.match_header(('Server', "Protected by COMODO WAF"))
