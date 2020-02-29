# nlp-utils-ch

### 1.说明
1. 根据自己nlp从业，一些可能会用到的中文处理脚本
2. 主要集合了一些大佬们的工作(巨人的肩膀真香)



### 2. 各模块使用详解
#### 2.1 Flashtext
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
#### 2.2 Zhconv
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

#### 2.3 Char_judgement
- 作用: 判断是否为中文，数字，英文等等
- 代码示例：代码简单而多，建议直接源码查看


#### 2.4 text_clean
- 作用: 清洗文本，去停用词，全解转半解，去网页制表符等
- 代码使用示例：代码简单而多，建议直接源码查看

#### 2.5 result_analysis
- 作用: 生成多分类结果报告，ner分类结果报告
- 代码使用示例：（todo）

#### 2.6 scel_to_txt
- 作用：搜狗词库文本格式（scel格式）转为可读的txt
- 参考: Ling Yue, Taiyuan U of Tech, http://blog.yueling.me/
- 词库来源: [link](https://pinyin.sogou.com/dict/)，此处感恩搜狗，为NLPer提供了各个领域的词库
- 代码使用示例
```python
>>> in_path = "your/scel/path/dir"
>>> out_path = "your/txt/path"
>>> convert_scel_to_txt(in_path, out_path)
```



### 3. TODO
- 拼音纠错 
- 表情符号过滤
- 等等，暂时没想起来




