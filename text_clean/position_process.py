# -*- coding: utf-8 -*-
"""
   Author :        Jesper
   Date：          2020/4/1 18:52
   Description :
   Changed by:
"""
from char_judgement.char_judgement import is_ch_digit_letter


def find_nearest_phrase(text, word_position):
	# log.debug("Text:{}, word_position:{}".format(text, word_position))
	l = word_position[0]
	r = word_position[1]
	while l >= 0 and is_ch_digit_letter(text[l]):
		l -= 1
	l += 1
	while r < len(text) and is_ch_digit_letter(text[r]):
		r += 1
	# log.debug("Phrase:{}, l:{}, r:{}".format(text[l:r], l, r))
	return text[l:r]
