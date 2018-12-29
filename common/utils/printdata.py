from termcolor import colored, cprint
from common.log.log_util import LogUtil as log
import os

logging = log.getLogger(__name__)


def warn(string, flag="[!]"):
    cprint(flag + string, 'yellow')


def error(string, flag="[-]"):
    cprint(flag + string, 'red')


def info(string, flag="[+]", end='\n'):
    cprint(flag + string, 'green', end=end)


def result_print(string):
    print(string)


def start_mark(string, flag='*'):
    print(flag * 76)
    print(flag + ' ' * 31 + string + ' ' * 31 + flag)
    print(flag * 76)


def end_mark(flag='*'):
    print(flag * 76)
    print(flag + ' ' * 35 + 'END' + ' ' * 36 + flag)
    print(flag * 76)




import threading
class Singleton(object):
    _instance_lock = threading.Lock()



class ResultExport(object):
    """
    单例模式
    """
    _instance_lock = threading.Lock()

    def __init__(self):
        self.file = None
        self.path = None

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(ResultExport, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(ResultExport, "_instance"):
                    ResultExport._instance = ResultExport(*args, **kwargs)
        return ResultExport._instance

    def pre_export(self, file_name):
        filepath = os.getcwd() + '/data/result/' + file_name + '.txt'
        self.path = filepath
        file = open(filepath, 'w+')
        file.truncate()  # 清空文件内容
        file.write('URL:'+file_name)
        file.write('\n')
        self.file = file

    def add_data(self, content):
        filepath = self.path
        file = self.file
        if filepath is None:
            logging.warn('result path not Exist')
            return
        if file is not None:
            file.write(content)
            file.write('\n')

    def close(self):
        if self.file is not None:
            self.file.close()
