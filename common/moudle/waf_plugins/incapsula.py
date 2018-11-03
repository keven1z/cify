#!/usr/bin/env python


NAME = 'Incapsula WAF'


def is_waf(self):
    # credit goes to Charlie Campbell
    if self.match_cookie('^.incap_ses'):
        return True
    if self.match_cookie('^visid.*='):
        return True
    return False
