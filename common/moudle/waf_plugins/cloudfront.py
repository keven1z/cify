NAME = 'CloudFront'


def is_waf(self):
    if self.match_header(('Server', 'CloudFront'), attack=True):
        return True
    return False
