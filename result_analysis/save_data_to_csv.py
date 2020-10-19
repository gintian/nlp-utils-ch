# -*- coding: utf-8 -*-
"""
   Author :        Jesper
   Date：          2020/3/4 12:45
   Description :
   Changed by:
"""


def save_data_by_cols(data, file_path, col_names, exist_header=True):
	with open(file_path, "w") as f:
		if exist_header:
			f.write("\t".join(col_names) + "\n")
		for item in data:
			line_str = "\t".join([item[x] for x in col_names])
			f.write(line_str + "\n")
