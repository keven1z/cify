#!/usr/bin/env python


NAME = 'West263CDN'


def is_waf(self):
    return self.match_header(('X-Cache', '.+WT263CDN-.+'))
