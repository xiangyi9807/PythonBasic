import time
# 1.导入进程包
import multiprocessing


def sing():
    for i in range(3):
        time.sleep(0.5)
        print("singing...")


def dance():
    for i in range(3):
        time.sleep(0.5)
        print("dancing...")


if __name__ == '__main__':
    # 2. 创建进程对象，target指定进程执行的函数名
    sing_process = multiprocessing.Process(target=sing)
    dance_process = multiprocessing.Process(target=dance)
    # 3. 启动进程对象执行指定任务
    sing_process.start()
    dance_process.start()
