#!/usr/bin/env python


NAME = 'Art of Defence HyperGuard'


def is_waf(self):
    # credit goes to W3AF
    return self.match_cookie('^WODSESSION=')
