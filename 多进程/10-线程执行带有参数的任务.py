import threading
import time


def singing(num, name):
    for i in range(num):
        print(name, " is singing...")
        time.sleep(0.5)


def dancing(count, name):
    for i in range(count):
        print(name, " is dancing...")
        time.sleep(0.5)


if __name__ == '__main__':
    sing_thread = threading.Thread(target=singing, args=(3, "tom"))
    dance_thread = threading.Thread(target=dancing, kwargs={"name": "jerry", "count": 3})
    sing_thread.start()
    dance_thread.start()