#!/usr/bin/env python


NAME = 'eEye Digital Security SecureIIS'


def is_waf(self):
    # credit goes to W3AF
    detected = False
    r = self.normal_request()
    if r is None:
        return
    if r.status_code == 404:
        return
    headers = dict()
    headers['Transfer-Encoding'] = 'z' * 1025
    r = self.normal_request(headers=headers)
    if r is None:
        return
    if r.status_code == 404:
        detected = True
    return detected
