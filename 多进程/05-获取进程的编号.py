import time
import os
# 1.导入进程包
import multiprocessing


def sing(num, name):
    print("singing process id:", os.getpid())
    print("singing方法中获取父进程id：", os.getppid())
    for i in range(num):
        time.sleep(0.5)
        print("singing...")
        print(name)


def dance(num, name):
    print("dancing process id:", os.getpid())
    print("dancing方法中获取父进程id：", os.getppid())
    for i in range(num):
        time.sleep(0.5)
        print("dancing...")
        print(name)


if __name__ == '__main__':      # 主进程，下面创建两个子进程
    # 2. 创建进程对象，target指定进程执行的函数名
    # 2.1 通过元组给指定任务传参
    print("main方法中打印主进程id：", os.getpid())
    sing_process = multiprocessing.Process(target=sing, args=(3, "jerry"))    # 参数传入顺序不能错
    # 2.2 通过字典给指定任务传参
    dance_process = multiprocessing.Process(target=dance, kwargs={"name":"tom", "num":5})   # 顺序可以不一致，参数名必须一致
    # 3. 启动进程对象执行指定任务
    sing_process.start()
    dance_process.start()
