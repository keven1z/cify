#!/usr/bin/env python


NAME = 'IBM Web Application Security'


def is_waf(self):
    normal = self.normal_request()
    protected = self.protected_folder()

    return protected is None and normal is not None
