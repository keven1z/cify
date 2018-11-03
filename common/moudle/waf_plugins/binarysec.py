#!/usr/bin/env python


NAME = 'BinarySec'


def is_waf(self):
    # credit goes to W3AF
    if self.match_header(('Server', 'BinarySec')):
        return True
    # the following based on nmap's http-waf-fingerprint.nse
    elif self.match_header(('x-binarysec-via', '.')):
        return True
    # the following based on nmap's http-waf-fingerprint.nse
    elif self.match_header(('x-binarysec-nocache', '.')):
        return True
    else:
        return False
