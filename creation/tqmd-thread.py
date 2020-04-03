#/bin/python
'''
tqmdの使い方、詳しく下記URLへ確認してください。
 [ https://tqdm.github.io/docs/tqdm/ ]
'''
import threading
from concurrent.futures import ThreadPoolExecutor
import random
import time
from tqdm import tqdm

def task(index):
    for i in range(20):
        time.sleep(0.05)
        
def execute_task(function, parameters):
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(tqdm(executor.map(function, parameters), total=len(parameters), ncols=60))
    return results

if __name__ == '__main__':
    parameters = range(50)
    execute_task(task, parameters)
