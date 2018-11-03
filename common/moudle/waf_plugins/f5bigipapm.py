#!/usr/bin/env python


NAME = 'F5 BIG-IP APM'


def is_waf(self):
    detected = False
    # the following based on nmap's http-waf-fingerprint.nse
    if self.match_cookie('^LastMRH_Session') and self.match_cookie('^MRHSession'):
        return True
    elif self.match_header(('Server', 'BigIP|BIG-IP|BIGIP')) and self.match_cookie('^MRHSession'):
        return True
    if self.match_header(('Location', '\/my.policy')) and self.match_header(('server', 'BigIP|BIG-IP|BIGIP')):
        return True
    elif self.match_header(('Location', '\/my\.logout\.php3')) and self.match_header(('server', 'BigIP|BIG-IP|BIGIP')):
        return True
    elif self.match_header(('Location', '.+\/f5\-w\-68747470.+')) and self.matchheader(('server', 'BigIP|BIG-IP|BIGIP')):
        return True
    elif self.match_header(('server', 'BigIP|BIG-IP|BIGIP')):
        return True
    elif self.match_cookie('^F5_fullWT') or self.match_cookie('^F5_ST') or self.match_cookie('^F5_HT_shrinked'):
        return True
    elif self.match_cookie('^MRHSequence') or self.match_cookie('^MRHSHint') or self.match_cookie('^LastMRH_Session'):
        return True
    else:
        return False
