#!/usr/bin/env python

NAME = 'Edgecast / Verizon Digital media'


def is_waf(self):
    return self.match_header(('Server', '^ECD \(.*?\)$')) or self.match_header(('Server', '^ECS \(.*?\)$'))
