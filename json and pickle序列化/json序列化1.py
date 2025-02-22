# -*- coding:utf-8 -*-
# xy

# 序列化：内存对象变字符串写入硬盘
# 反序列化：加载回来

info = {
    'name':'totti',
    'age':40
}

f = open('test.txt', 'w')
# f.write(info)   # 报错，不能直接写如字典
f.write(str(info))  # 可以通过强制转字符串再写入

f.close()


f = open('test.txt', 'r')
data = f.read()
print(eval(data))
