#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time;
import os;
import shutil
# 1、指定清理目录
# 2、过滤合法文件
# 3、指定清理时间日期
# 4、统计清理文件的总计大小
# 5、统计清理耗时
# 6、？删除找回功能？
build='/build/'
clearDirlist=[build+'generated',build+'outputs',build+'tmp',build+'intermediates'
            ,build+'arcore-native',build+'sceneform_sdk'
            ]# 待删除的文件目录
print clearDirlist

clearFileList=['.dmg']
print clearFileList

filterList=['.java','.js','.cpp','.c']

targetList=['/Users/lichong/Documents'] # 指定的目标目录
print targetList

def file_name(file_dir):
    for root,dirs,files in os.walk(file_dir):
        for clearFile in clearFileList:
            for file in files:
                if os.path.splitext(file)[1]==clearFile:
                    print(file)


        if build in root:
            # print(root)
            for clearDir in clearDirlist:
                if clearDir in root:
                    print("待删除："+root)
                    # shutil.rmtree(root)    #递归删除文件夹
                    print("**已删除："+root)
                    break
            continue
        else:
            for dir in dirs:
                file_name(dir)
        

for dir in targetList:
    file_name(dir)
