使用第三方包 openpyxl

1.创建工作表
1.1创建工作簿之后会自动生成一个默认名为Sheet的工作表

from openpyxl import Workbook
wb = Workbook()
ws = wb.active
print(ws.title)
wb.close()


1.2运用create_sheet方法创建工作表
create_sheet(title,index)
title:工作表sheet名
index：下标，从0开始，表示sheet的位置

ws1 = wb.create_sheet('test_sheet1',1)


2.调用库，打开已有文件，获取默认sheet表
from openpyxl import load_workbook
wb=load_workbook('test.xlsx')        #打开文件目录下名为test.xlsx文件
ws=wb.active                         #获取默认sheet


3.创建一个sheet表
ws2 = wb.create_sheet('test1',1)     #在第二个位置创建一个sheet名为test1的sheet表
print(ws2.title)                     #输出sheet名验证一下


4.表名的修改
ws.title='我是第一张表'               #修改sheet名
ws2.title='我改名啦'                  #修改sheet名
print(ws.title)                      #输出sheet名验证一下


5.通过表名获取sheet表
sheet=wb['我改名啦']                  #通过sheet名获取sheet表
sheet1=wb['我是第一张表']
print(sheet)                         #输出sheet名验证一下


6.获取sheet表的下标
index=wb.index(ws2)  #获取sheet表的下标
print("我是表:%s的下标:%d"%(ws2.title,index))


7.sheet的移动
ws3=wb.create_sheet('我是第三个来的',2)    #创建新sheet表
ws4=wb.create_sheet('删我',3)             #创建新sheet表
wb.move_sheet('我是第三个来的',-1) # -1 负数表示向左移动，正数表示向右移动，数字表示移动几个位置
print(wb.sheetnames)


8.sheet表的复制和删除
cp_sheet=wb.copy_worksheet(ws4)        #对sheet表删我进行复制
print(wb.sheetnames)                   #输出所有sheet名
del wb['删我']                         #删除sheet表
print(wb.sheetnames)                   #输出所有sheet名


数据驱动：
https://blog.csdn.net/huang_zp123/article/details/130295945?ops_request_misc=&request_id=&biz_id=102&utm_term=openpyxl%20%E6%95%B0%E6%8D%AE%E9%A9%B1%E5%8A%A8&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-1-130295945.142^v96^pc_search_result_base2&spm=1018.2226.3001.4187

注意事项：
openpyxl文件加入图片时需要使用pillow包


目录（参考：https://developer.aliyun.com/article/1311373?spm=a2c6h.14164896.0.0.367847c5NLzMue）
1.openpyxl库
1.1介绍
1.2安装和导入
2.Excel文件处理
2.1打开、读取文件
2.2sheet操作
2.3写入、修改excel文件
3.样式和格式处理
3.1更改格式
3.2合并单元格
3.3拆分单元格
3.4冻结窗口
3.5对齐单元格文本
4.操作图标
