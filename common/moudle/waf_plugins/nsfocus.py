#!/usr/bin/env python


NAME = 'NSFocus'


def is_waf(self):
    if self.match_header(('Server', 'NSFocus')):
        return True
    return False
