#!/usr/bin/env python


NAME = 'Teros WAF'


def is_waf(self):
    # credit goes to W3AF
    return self.match_cookie('^st8id=')
