#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time;
import os;
import shutil
# raw_input("按下 enter 键退出，其他任意键显示...\n")

list=['build','tmp']# 待删除的文件目录
print list

targetList=['/Users/lichong/Documents'] # 指定的目标目录
print targetList

# ticks=time.localtime(time.time())
# localtime=time.asctime(ticks)
# print localtime

# 格式化成2016-03-20 11:45:39形式
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 

# 打开一个文件
# fo=open("foo.txt","w")
# print "文件名: ", fo.name
# print "是否已关闭 : ", fo.closed
# print "访问模式 : ", fo.mode
# print "末尾是否强制加空格 : ", fo.softspace

# fo.write( "www.runoob.com!\nVery good site!\n")

# # 关闭打开的文件
# fo.close()

# # 打开一个文件
# fo = open("foo.txt", "r+")
# str = fo.read(10)
# print "读取的字符串是 : ", str
# # 关闭打开的文件
# fo.close()

# 重命名文件test1.txt到test2.txt。
# os.rename( "foo.txt", "fo.txt" )

# os.remove("fo.txt")

# 给出当前的目录
print os.getcwd()

# def searchBuildChildFile(dirs,files):


def file_name(file_dir):
    for root,dirs,files in os.walk(file_dir):
        if root.endswith('/build'):
            print(file_dir)
            print(root)
            print(files)
        elif '/build' in root:
            print(root)
            # shutil.rmtree(path)    #递归删除文件夹
        else:
            for dir in dirs:
                file_name(dir)

for dir in targetList:
    file_name(dir)
