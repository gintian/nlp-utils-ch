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
		keyword_processor.add_keyword(word, "123")
	keywords_found = keyword_processor.extract_keywords(text)
	print(keywords_found)

def test_zhconv():
	from zhconv import convert

	# 繁体转简体
	print(convert('我幹什麼不干你事。', 'zh-cn'))
	# 简体转繁体
	print(convert('人体内存在很多微生物', 'zh-tw'))

def test_char_judgement():
	from char_judgement.char_judgement import is_contain_chinese, is_all_chinese, is_ch_digit_letter, len_of_ch_digit_letter, is_all_letter

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

	res_7 = is_all_letter("abc")
	print(res_7)
	res_8 = is_all_letter("abc12")
	print(res_8 )

def test_scel_to_txt():
	from scel_to_txt.scel2txt import convert_scel_to_txt

	in_path = "your/scel/path/dir"
	out_path = "your/txt/path"
	convert_scel_to_txt(in_path, out_path)

def test_text_clean():
	# from text_clean.filter_text import filter_text_between_bracket, bracket_words_process
	# text = "()你好有东西, 挂精卫哪个位置？_(非常疑惑)"
	# text = "【女武神】丽塔"
	# text = "「影骑士·月轮」作战指南"
	# # res = filter_text_between_bracket(text)
	# res = bracket_words_process(text, is_filter=False)
	# print(res)
	from text_clean.text_tokenize import token_en_number_seq_words
	token_en_number_seq_words("add今天ab真cd4不错ab")

def test_result_analysis():
	# from result_analysis.classification_result import total_accuracy, evaluation_metrics, classification_report
	# y_true = [1, 0, 0, 1, 1, 0, 1, -1, -1]
	# y_pred = [1, 0, 0, 0, 1, 0, 1, -1, 1]
	# res = total_accuracy(y_true, y_pred)
	# print(res)
	# res = evaluation_metrics(y_true, y_pred)
	# print(res)
	#
	# res = classification_report(y_true, y_pred)
	# print(res)

	# rouge metric
	import time
	import sys
	sys.setrecursionlimit(500)
	from result_analysis.rouge_metric import Rouge
	rouge = Rouge(metrics=["rouge-2"], exclusive=False)
	start_time = time.time()
	a = "今天天气不错"
	b = "欢迎新入职的休伯利安舰长，相信各位在经过角色养成篇后以经对(清洗甲板)有了初步了解，接下来就让我来详细教各位舰长如何(空中劈叉)啦～角色装备篇【悬赏委托】(必肝)武器:超电磁手炮☆古老的月光毕业武器，已经基本没有实用价值。不过是超限电磁炮的前置要素（解锁图鉴），依旧可以成为新的毕业武器武器:磁暴斩☆古老的鬼铠毕业武器，攻击自带特效，可惜已经基本没有实战价值。不过是超限磁暴斩的前置要素（解锁图鉴），并且强力推荐超限为重磁暴，使用频率极高武器:妖刀·赤染樱☆真炎幸魂标准的毕业武器，加伤稳定，武器主动可刷新分支的易伤时间（分支自身无法刷新），提高易伤覆盖率。超限武器相较其提升明显，强度有保证武器:百手巨人初型☆目前来说已很少作为输出武器使用，主要用于时空控制并施加脆弱效果。超限后成功实现量变到质变，进而在实战中打出各种战场高分。同时也是山吹的好伙伴，补足脆弱的同时，还实现了延迟角色离场 → 延迟触发BUFF加成☆俗称沙皇中，根据连击数增加无限制的物理伤害，效果优秀☆在满生命情况下可大幅提升物理伤害的通用物理圣痕，不适合持续流血的量子深渊及迪拉克之☆大幅提升对麻痹敌人的元素伤害，在对可麻痹敌人的作战中发挥出色，对其他无法麻痹敌人的作战中等于白板圣痕。☆大幅提升对点燃敌人的元素伤害，目前点燃手段多样，很多BOSS都可点燃，加伤很容易生效。☆俗称艳后下，与苍玄中相似，大幅提升对麻痹敌人的全伤害，因此也可以给物理角色使用，在对可麻痹敌人的作战中发挥出色。☆可显著缩短武器主动CD。特别的，其下位替代——德丽莎·起源（中）已经能够满足日常战斗的基本需求，齐格飞（中）只有在极限竞速的情况下，才能展现出其优势。☆中位用于给圣女快速回复SP（圣女闪避技带有流血效果）。☆可提供雷电易伤效果，但需要启动时间。整体加成偏低，而且还需要启动时间。目前有超限百手延迟驻场的骚套路，但具体实用性不算很高。☆麻痹效果长，CD短，整体覆盖率高，常由月光携带。但在超限电磁炮出现后，武器带来的长时间麻痹效果逐渐取代了开普勒（中）。在没有超限电磁炮之前，推荐月光采用：开普勒（上、中） 艳后（下）的搭配。☆对群效果好，对单弱势。上位限制较多，因此实际加伤能力一般；中位为伤害倍率提升，非常吃角色自身加成；下位为核心单件，减速/冻结的敌人越多，加伤最足。3件套提供高额冰伤加成，因此通常还是成套使用。地图装☆在BOSS战中（单个敌人），所有角色均可使用。中位也算是不错的火伤圣痕（白核装），因为主流的：玫瑰，真红，荣光，其主要输出方式都包含有蓄力攻击☆可提供高额的闪避技冷缩效果☆整体是一套依赖全局时空，才能触发强力效果的圣痕。其中中位的价值最大，可提供高额暴击率，推荐优先锻造（并且也只能获取一个）。上位一般用于快速破盾，2件套可加快圣女的SP回复速度，均主要在战场竞速中使用☆下位非常契合增幅迅羽（迅雷）闪避接大招的输出机制，可提供120%的超高雷伤加成，主要用于BOSS竞速（闪避可控）☆各单件效果一般，主要牛逼在2件套：在仅携带上、中2件套时，只会混出橙色，使目标受到的物理伤害提升30% 。虽然只持续4秒，但已足够部分物理爆发类角色输出（比如增幅游侠）。在合理使用的情况下，其辅助效果会强过古斯塔夫☆一般由辅助携带，虽然10%的概率较低，但18%的全伤害提升也算对的起这个概率，通常是凹战场高分才会使用的圣痕。特别的，该圣痕的词条为“攻击时”，没有限制攻击类型，因此，例如：神恩大招、鬼角主动这样，能后台造成伤害还具备高攻击段数的效果时，暴食加成的期望值会大幅提高，会优于特斯拉（上）等圣痕。(注4.1版本糖从做，会重写)☆极其廉价的白核圣痕。数值高，无需启动是其一大优势。缺点是杀敌会增加自身受到的伤害，不太适合深渊群怪，倒是很适合战场☆后台每秒恢复sp，上场后sp快速衰减，通常有两种携带情况，① ：雪地大招物理易伤兼控制，战车大招远程物理易伤兼聚怪。平时挂后台，SP够了就可以切出来打一波爆发。特别提醒：因为上场后会快速消耗SP，因此按大招的手要快，不然可能SP就不足了。②：懒惰下 血舞。通常用于记忆战场☆一般用于辅助，2件套“下场后全队全伤 10%”的效果非常实用，加成无限制且触发非常简单。中位又可额外提升队友的火元素伤害，整体就辅助火属性主C来说，非常给力。炽翎可穿戴3件套辅助，兼顾输出。☆可作莎士比亚（下）的替代品☆优秀的物理过渡圣痕，上位物理加伤，中位暴击加伤，下位提升暴击率的同时还能回复一定的SP。可根据自身的不足（比如缺中位物理），选择合适的部位过渡。☆并不廉价的雷伤过渡圣痕，上、中一般；下位较为通用，且对于缺少全伤的角色来说提升不错。圣痕整体的伤害加成偏低，相较爱迪生提升有限，且它是白核圣痕，所以并不廉价，值得换的也就下位。☆优秀的近战物理过渡圣痕，上位花瓶，中、下位较为实用，2件套效果强力，但需要搭配山吹的护盾（不被击中）以维持全伤加成☆活动圣痕，需等待活动复刻。通常利用2件套触发持续的点燃效果，以触发队友被动加伤或BOSS（黑轩辕）易伤。由于下位具备不错的辅助加成（20%火伤和物伤），因此通常是上、下或上、中（点燃）组合。☆活动圣痕，需等待活动复刻。上位的水球爆炸基本无伤害，核心在于中位的元素伤害提升效果。由于想触发中位必须携带上，所以通常使用上、中组合。作为活动圣痕，加成还是很不错的。相对叶采章，其加成稍低，且为延迟触发，不能立刻生效。地图装圣痕是各路神仙战场的常客，它们有的承担了极限伤害的补足、有的另辟蹊径实现了蛋池装备都不一定能实现的功能。好活。增幅游侠带姬麟黑套，月光上色效果怎样？。幽色倒是有了，没神恩，圣女得给黑希用，单月光和游侠有伤害吗？。游侠最好3s，可以用幽色猫黑黑，山吹带毕加索上色牛下，月光可以特毕奥武器索尔。👌🏻，我先肝到3s，还差几十片。好活。。现在还有萌新？。我呀，刚入坑。这个怎么肝啊，买不起委托书。。入坑。想求个发展思路。毕业雷律号入坑，打算抽丹心，那么炽翎还要继续养么，是不是要换樱桃炸弹。然后下一个养谁比较好（武器只有双狼）。我比较随意，不追求赶进度，但是不想走太多弯路不在意养成周期。。现在武器圣痕打造系统都看不懂，联机委托也不知道选啥。战场换粉毛，可以垃圾屋换血舞，攒水到周年庆，物理队的话神恩是必备的，炎八2s，山吹肝到增幅4星，金辉每周观星换完，星石买量力而行，不追求强度毕业雷律队够了红莲要多个体系配置完整，你有毕业雷律加个云墨血舞，初中级区红莲是没问题的。好的"
	print("test")
	print(len(b))
	a = " ".join(a)
	b = " ".join(b)
	res = rouge.get_scores(a, b)
	print(res)
	end_time = time.time()
	print("time:{}".format(end_time - start_time))
	
def test_file_process():
	from utils.file_process import excel_to_csv
	src_path = "/private/tmp/tmp.xlsx"
	tgt_path = "/private/tmp/tmp.csv"


	excel_to_csv(src_path, tgt_path, src_file_type="excel")



if __name__ == '__main__':
	test_file_process()
