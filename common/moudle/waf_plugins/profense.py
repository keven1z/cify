#!/usr/bin/env python


NAME = 'Profense'


def is_waf(self):
    """
    Checks for server headers containing "profense"
    """
    return self.match_header(('Server', 'profense'))
