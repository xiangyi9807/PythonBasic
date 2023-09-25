import threading
import time


def task():
    time.sleep(0.5)
    # 获取当前线程的线程对象
    print(threading.current_thread())


if __name__ == '__main__':
    for i in range(5):
        sub_thread = threading.Thread(target=task)
        sub_thread.start()