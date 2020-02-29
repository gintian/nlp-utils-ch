# -*- coding: utf-8 -*-
"""
   Author :        Jesper
   Date：          2020/2/25 17:27
   Description :
   Changed by:
"""

# 统一文本编码，可用于文本匹配时，避免因全角半角导致匹配不致的问题
def strQ2B(ustring):
    """全角转半角"""
    rstring = ""
    for uchar in ustring:
        inside_code=ord(uchar)
        if inside_code == 12288:                              #全角空格直接转换
            inside_code = 32
        elif (inside_code >= 65281 and inside_code <= 65374): #全角字符（除空格）根据关系转化
            inside_code -= 65248
        rstring += unichr(inside_code)
    return rstring