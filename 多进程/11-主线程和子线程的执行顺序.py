import time
import threading

def work():
    for i in range(10):
        print("working...")
        time.sleep(0.2)

if __name__ == '__main__':
    work_thread = threading.Thread(target=work)
    # 设置为守护线程，主线程结束后子线程也销毁
    work_thread.daemon = True
    work_thread.start()
    time.sleep(0.5)
    print("主线程执行结束！")