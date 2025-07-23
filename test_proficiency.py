#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试熟练度功能
"""

import sys
import os
from datetime import datetime, timedelta

# 添加src目录到Python路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from data.word_model import WordManager, Word


def test_proficiency_basic():
    """测试基础熟练度功能"""
    print("=== 测试基础熟练度功能 ===")
    
    # 创建管理器
    manager = WordManager("test_proficiency.json")
    
    # 添加测试单词
    test_words = [
        ("apple", "苹果", "I eat an apple every day."),
        ("book", "书", "I love reading books."),
        ("computer", "电脑", "I work on my computer.")
    ]
    
    for word, meaning, example in test_words:
        manager.add_word(word, meaning, example)
    
    print(f"添加了 {manager.get_word_count()} 个单词")
    
    # 测试熟练度初始值
    for word in manager.get_all_words():
        print(f"单词 '{word.word}' 初始熟练度: {word.proficiency}")
    
    # 测试增加熟练度
    print("\n--- 测试增加熟练度 ---")
    manager.increase_proficiency("apple")
    apple_word = manager.get_word("apple")
    print(f"apple 熟练度增加到: {apple_word.proficiency}")
    
    # 测试减少熟练度
    print("\n--- 测试减少熟练度 ---")
    manager.decrease_proficiency("book")
    book_word = manager.get_word("book")
    print(f"book 熟练度减少到: {book_word.proficiency}")
    
    # 测试边界值
    print("\n--- 测试边界值 ---")
    # 尝试增加到超过5
    for i in range(10):
        manager.increase_proficiency("apple")
    apple_word = manager.get_word("apple")
    print(f"apple 熟练度（应该最大为5）: {apple_word.proficiency}")
    
    # 尝试减少到低于0
    for i in range(10):
        manager.decrease_proficiency("book")
    book_word = manager.get_word("book")
    print(f"book 熟练度（应该最小为0）: {book_word.proficiency}")
    
    # 清理测试文件
    if os.path.exists("test_proficiency.json"):
        os.remove("test_proficiency.json")
    
    print("=== 基础熟练度功能测试完成 ===\n")


def test_studyable_words():
    """测试可学习单词功能"""
    print("=== 测试可学习单词功能 ===")
    
    # 创建管理器
    manager = WordManager("test_studyable.json")
    
    # 添加测试单词，设置不同的熟练度
    test_words = [
        ("apple", "苹果", "I eat an apple.", 0),
        ("book", "书", "I love reading books.", 3),
        ("computer", "电脑", "I work on my computer.", 5),
        ("dog", "狗", "The dog is my friend.", 2)
    ]
    
    for word, meaning, example, proficiency in test_words:
        w = Word(word, meaning, example, proficiency=proficiency)
        manager.words.append(w)
    
    print(f"添加了 {manager.get_word_count()} 个单词")
    
    # 显示所有单词的熟练度
    print("\n所有单词的熟练度:")
    for word in manager.get_all_words():
        print(f"  {word.word}: {word.proficiency}/5")
    
    # 测试可学习单词
    studyable_words = manager.get_studyable_words()
    print(f"\n可学习的单词数量: {len(studyable_words)}")
    for word in studyable_words:
        print(f"  {word.word} (熟练度: {word.proficiency})")
    
    # 测试一个月后重新学习
    print("\n--- 测试一个月后重新学习 ---")
    # 设置computer为一个月前学习过
    computer_word = manager.get_word("computer")
    one_month_ago = datetime.now() - timedelta(days=31)
    computer_word.last_review = one_month_ago.isoformat()
    
    studyable_words = manager.get_studyable_words()
    print(f"一个月后可学习的单词数量: {len(studyable_words)}")
    for word in studyable_words:
        print(f"  {word.word} (熟练度: {word.proficiency})")
    
    # 清理测试文件
    if os.path.exists("test_studyable.json"):
        os.remove("test_studyable.json")
    
    print("=== 可学习单词功能测试完成 ===\n")


def test_random_word_selection():
    """测试随机单词选择"""
    print("=== 测试随机单词选择 ===")
    
    # 创建管理器
    manager = WordManager("test_random.json")
    
    # 添加测试单词，设置不同的熟练度
    test_words = [
        ("apple", "苹果", "I eat an apple.", 0),
        ("book", "书", "I love reading books.", 3),
        ("computer", "电脑", "I work on my computer.", 5),
        ("dog", "狗", "The dog is my friend.", 2),
        ("elephant", "大象", "Elephants are large.", 4)
    ]
    
    for word, meaning, example, proficiency in test_words:
        w = Word(word, meaning, example, proficiency=proficiency)
        manager.words.append(w)
    
    print(f"添加了 {manager.get_word_count()} 个单词")
    
    # 测试随机选择（应该只从可学习的单词中选择）
    print("\n随机选择测试（10次）:")
    for i in range(10):
        random_word = manager.get_random_word()
        if random_word:
            print(f"  第{i+1}次: {random_word.word} (熟练度: {random_word.proficiency})")
        else:
            print(f"  第{i+1}次: 没有可学习的单词")
    
    # 清理测试文件
    if os.path.exists("test_random.json"):
        os.remove("test_random.json")
    
    print("=== 随机单词选择测试完成 ===\n")


def show_proficiency_rules():
    """显示熟练度规则"""
    print("=== 熟练度规则说明 ===")
    rules = [
        "1. 新添加的单词熟练度为0",
        "2. 答对题目熟练度+1，答错熟练度-1",
        "3. 熟练度范围：0-5",
        "4. 熟练度达到5的单词一个月内不再弹出学习",
        "5. 一个月后熟练度为5的单词会重新进入学习队列",
        "6. 只有第一次答对才增加熟练度，答错会减少熟练度"
    ]
    
    for rule in rules:
        print(f"  {rule}")
    
    print("=== 规则说明完成 ===\n")


if __name__ == "__main__":
    print("熟练度功能测试")
    print("=" * 50)
    
    test_proficiency_basic()
    test_studyable_words()
    test_random_word_selection()
    show_proficiency_rules()
    
    print("所有测试完成！") 