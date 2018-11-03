#!/usr/bin/env python


NAME = 'F5 BIG-IP ASM'


def is_waf(self):
    # credit goes to W3AF
    return self.match_cookie('^TS[a-zA-Z0-9]{3,8}=')
