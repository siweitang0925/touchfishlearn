#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试新功能 - 搜索和间隔设置
"""

import sys
import os
import json

# 添加src目录到Python路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from data.word_model import WordManager, Word


def test_search_function():
    """测试搜索功能"""
    print("=== 测试搜索功能 ===")
    
    # 创建管理器
    manager = WordManager("test_search.json")
    
    # 添加测试单词
    test_words = [
        ("apple", "苹果", "I eat an apple every day."),
        ("application", "应用程序", "This is a useful application."),
        ("book", "书", "I love reading books."),
        ("computer", "电脑", "I work on my computer."),
        ("programming", "编程", "I enjoy programming."),
        ("python", "Python语言", "Python is a great programming language."),
        ("software", "软件", "This software is very useful."),
        ("technology", "技术", "Technology is advancing rapidly.")
    ]
    
    for word, meaning, example in test_words:
        manager.add_word(word, meaning, example)
    
    print(f"总单词数: {manager.get_word_count()}")
    
    # 测试搜索
    search_tests = [
        ("apple", "搜索'apple'"),
        ("程序", "搜索'程序'"),
        ("prog", "搜索'prog'"),
        ("技术", "搜索'技术'"),
        ("book", "搜索'book'"),
        ("", "搜索空字符串")
    ]
    
    for search_term, description in search_tests:
        results = manager.search_words(search_term)
        print(f"{description}: 找到 {len(results)} 个结果")
        for word in results:
            print(f"  - {word.word} ({word.meaning})")
        print()
    
    # 清理测试文件
    if os.path.exists("test_search.json"):
        os.remove("test_search.json")
    
    print("=== 搜索功能测试完成 ===\n")


def test_settings():
    """测试设置功能"""
    print("=== 测试设置功能 ===")
    
    # 测试设置保存和加载
    test_settings = {
        'study_interval': 15
    }
    
    # 保存设置
    with open("test_settings.json", 'w', encoding='utf-8') as f:
        json.dump(test_settings, f, ensure_ascii=False, indent=2)
    
    print("设置已保存")
    
    # 加载设置
    with open("test_settings.json", 'r', encoding='utf-8') as f:
        loaded_settings = json.load(f)
    
    print(f"加载的设置: {loaded_settings}")
    
    # 验证间隔时间
    interval = loaded_settings.get('study_interval', 10)
    print(f"学习间隔: {interval} 分钟")
    
    # 清理测试文件
    if os.path.exists("test_settings.json"):
        os.remove("test_settings.json")
    
    print("=== 设置功能测试完成 ===\n")


def test_interval_validation():
    """测试间隔时间验证"""
    print("=== 测试间隔时间验证 ===")
    
    def validate_interval(interval_str):
        try:
            interval = int(interval_str)
            return max(1, min(60, interval))  # 限制在1-60分钟之间
        except ValueError:
            return 10  # 默认10分钟
    
    test_intervals = [
        ("5", "5分钟"),
        ("15", "15分钟"),
        ("30", "30分钟"),
        ("0", "0分钟（应该变成1分钟）"),
        ("100", "100分钟（应该变成60分钟）"),
        ("abc", "无效输入（应该变成10分钟）"),
        ("", "空字符串（应该变成10分钟）")
    ]
    
    for interval_str, description in test_intervals:
        result = validate_interval(interval_str)
        print(f"{description}: {result} 分钟")
    
    print("=== 间隔时间验证测试完成 ===\n")


if __name__ == "__main__":
    test_search_function()
    test_settings()
    test_interval_validation()
    print("所有新功能测试完成！") 