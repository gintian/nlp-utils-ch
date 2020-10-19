# -*- coding: utf-8 -*-
"""
   Author :        Jesper
   Date：          2020/3/3 15:24
   Description :
   Changed by:
"""

import re

# 去除括号内容，避免对模型造成干扰
# todo: badcase  挂精卫(哪个位置？_(非)常疑惑)

def filter_text_between_bracket(text):
	l_symbols = ["(", "）", "[", "【"]
	r_symbols = [")", "）", "]", "】"]
	bracket_positions = list()
	text_len = len(text)
	i = 0
	while i < text_len:
		if text[i] in l_symbols:
			j = i+1
			while j <  text_len and text[j] not in r_symbols:
				j += 1
			if j < text_len and text[j] in r_symbols and l_symbols.index(text[i]) == r_symbols.index(text[j]):
				bracket_positions.append([i,j])
				i = j
		i += 1
	return remove_text_by_section(text, bracket_positions)


def bracket_words_process(text, bracket_symbols=None, is_filter=False):
	if bracket_symbols is None:
		l_symbols = ["(", "）", "[", "【", "「"]
		r_symbols = [")", "）", "]", "】", "」"]
	else:
		l_symbols = [x[0] for x in bracket_symbols]
		r_symbols = [x[1] for x in bracket_symbols]
	bracket_positions = list()
	text_len = len(text)
	i = 0
	while i < text_len:
		if text[i] in l_symbols:
			j = i + 1
			while j < text_len and text[j] not in r_symbols:
				j += 1
			if j < text_len and text[j] in r_symbols and l_symbols.index(text[i]) == r_symbols.index(text[j]):
				bracket_positions.append([i, j])
				i = j
		i += 1
	if is_filter is True:
		return remove_text_by_section(text, bracket_positions)
	else:
		words_list = list()
		for _position in bracket_positions:
			# print(_position)
			_word = text[_position[0]+1:_position[1]]
			if _word:
				words_list.append(_word)

		return words_list





def remove_text_by_section(text, sections):
	"""
	:param text:
	:param sections: e.g. [[10, 15], [18, 23]]
	:return:
	"""
	res_text = ""
	start_index = 0
	for _section in sections:
		res_text += text[start_index:_section[0]]
		start_index = _section[1] + 1
	res_text += text[start_index:len(text)]
	return res_text


# 删除网页标签
def delete_html_tag(s):
	s = re.sub('\{IMG:.?.?.?\}', '', s)  # 图片
	s = re.sub(re.compile(r'[a-zA-Z]+://[^\s]+'), '', s)  # 网址
	s = re.sub(re.compile('<.*?>'), '', s)  # 网页标签
	s = re.sub(re.compile('&[a-zA-Z]+;?'), ' ', s)  # 网页标签
	s = re.sub(re.compile('[a-zA-Z0-9]*[./]+[a-zA-Z0-9./]+[a-zA-Z0-9./]*'), ' ', s)
	s = re.sub("\?{2,}", "", s)
	s = re.sub("\r", "", s)
	s = re.sub("\n", ",", s)
	s = re.sub("\t", ",", s)
	s = re.sub("（", ",", s)
	s = re.sub("）", ",", s)
	s = re.sub("\u3000", "", s)
	s = re.sub(" ", "", s)
	r4 = re.compile('\d{4}[-/]\d{2}[-/]\d{2}')  # 日期
	return s

def merege_seq_duplicated_to_one(text, duplicated_char):
	splited_text = text.split(duplicated_char)
	res_text = list()
	for _text in splited_text:
		if _text:
			res_text.append(_text)
	res_text = duplicated_char.join(res_text)
	return res_text







