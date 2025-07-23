#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
演示新功能 - 搜索和间隔设置
"""

import sys
import os
import json

# 添加src目录到Python路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from data.word_model import WordManager


def demo_search_feature():
    """演示搜索功能"""
    print("🔍 搜索功能演示")
    print("=" * 50)
    
    # 创建管理器并添加示例单词
    manager = WordManager("demo_words.json")
    
    # 添加一些示例单词
    sample_words = [
        ("apple", "苹果", "I eat an apple every day."),
        ("application", "应用程序", "This is a useful application."),
        ("book", "书", "I love reading books."),
        ("computer", "电脑", "I work on my computer."),
        ("programming", "编程", "I enjoy programming."),
        ("python", "Python语言", "Python is a great programming language."),
        ("software", "软件", "This software is very useful."),
        ("technology", "技术", "Technology is advancing rapidly."),
        ("learning", "学习", "Learning is a lifelong process."),
        ("education", "教育", "Education is important for everyone.")
    ]
    
    for word, meaning, example in sample_words:
        manager.add_word(word, meaning, example)
    
    print(f"已添加 {manager.get_word_count()} 个单词")
    print()
    
    # 演示搜索功能
    search_examples = [
        ("apple", "搜索英文单词"),
        ("程序", "搜索中文含义"),
        ("prog", "搜索部分英文"),
        ("技术", "搜索中文关键词"),
        ("learn", "搜索例句中的词")
    ]
    
    for search_term, description in search_examples:
        print(f"📝 {description}: '{search_term}'")
        results = manager.search_words(search_term)
        if results:
            for word in results:
                print(f"   ✓ {word.word} - {word.meaning}")
        else:
            print("   ✗ 未找到匹配结果")
        print()
    
    # 清理演示文件
    if os.path.exists("demo_words.json"):
        os.remove("demo_words.json")


def demo_interval_setting():
    """演示间隔设置功能"""
    print("⏰ 学习间隔设置演示")
    print("=" * 50)
    
    # 演示设置保存和加载
    settings = {
        'study_interval': 15
    }
    
    print("💾 保存设置...")
    with open("demo_settings.json", 'w', encoding='utf-8') as f:
        json.dump(settings, f, ensure_ascii=False, indent=2)
    
    print("📖 加载设置...")
    with open("demo_settings.json", 'r', encoding='utf-8') as f:
        loaded_settings = json.load(f)
    
    interval = loaded_settings.get('study_interval', 10)
    print(f"✅ 学习间隔设置为: {interval} 分钟")
    print()
    
    # 演示间隔验证
    print("🔧 间隔时间验证:")
    test_intervals = [5, 15, 30, 0, 100, -5]
    
    for test_interval in test_intervals:
        # 验证逻辑
        valid_interval = max(1, min(60, test_interval))
        status = "✅" if test_interval == valid_interval else "⚠️"
        print(f"   {status} 输入: {test_interval}分钟 -> 有效: {valid_interval}分钟")
    
    print()
    
    # 清理演示文件
    if os.path.exists("demo_settings.json"):
        os.remove("demo_settings.json")


def show_usage_tips():
    """显示使用提示"""
    print("💡 使用提示")
    print("=" * 50)
    
    tips = [
        "🔍 搜索功能: 在搜索框中输入任何关键词，支持英文、中文、例句搜索",
        "⏰ 间隔设置: 可以设置1-60分钟的学习间隔，默认10分钟",
        "💾 自动保存: 设置会自动保存到settings.json文件",
        "📊 实时统计: 搜索时会显示总单词数和搜索结果数",
        "🎯 强制学习: 答对题目才能关闭弹窗，没有关闭按钮"
    ]
    
    for tip in tips:
        print(tip)
    
    print()
    print("🚀 现在可以运行程序体验这些功能了！")


if __name__ == "__main__":
    print("英语学习助手 - 新功能演示")
    print("=" * 60)
    print()
    
    demo_search_feature()
    demo_interval_setting()
    show_usage_tips()
    
    print("演示完成！") 