# -*- coding: utf-8 -*-
"""
   Author :        Jesper
   Date：          2020/4/9 14:38
   Description :
   Changed by:
"""

def whitespace_tokenize(text):
    """Runs basic whitespace cleaning and splitting on a piece of text."""
    text = text.strip()
    if not text:
        return []
    tokens = text.split()
    return tokens