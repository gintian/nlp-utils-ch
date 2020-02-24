
1. 集合了各位大佬的成果，做一个总合，方便nlper使用
2. 加了一些自己从事nlp工作的小结



### 各模块使用详解
#### Flashtext
- 作用:提取关键词, 同义词替换
- 参考: vi3k6i5大佬，[Github](https://github.com/vi3k6i5/flashtext)
- 优化点：原flashtext主要针对英语文本，因而在识别中文时出现bug，即在抽取多个相邻词，会出现抽取词变少的情问, 测试结果如下
```python
>>> from flashtext.keyword import KeywordProcessor
>>> keyword_processor = KeywordProcessor()
>>> keyword_processor.add_keyword("测试")
>>> keyword_processor.add_keyword("用例")
>>> text="这只是一个测试用例"
>>> keywords_found = keyword_processor.extract_keywords(text, span_info=True)
>>> keywords_found
>>> # [('测试', 5, 7)]
```
上述代码显示，keyword_processor加入了两个词“测试”和“用例”,但只识别出了“测试”


- 代码使用示例
```python
>>> from flash_text.keyword import KeywordProcessor
>>> keyword_processor = KeywordProcessor()
>>> keyword_processor.add_keyword("测试")
>>> keyword_processor.add_keyword("用例")
>>> text="这只是一个测试用例"
>>> keywords_found = keyword_processor.extract_keywords(text, span_info=True)
>>> keywords_found
>>># [('测试', 5, 7), ('用例', 7, 9)]
```
#### Zhconv
- 作用：繁体转简体,简体转繁体
- 参考：gumblex大佬，[Github](https://github.com/gumblex/zhconv)
- 代码使用示例：
```python
>>> from zhconv import convert
>>> # 繁体转简体
>>> res_1 = convert('我幹什麼不干你事。', 'zh-cn')
>>> # 简体转繁体
>>> res_2 = convert('人体内存在很多微生物', 'zh-tw')
>>> print(res_1)
我干什么不干你事。
>>> print(res_2)
人體內存在很多微生物
```

#### Scel_to_txt
- 作用：搜狗词库文本格式（scel格式）转为可读的txt
- 参考: Ling Yue, Taiyuan U of Tech, http://blog.yueling.me/
- 词库来源: [link](https://pinyin.sogou.com/dict/)，此处感恩搜狗，为NLPer提供了各个领域的词库
- 代码使用示例
```python
>>> in_path = "your/scel/path/dir"
>>> out_path = "your/txt/path"
>>> convert_scel_to_txt(in_path, out_path)
```

#### Char_judgement
- 作用: 判断是否为中文




#### ref
1. flashtext https://github.com/vi3k6i5/flashtext
2. scel2txt http://blog.yueling.me