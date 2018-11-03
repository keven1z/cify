#!/usr/bin/env python


NAME = 'Barracuda Application Firewall'


def is_waf(self):
    # credit goes to W3AF
    if self.match_cookie('^barra_counter_session='):
        return True
    # credit goes to Charlie Campbell
    if self.match_cookie('^BNI__BARRACUDA_LB_COOKIE='):
        return True
    # credit goes to yours truly
    if self.match_cookie('^BNI_persistence='):
        return True
    if self.match_cookie('^BN[IE]S_.*?='):
        return True
    return False
