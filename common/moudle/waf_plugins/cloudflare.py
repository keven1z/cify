#!/usr/bin/env python


NAME = 'CloudFlare'


# the following based on nmap's http-waf-fingerprint.nse
def is_waf(self):
    if self.match_header(('Server', 'cloudflare-nginx')):
        return True
    if self.match_cookie('__cfduid'):
        return True
    return False
