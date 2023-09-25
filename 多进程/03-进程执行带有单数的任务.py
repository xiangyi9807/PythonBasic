import time
# 1.导入进程包
import multiprocessing


def sing(num):
    for i in range(num):
        time.sleep(0.5)
        print("singing...")


def dance(num):
    for i in range(num):
        time.sleep(0.5)
        print("dancing...")


if __name__ == '__main__':
    # 2. 创建进程对象，target指定进程执行的函数名
    # 2.1 通过元组给指定任务传参
    sing_process = multiprocessing.Process(target=sing, args=(3,))
    # 2.2 通过字典给指定任务传参
    dance_process = multiprocessing.Process(target=dance, kwargs={"num":5})
    # 3. 启动进程对象执行指定任务
    sing_process.start()
    dance_process.start()
