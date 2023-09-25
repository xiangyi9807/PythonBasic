import multiprocessing
import time


def work():
    for i in range(10):
        print("working...")
        time.sleep(0.2)


if __name__ == '__main__':
    work_process = multiprocessing.Process(target=work)
    # 设置守护进程，主进程结束后子进程直接销毁
    work_process.daemon = True
    work_process.start()
    time.sleep(1)
    print("主进程执行完成，检查子进程是否还在执行")