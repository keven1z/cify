#!/usr/bin/env python


NAME = 'Juniper WebApp Secure'


def is_waf(self):
    detected = False
    r = self.normal_request()
    if r is None:
        return
    if r.status_code == 403:
        return detected
    newpath = self.path + '?nx=@@'
    r = self.request(path=newpath)
    if r is None:
        return
    if r.status_code == 403:
        detected = True
    return detected
