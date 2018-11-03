#!/usr/bin/env python


NAME = 'USP Secure Entry Server'


def is_waf(self):
    if self.match_header(('Server', 'Secure Entry Server')):
        return True
    return False
