import time


def sing():
    for i in range(3):
        time.sleep(0.5)
        print("singing...")


def dance():
    for i in range(3):
        time.sleep(0.5)
        print("dancing...")


if __name__ == '__main__':
    sing()
    dance()