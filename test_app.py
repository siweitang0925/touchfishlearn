#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试脚本 - 验证程序功能
"""

import sys
import os
import json

# 添加src目录到Python路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from data.word_model import WordManager, Word


def test_word_manager():
    """测试单词管理器"""
    print("=== 测试单词管理器 ===")
    
    # 创建管理器
    manager = WordManager("test_words.json")
    
    # 添加测试单词
    test_words = [
        ("apple", "苹果", "I eat an apple every day."),
        ("book", "书", "I love reading books."),
        ("computer", "电脑", "I work on my computer."),
        ("dog", "狗", "The dog is my best friend."),
        ("elephant", "大象", "Elephants are very large animals."),
        ("flower", "花", "The flowers are beautiful.")
    ]
    
    for word, meaning, example in test_words:
        success = manager.add_word(word, meaning, example)
        print(f"添加单词 '{word}': {'成功' if success else '失败'}")
    
    print(f"\n总单词数: {manager.get_word_count()}")
    
    # 测试随机单词
    random_word = manager.get_random_word()
    if random_word:
        print(f"随机单词: {random_word}")
        
        # 测试随机选项
        options = manager.get_random_meanings(random_word.meaning, 5)
        print(f"错误选项: {options}")
    
    # 清理测试文件
    if os.path.exists("test_words.json"):
        os.remove("test_words.json")
    
    print("=== 测试完成 ===\n")


def test_word_class():
    """测试单词类"""
    print("=== 测试单词类 ===")
    
    # 创建单词
    word = Word("test", "测试", "This is a test.")
    print(f"单词: {word}")
    
    # 转换为字典
    word_dict = word.to_dict()
    print(f"字典格式: {word_dict}")
    
    # 从字典创建
    new_word = Word.from_dict(word_dict)
    print(f"从字典创建: {new_word}")
    
    print("=== 测试完成 ===\n")


if __name__ == "__main__":
    test_word_class()
    test_word_manager()
    print("所有测试完成！") 