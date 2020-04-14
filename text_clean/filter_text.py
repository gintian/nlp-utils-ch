# -*- coding: utf-8 -*-
"""
   Author :        Jesper
   Date：          2020/3/3 15:24
   Description :
   Changed by:
"""

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


