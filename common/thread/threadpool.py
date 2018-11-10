from concurrent.futures import ThreadPoolExecutor
from data.config import *


def execute_by_thread(method, data_list):
    with ThreadPoolExecutor(THREAD_NUMBER) as executor:
        executor.submit(method, data_list)
