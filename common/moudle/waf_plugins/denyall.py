#!/usr/bin/env python


NAME = 'DenyALL WAF'


def is_waf(self):
    # credit goes to W3AF
    if self.match_cookie('^sessioncookie='):
        return True
    # credit goes to Sebastien Gioria
    #   Tested against a Rweb 3.8
    # and modified by sandro gauci and someone else
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        if r.status_code == 200:
            if r.reason == 'Condition Intercepted':
                return True
    return False
