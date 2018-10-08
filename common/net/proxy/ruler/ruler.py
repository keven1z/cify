class Ruler(object):
    def __init__(self):
        self.ruler_id = -1

    def execute(self, html_text):  # Through this rule, get ip_list
        self._execute(html_text)

    def _execute(self, html_text):
        raise Exception('unimplemented method')

    def get_ip_list(self):
        raise Exception('unimplemented method')
