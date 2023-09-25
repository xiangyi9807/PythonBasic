"""
需求：把一个文件夹下的多个视频文件拷贝到另外一个文件夹
使用多进程实现多任务拷贝提高性能
"""

import os
import multiprocessing


def copy_file(file_name, source_dir, dest_dir):
    #  拼接源文件路径和目标文件路径
    # print(os.getpid())
    source_path = source_dir + "/" + file_name
    dest_path = dest_dir + "/" + file_name
    # 打开源文件和目标文件
    with open(source_path, 'rb') as source_file:
        with open(dest_path , 'wb') as dest_file:
            # 循环实现拷贝
            while True:
                data = source_file.read(1024)
                if data:
                    dest_file.write(data)
                else:
                    break


if __name__ == '__main__':
    # 1. 定义源文件夹和目标文件夹
    source_dir = "video"        # 当前文件同级目录下建个video文件夹
    dest_dir = "test"           # 当前文件同级目录下建个test文件夹

    # 2.创建目标文件夹
    try:
        os.mkdir(dest_dir)
    except:
        print("目标文件夹已经存在!")

    # 3. 读取源文件夹下的文件列表
    file_list = os.listdir(source_dir)

    # 4. 遍历文件夹列表实现拷贝
    for file_name in file_list:
        # copy_file(file_name, source_dir, dest_dir)        # 单进程实现
        # 5. 使用多进程实现多任务拷贝
        sub_process = multiprocessing.Process(target=copy_file, args=(file_name, source_dir, dest_dir))
        sub_process.start()