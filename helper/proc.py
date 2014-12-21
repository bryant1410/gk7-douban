#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
author by jacksyen[hyqiu.syen@gmail.com]
---------------------------------------
调用系统进程命令帮助
"""
import os

from log import logger
from subprocess import call
import helper.aop as aop
from webglobal.globals import Global

class proc_helper:

    def __init__(self):
        pass

    '''
    转换文件[将html文件转换为epub格式]
    利用ebook-convert命令[基于calibre]
    input_file_path: 输入文件绝对路径
    out_file_dir: 输出文件目录绝对路径[如果不存在，则创建]
    author: 作者
    '''
    @staticmethod
    @aop.exec_time
    def convert(input_file_path, out_file_dir, author):
        if not os.path.exists(out_file_dir):
            os.mkdir(out_file_dir)
        # 文件名
        file_name = input_file_path.split('/')[-1]
        # 输出文件绝对路径
        out_file_path = '%s/%s.%s' %(out_file_dir, file_name[0: file_name.rfind('.')], Global.GLOBAL_OUT_FILE_FORMAT)
        call(['ebook-convert', input_file_path, out_file_path, '--authors', author])
        ## 转换成功
        return out_file_path
