#!/usr/bin/env python


NAME = 'Better WP Security'


def is_waf(self):
    r = self.normal_request()

    if r is None:
        return False

    link_header = r.headers.get('Link') or ""

    if "https://api.w.org/" not in link_header:
        # Does not appear to be a wordpress at all
        return False

    r = self.request("GET", self.path + "wp-content/plugins/better-wp-security/")

    if r is None:
        return False

    return r.status_code == 200
