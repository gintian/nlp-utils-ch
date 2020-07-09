# -*- coding: utf-8 -*-
# Author : Jesper
# Date：   2020/6/30 21:19
# Description :
import json
import pickle

def save_pickle(data, file_path):
    '''
    保存成pickle文件
    :param data:
    :param file_name:
    :param pickle_path:
    :return:
    '''
    with open(file_path, 'wb') as f:
        pickle.dump(data, f)


def load_pickle(input_file):
    '''
    读取pickle文件
    :param pickle_path:
    :param file_name:
    :return:
    '''
    with open(str(input_file), 'rb') as f:
        data = pickle.load(f)
    return data


def save_json(data, file_path, ensure_ascii=False, indent=4):
    '''
    保存成json文件
    :param data:
    :param json_path:
    :param file_name:
    :return:
    '''

    with open(str(file_path), 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def load_json(file_path):
    '''
    加载json文件
    :param json_path:
    :param file_name:
    :return:
    '''
    with open(str(file_path), 'r') as f:
        data = json.load(f)
    return data