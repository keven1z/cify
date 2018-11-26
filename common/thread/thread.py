import threading
import inspect
import ctypes


class CIFYThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self._thread_id = threading.current_thread().ident
        self.url = None
        self.kwargs = None
        self.method = None
        self.result = None

    @property
    def thread_id(self):
        return self._thread_id

    def submit(self, method, url, **kwargs):
        self.url = url
        self.kwargs = kwargs
        self.method = method
        self.start()

    def get_result(self):
        try:
            return self.result
        except Exception:
            return None

    def run(self):
        if self.method is None:
            raise Exception('empty method')
        if self.url is None or self.kwargs is None:
            raise Exception('empty args')
        method = self.method
        print(method)
        print(method.request(self.url, self.kwargs))


