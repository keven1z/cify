#!/usr/bin/env python


NAME = 'Citrix NetScaler'


def is_waf(self):
    """
    First checks if a cookie associated with Netscaler is present,
    if not it will try to find if a "Cneonction" or "nnCoection" is returned
    for any of the attacks sent
    """
    # NSC_ and citrix_ns_id come from David S. Langlands <dsl 'at' surfstar.com>
    if self.match_cookie('^(ns_af=|citrix_ns_id|NSC_)'):
        return True
    if self.match_header(('Cneonction', 'close'), attack=True):
        return True
    if self.match_header(('nnCoection', 'close'), attack=True):
        return True
    if self.match_header(('Via', 'NS-CACHE'), attack=True):
        return True
    if self.match_header(('X-Client-Ip', '.'), attack=True):
        return True
    if self.match_header(('Location', '\/vpn\/index\.html')):
        return True
    if self.match_cookie('^pwcount'):
        return True
    return False
