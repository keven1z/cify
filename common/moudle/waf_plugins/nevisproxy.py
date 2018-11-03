#!/usr/bin/env python

NAME = 'AdNovum nevisProxy'


def is_waf(self):
    # credit goes to an anonymous reporter
    if self.match_cookie('^Navajo.*?$'):
        return True
    return False
