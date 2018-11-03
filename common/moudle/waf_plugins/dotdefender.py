#!/usr/bin/env python


NAME = 'Applicure dotDefender'


def is_waf(self):
    # thanks to j0e
    return self.match_header(['X-dotDefender-denied', '^1$'], attack=True)
