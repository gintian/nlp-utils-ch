# -*- coding: utf-8 -*-
"""
   Author :        Jesper
   Date：          2020/6/9 20:08
   Description :
   Changed by:
"""

from numba import jit
import numpy as np
from utils.logger import log

def vector_similarity(vector_a, vector_b, mode="cosine"):
	sim_score = -1
	if mode == "consine":
		sim_score = cos_sim(vector_a, vector_b)
	else:
		log.info("[ERROR] Not support such mode:{}".format(mode))

	return sim_score



def cos_sim(vector_a, vector_b):
	"""
	计算两个向量之间的余弦相似度
	:param vector_a: 向量 a
	:param vector_b: 向量 b
	:return: sim
	"""
	vector_a = np.mat(vector_a)
	vector_b = np.mat(vector_b)
	num = float(vector_a * vector_b.T)
	denom = np.linalg.norm(vector_a) * np.linalg.norm(vector_b)
	cos = num / denom
	sim = 0.5 + 0.5 * cos
	return sim



# 余弦相似度加速算法
@jit(nopython=True)
def cosine_similarity(u: np.ndarray, v: np.ndarray):
    #     assert(u.shape[0] == v.shape[0])
    uv = 0
    uu = 0
    vv = 0
    for i in range(u.shape[0]):
        uv += u[i] * v[i]
        uu += u[i] * u[i]
        vv += v[i] * v[i]
    cos_theta = 0.0
    if uu != 0 and vv != 0:
        cos_theta = uv / np.sqrt(uu * vv)
    return cos_theta


@jit(nopython=True)
def cosine_similarity_batch(u_list: np.ndarray, v: np.ndarray):
    r = np.zeros(u_list.shape[0])
    max_score = 0.0
    for n, u in enumerate(u_list):
        uv = 0
        uu = 0
        vv = 0
        for i in range(u.shape[0]):
            uv += u[i] * v[i]
            uu += u[i] * u[i]
            vv += v[i] * v[i]
        cos_theta = 0.0
        if uu != 0 and vv != 0:
            cos_theta = uv / np.sqrt(uu * vv)
            max_score = max(max_score, cos_theta)
        r[n] = cos_theta
    return r, max_score
