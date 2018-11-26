# coding=utf-8
NAME = 'zhidaochuangyuwaf（知道创宇云安全）'


def is_waf(self):
    for attack in self.attacks:
        w_resp = attack(self)
        if w_resp is None:
            return False
        if w_resp.status_code == 403 and w_resp.content.find(bytes('知道创宇云安全', encoding="utf8")) != -1:
            return True
    return False
