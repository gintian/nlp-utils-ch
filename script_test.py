# -*- coding: utf-8 -*-
"""
   Author :        Jesper
   Date：          2020/2/24 20:49
   Description :
   Changed by:
"""


def test_flast_text():
	from flash_text.keyword import KeywordProcessor

	text="这只是一个测试用例"
	words=["测试", "用例"]
	keyword_processor = KeywordProcessor()
	for word in words:
		keyword_processor.add_keyword(word)
	keywords_found = keyword_processor.extract_keywords(text, span_info=True)
	print(keywords_found)

def test_zhconv():
	from zhconv import convert

	# 繁体转简体
	print(convert('我幹什麼不干你事。', 'zh-cn'))
	# 简体转繁体
	print(convert('人体内存在很多微生物', 'zh-tw'))

def test_char_judgement():
	from char_judgement.char_judgement import is_contain_chinese, is_all_chinese, is_ch_digit_letter, len_of_ch_digit_letter

	res_1 = is_contain_chinese("abc测试一下")
	res_2 = is_contain_chinese("abc")
	print(res_1)
	print(res_2)
	res_3 = is_all_chinese("测试一下")
	res_4 = is_all_chinese("abc测试一下")
	print(res_3)
	print(res_4)
	res_5 = is_ch_digit_letter("123abc测试一下")
	res_6 = is_ch_digit_letter("1")
	print(res_5)
	print(res_6)
	print(len_of_ch_digit_letter("..123abc测试一下a.."))

def test_scel_to_txt():
	from scel_to_txt.scel2txt import convert_scel_to_txt

	in_path = "your/scel/path/dir"
	out_path = "your/txt/path"
	convert_scel_to_txt(in_path, out_path)


if __name__ == '__main__':
	test_char_judgement()
