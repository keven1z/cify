#!/usr/bin/env python


NAME = 'Microsoft URLScan'


def is_waf(self):
    detected = False
    testheaders = dict()
    testheaders['Translate'] = 'z' * 10
    testheaders['If'] = 'z' * 10
    testheaders['Lock-Token'] = 'z' * 10
    testheaders['Transfer-Encoding'] = 'z' * 10
    r1 = self.normal_request()
    if r1 is None:
        return
    r2 = self.normal_request(headers=testheaders)
    if r2 is None:
        return
    if r1.status_code != r2.status_code:
        if r2.status == 404:
            detected = True
    return detected
