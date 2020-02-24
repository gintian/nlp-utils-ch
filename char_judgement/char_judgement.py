# -*- coding: utf-8 -*-
"""
   Author :        Jesper
   Date：          2020/2/24 21:34
   Description :
   Changed by:
"""

# 1. 判断是否包含中文
def is_contains_chinese(strs):
    for _char in strs:
        if '\u4e00' <= _char <= '\u9fa5':
            return True
    return False

# 2. 判断是否全是中文字符
def is_all_chinese(strs):
    for _char in strs:
        if not '\u4e00' <= _char <= '\u9fa5':
            return False
    return True

# 3. 判断是否仅包括中文，数字或者字母
def is_ch_digit_letter(strs):
	pass
