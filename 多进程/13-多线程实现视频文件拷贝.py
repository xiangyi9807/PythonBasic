"""
需求：把一个文件夹下的多个视频文件拷贝到另外一个文件夹
使用多线程实现多任务拷贝提高性能
"""

import threading
import os


def copy_file(file_name, source_dir, dest_dir):
    source_path = source_dir + "/" + file_name
    print(source_path)
    dest_path = dest_dir + "/" + file_name

    with open(source_path, "rb") as source_file:
        with open(dest_path, "wb") as dest_file:
            while True:
                data = source_file.read(1024)
                if data:
                    dest_file.write(data)
                else:
                    break


if __name__ == '__main__':
    # 1.定义源文件夹路径和目标文件夹路径
    source_dir = "video"
    dest_dir = "test"

    # 2.判断目标文件夹是否存在
    try:
        os.mkdir(dest_dir)
    except:
        print("文件夹已存在！")

    # 3.获取源文件夹中的文件列表
    file_list = os.listdir(source_dir)

    # 4.循环遍历源文件夹中的文件
    for file_name in file_list:
        # copy_file(file_name, source_dir, dest_dir)
        sub_thread = threading.Thread(target=copy_file(file_name, source_dir, dest_dir))
        sub_thread.start()
