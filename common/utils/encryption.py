# 加密工具类

import hashlib


# 计算文件的md5值
def file2md5(content):
    if not isinstance(content,bytes):
        content = content.encode('utf-8')
    return hashlib.md5(content).hexdigest()
