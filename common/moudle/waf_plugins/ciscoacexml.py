#!/usr/bin/env python


NAME = 'Cisco ACE XML Gateway'


def is_waf(self):
    if self.match_header(('Server', 'ACE XML Gateway')):
        return True
    return False
