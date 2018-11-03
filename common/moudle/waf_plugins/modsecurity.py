#!/usr/bin/env python


NAME = 'Trustwave ModSecurity'


def is_waf(self):
    detected = False
    for attack in self.attacks:
        r = attack(self)
        if r is None:
            return
        if r.status_code == 501:
            detected = True
            break
    # the following based on nmap's http-waf-fingerprint.nse
    if self.match_header(('Server', '(mod_security|Mod_Security|NOYB)')):
        return True
    return detected
