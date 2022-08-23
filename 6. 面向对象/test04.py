#! /usr/bin/env python
# author: vin

class OperationFile(object):
    def __init__(self, filename='c:\log.txt'):
        self.filenmae = filename

    def readfile(self):
        with open(self.filenmae, 'r') as f:
            pass

    def writefile(self):
        with open(self.filenmae, 'w') as f:
            pass

if __name__ == '__main__':
    obj1 = OperationFile()
    obj2 = OperationFile('D:\log.txt')