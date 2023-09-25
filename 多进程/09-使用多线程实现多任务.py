import threading
import time


def singing():
    for i in range(3):
        print("singing...")
        time.sleep(1)

def dancing():
    for i in range(3):
        print("dancing...")
        time.sleep(1)


if __name__ == '__main__':
    sing_thread = threading.Thread(target=singing)
    dance_thread = threading.Thread(target=dancing)
    sing_thread.start()
    dance_thread.start()