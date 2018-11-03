#!/usr/bin/env python


NAME = 'Safedog(安全狗)'


def is_waf(self):
    if self.match_cookie('wwwsafedog'):
        return True
    if self.match_cookie('^safedog-flow-item='):
        return True
    if self.match_header(('Server', '^Safedog')):
        return True
    if self.match_header(('X-Powered-By', '^WAF/\d\.\d')):
        return True
    return False
