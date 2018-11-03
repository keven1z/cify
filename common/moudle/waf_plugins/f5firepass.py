#!/usr/bin/env python


NAME = 'F5 FirePass'


def is_waf(self):
    detected = False
    if self.match_header(('Location', '\/my\.logon\.php3')) and self.match_cookie('^VHOST'):
        return True
    elif self.match_cookie('^MRHSession') and (self.match_cookie('^VHOST') or self.match_cookie('^uRoamTestCookie')):
        return True
    elif self.match_cookie('^MRHSession') and (self.match_cookie('^MRHCId') or self.match_cookie('^MRHIntranetSession')):
        return True
    elif self.match_cookie('^uRoamTestCookie') or self.match_cookie('^VHOST'):
        return True
    else:
        return False
