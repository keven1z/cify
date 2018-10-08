
#log模块
import logging
import os
import threading
import time
class LogUtil(object):
    LOG_TYPE_FILE=0
    LOG_TYPE_CONSOLE=1
    ERROR = logging.ERROR
    WARN = logging.WARN
    INFO = logging.INFO
    DEBUG = logging.DEBUG
    _LogUtil_lock = threading.Lock()
    def __init__(self):
        self.logger=None
        time.sleep(0.1)

    @classmethod
    def instance(cls, *args, **kwargs):#获取日志对象
        if not hasattr(LogUtil, "_instance"):
            with LogUtil._LogUtil_lock:
                if not hasattr(LogUtil, "_instance"):
                    LogUtil._instance = LogUtil(*args, **kwargs)
        return LogUtil._instance

    def getLogger(self,type=LOG_TYPE_CONSOLE,filename=''):#默认控制台输出
        if type == self.LOG_TYPE_CONSOLE:#写入控制台
            fmt='%(asctime)s - %(levelname)s - %(message)s'
            logging.basicConfig(level=self.INFO,format=fmt)
            logger=logging.getLogger("console")
            return logger
        elif type == self.LOG_TYPE_FILE:#写入文件
            filename=os.path.dirname(__file__)+"/../../log/"+filename+".txt"
            logger=logging.getLogger("file")
            handler = logging.FileHandler(filename)
            handler.setLevel(logging.INFO)
            logger.addHandler(handler)
            return logger
if __name__ == '__main__':
    A=LogUtil.instance()
    logger=A.getLogger()
    logger.info("aaaa")
    B=LogUtil.instance()
    logger2=B.getLogger(0,"a")
    logger2.warn("aaa")