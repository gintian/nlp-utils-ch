#!user/bin/python
# _*_ coding: utf-8 _*_
# @Author      :   Jesper
# @Time        :   2020/8/18 15:34
# @Description :


def print_parameters(model):
	params = list(model.parameters())
	k = 0
	for i in params:
		l = 1
		print("该层的结构：" + str(list(i.size())))
		for j in i.size():
			l *= j
		print("该层参数和：" + str(l))
		k = k + l
	print("总参数数量和：" + str(k))