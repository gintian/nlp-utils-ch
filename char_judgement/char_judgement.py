# -*- coding: utf-8 -*-
"""
   Author :        Jesper
   Date：          2020/2/24 21:34
   Description :
   Changed by:
"""

#  判断是否包含中文
def is_contain_chinese(text):
    for _char in text:
        if '\u4e00' <= _char <= '\u9fa5':
            return True
    return False

#  判断是否全是中文字符
def is_all_chinese(text):
    for _char in text:
        if not '\u4e00' <= _char <= '\u9fa5':
            return False
    return True

# 判断是否全为英文字符
def is_all_letter(text):
	for _char in text:
		if not is_alphabet(_char):
			return False
	return True



#   判断是否仅包括中文，数字或者字母（暂时忽略小数）
def is_ch_digit_letter(text):
	for _char in text:
		if not any([is_chinese(_char), is_alphabet(_char), is_number(_char)]):
			return False
	return True

#  包含中文，数字和字母的长度(连续数字和连续字母长度为1)
def len_of_ch_digit_letter(text):
	strs_len = 0
	index = 0
	while index < len(text):
		_char = text[index]
		if is_chinese(_char):
			strs_len +=1
			index += 1
		elif is_alphabet(_char):
			strs_len += 1
			while index < len(text)  and is_alphabet(text[index]): index +=1
		elif is_number(_char):
			strs_len += 1
			while index < len(text)  and is_number(text[index]): index +=1
		else: index += 1
	return strs_len

#  判断一个字符是否是汉字
def is_chinese(uchar):
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False

#  判断一个字符是否为英文字母
def is_alphabet(uchar):
    if (uchar >= u'\u0041' and uchar <= u'\u005a') or (uchar >= u'\u0061' and uchar <= u'\u007a'):
        return True
    else:
        return False

#  判断一个字符是否为数字
def is_number(uchar):
    if uchar >= u'\u0030' and uchar <= u'\u0039':
        return True
    else:
        return False

#  判断一个字符串是否为可比较数字
def is_comparable_number(word):
	pass

