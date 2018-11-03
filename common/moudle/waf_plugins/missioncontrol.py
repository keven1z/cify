#!/usr/bin/env python


NAME = 'Mission Control Application Shield'


def is_waf(self):
    if self.match_header(('Server', 'Mission Control Application Shield')):
        return True
    return False
