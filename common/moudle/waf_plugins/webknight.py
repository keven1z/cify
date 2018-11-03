#!/usr/bin/env python


NAME = 'Aqtronix WebKnight'


def is_waf(self):
    detected = False
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        if r.status_code == 404 and r.reason == 'Hack Not Found':
            detected = True
            break
    return detected
