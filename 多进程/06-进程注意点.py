import multiprocessing
import time


def work():
    for i in range(10):
        print("working...")
        time.sleep(0.2)


if __name__ == '__main__':
    work_process = multiprocessing.Process(target=work)
    work_process.start()
    time.sleep(1)
    print("主进程结束等待，检查子进程是否还在执行")