# -*- coding: utf-8 -*-
"""
   Author :        Jesper
   Date：          2020/2/25 09:52
   Description :
   Changed by:
"""

from collections import defaultdict

def classification_report(y_true, y_pred, decimal_place=4, use_f1=False,
                          use_confusion_matrix=False, print_report_str=True, show_label_num=True):
	assert len(y_true) == len(y_pred)

	report_str = "\n" + "="*20 + "[REPORT]" + "=" * 20 + "\n"

	report_str += total_accuracy(y_true, y_pred, decimal_place) + "\n"

	label_predict_detail = evaluation_metrics(y_true, y_pred, use_f1, use_confusion_matrix, decimal_place, show_label_num)

	for label, item in label_predict_detail.items():
		_label_report = item["report_str"]
		report_str += _label_report + "\n"
	if print_report_str:
		print(report_str)

	return report_str



def total_accuracy(y_true, y_pred, decimal_place=4):
	assert len(y_true) == len(y_pred)
	if_true_list = [1 if y_true[i] == y_pred[i] else 0 for i in range(len(y_true))]
	accuracy = sum(if_true_list) / len(y_true)
	accuracy = round(accuracy, decimal_place)
	acc_str = "Accuracy: {}, data num: {}, match num: {}".format(accuracy, len(y_true), sum(if_true_list))
	return acc_str





def evaluation_metrics(y_true, y_pred, use_f1=False, use_confusion_matrix=False, decimal_place=4, show_label_num=False):
	assert len(y_true) == len(y_pred)
	label_predict_detail = defaultdict(dict)
	labels_set = list(set(y_true))
	data_num = len(y_true)
	for _label in labels_set:
		predict_p = sum([1 if y_pred[i] == _label else 0 for i in range(len(y_true))])
		true_p = sum([1 if y_true[i] == _label else 0 for i in range(len(y_true))])
		_tp_num = sum([1 if y_true[i] == _label and y_pred[i] == _label else 0 for i in range(len(y_true))])
		_tn_num = sum([1 if y_true[i] != _label and y_pred[i] != _label else 0 for i in range(len(y_true))])
		_fp_num = predict_p - _tp_num
		_fn_num = true_p - _tp_num

		precision = round(_tp_num * 1.0/predict_p, decimal_place) if predict_p != 0 else 0
		recall = round(_tp_num * 1.0/true_p, decimal_place) if true_p != 0 else 0
		f1 = round(2 * precision * recall / (precision + recall), decimal_place) if (precision + recall) != 0 else 0
		
		
		report_str = "Label: {:4}, Precision:{:6}, Recall:{:6}".format(_label, precision, recall)
		if use_f1:
			report_str += ",  f1:{:6}".format(f1)
		if show_label_num:
			report_str += ", TP:{:6}, pred_postive:{:6}, true_positive:{:6}".format(_tp_num, predict_p, true_p)
		if use_confusion_matrix:
			raise NotImplementedError
	
		label_predict_detail[_label]["TP"] = _tp_num
		label_predict_detail[_label]["FP"] = _fp_num
		label_predict_detail[_label]["FN"] = _fn_num
		label_predict_detail[_label]["TN"] = _tn_num
		label_predict_detail[_label]["F1"] = f1
		label_predict_detail[_label]["precision"] = precision
		label_predict_detail[_label]["recall"] = recall
		label_predict_detail[_label]["report_str"] = report_str

	return label_predict_detail
