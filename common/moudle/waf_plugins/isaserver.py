#!/usr/bin/env python


NAME = 'Microsoft ISA Server'


def is_waf(self):
    detected = False
    r = self.invalid_host()
    if r is None:
        return
    if r.reason in self.isaservermatch:
        detected = True
    return detected
