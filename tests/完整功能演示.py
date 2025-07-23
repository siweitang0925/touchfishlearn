#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
英语学习助手 - 完整功能演示（包含熟练度系统）
"""

import sys
import os
import json
from datetime import datetime, timedelta

# 添加src目录到Python路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from data.word_model import WordManager, Word


def demo_proficiency_system():
    """演示熟练度系统"""
    print("🎯 熟练度系统演示")
    print("=" * 50)
    
    # 创建管理器
    manager = WordManager("demo_proficiency.json")
    
    # 添加示例单词
    sample_words = [
        ("apple", "苹果", "I eat an apple every day.", 0),
        ("application", "应用程序", "This is a useful application.", 2),
        ("book", "书", "I love reading books.", 4),
        ("computer", "电脑", "I work on my computer.", 5),
        ("programming", "编程", "I enjoy programming.", 1),
        ("python", "Python语言", "Python is a great programming language.", 3),
        ("software", "软件", "This software is very useful.", 0),
        ("technology", "技术", "Technology is advancing rapidly.", 2),
        ("learning", "学习", "Learning is a lifelong process.", 5),
        ("education", "教育", "Education is important for everyone.", 1)
    ]
    
    print("📚 1. 单词熟练度初始化")
    print("-" * 30)
    for word, meaning, example, proficiency in sample_words:
        w = Word(word, meaning, example, proficiency=proficiency)
        manager.words.append(w)
        stars = "★" * proficiency + "☆" * (5 - proficiency)
        print(f"   {word:12} -> {stars} ({proficiency}/5)")
    
    print(f"\n   总单词数: {manager.get_word_count()}")
    
    # 显示可学习单词
    studyable_words = manager.get_studyable_words()
    print(f"   可学习单词数: {len(studyable_words)}")
    
    print("\n🔍 2. 可学习单词筛选")
    print("-" * 30)
    for word in studyable_words:
        stars = "★" * word.proficiency + "☆" * (5 - word.proficiency)
        status = "可学习" if word.proficiency < 5 else "一个月后可重新学习"
        print(f"   {word.word:12} {stars} - {status}")
    
    print("\n📈 3. 熟练度变化演示")
    print("-" * 30)
    
    # 演示熟练度增加
    test_word = "software"
    print(f"   测试单词: {test_word}")
    print(f"   初始熟练度: {manager.get_word(test_word).proficiency}")
    
    manager.increase_proficiency(test_word)
    print(f"   答对后熟练度: {manager.get_word(test_word).proficiency}")
    
    manager.increase_proficiency(test_word)
    print(f"   再次答对后熟练度: {manager.get_word(test_word).proficiency}")
    
    # 演示熟练度减少
    test_word2 = "book"
    print(f"\n   测试单词: {test_word2}")
    print(f"   初始熟练度: {manager.get_word(test_word2).proficiency}")
    
    manager.decrease_proficiency(test_word2)
    print(f"   答错后熟练度: {manager.get_word(test_word2).proficiency}")
    
    print("\n🎲 4. 随机单词选择演示")
    print("-" * 30)
    print("   随机选择测试（只从可学习单词中选择）:")
    for i in range(5):
        random_word = manager.get_random_word()
        if random_word:
            stars = "★" * random_word.proficiency + "☆" * (5 - random_word.proficiency)
            print(f"   第{i+1}次: {random_word.word:12} {stars}")
        else:
            print(f"   第{i+1}次: 没有可学习的单词")
    
    # 清理演示文件
    if os.path.exists("demo_proficiency.json"):
        os.remove("demo_proficiency.json")
    
    print("\n" + "=" * 50)


def demo_learning_mechanism():
    """演示学习机制"""
    print("🎓 学习机制演示")
    print("=" * 50)
    
    print("📝 1. 答题流程")
    print("-" * 30)
    steps = [
        "弹窗显示英文单词和熟练度星级",
        "显示6个中文选项",
        "用户选择答案",
        "答对：显示绿色勾号，熟练度+1，1秒后淡出关闭",
        "答错：显示红色叉号，显示例句，熟练度-1，弹框保持显示"
    ]
    
    for i, step in enumerate(steps, 1):
        print(f"   {i}. {step}")
    
    print("\n⭐ 2. 熟练度规则")
    print("-" * 30)
    rules = [
        "新添加的单词熟练度为0",
        "答对题目熟练度+1，答错熟练度-1",
        "熟练度范围：0-5",
        "熟练度达到5的单词一个月内不再弹出学习",
        "一个月后熟练度为5的单词会重新进入学习队列",
        "只有第一次答对才增加熟练度，答错会减少熟练度"
    ]
    
    for rule in rules:
        print(f"   • {rule}")
    
    print("\n🎯 3. 学习效果")
    print("-" * 30)
    effects = [
        "智能调度：优先学习熟练度低的单词",
        "避免重复：熟练度高的单词减少出现频率",
        "长期记忆：一个月后重新学习已掌握的单词",
        "即时反馈：答题结果立即影响熟练度",
        "进度可视：星级显示学习进度"
    ]
    
    for effect in effects:
        print(f"   ✓ {effect}")
    
    print("\n" + "=" * 50)


def demo_ui_features():
    """演示UI功能"""
    print("🖥️  UI功能演示")
    print("=" * 50)
    
    print("📋 1. 主界面功能")
    print("-" * 30)
    features = [
        "单词列表显示熟练度星级（★☆☆☆☆ 到 ★★★★★）",
        "搜索功能支持按单词、中文、例句搜索",
        "学习间隔设置（1-60分钟）",
        "状态栏显示总单词数和可学习单词数",
        "系统托盘自动最小化"
    ]
    
    for feature in features:
        print(f"   ✓ {feature}")
    
    print("\n🎨 2. 学习弹窗功能")
    print("-" * 30)
    popup_features = [
        "显示英文单词和熟练度星级",
        "6个中文选项随机排列",
        "答对显示绿色勾号（✓），1秒后自动关闭",
        "答错显示红色叉号（✗），显示例句",
        "答错后弹框保持显示，可手动关闭",
        "无关闭按钮，必须答题"
    ]
    
    for feature in popup_features:
        print(f"   ✓ {feature}")
    
    print("\n⚙️  3. 设置功能")
    print("-" * 30)
    settings = [
        "学习间隔自动保存",
        "单词数据自动保存",
        "熟练度数据自动保存",
        "程序设置自动保存"
    ]
    
    for setting in settings:
        print(f"   ✓ {setting}")
    
    print("\n" + "=" * 50)


def show_usage_tips():
    """显示使用技巧"""
    print("💡 使用技巧")
    print("=" * 50)
    
    print("🎯 1. 学习策略")
    print("-" * 30)
    strategies = [
        "合理添加20-50个单词，避免选项重复",
        "关注熟练度星级，了解学习进度",
        "利用搜索功能快速找到特定单词",
        "根据工作强度调整学习间隔",
        "坚持每天使用，效果更佳"
    ]
    
    for i, strategy in enumerate(strategies, 1):
        print(f"   {i}. {strategy}")
    
    print("\n🔧 2. 操作技巧")
    print("-" * 30)
    tips = [
        "双击单词列表中的单词进行编辑",
        "使用搜索框快速定位单词",
        "右键系统托盘图标访问菜单",
        "学习时程序最小化到托盘，不干扰工作",
        "熟练度达到5星的单词会暂时停止学习"
    ]
    
    for i, tip in enumerate(tips, 1):
        print(f"   {i}. {tip}")
    
    print("\n⚠️  3. 注意事项")
    print("-" * 30)
    notes = [
        "摸鱼学习模式启动后必须答题才能关闭",
        "没有关闭按钮，无法强制关闭测试窗口",
        "建议在开始工作前先添加足够的单词",
        "程序会自动保存所有数据，不会丢失"
    ]
    
    for note in notes:
        print(f"   • {note}")
    
    print("\n" + "=" * 50)


def main():
    """主演示函数"""
    print("🎓 英语学习助手 - 完整功能演示")
    print("包含熟练度系统、智能学习调度、系统托盘等新功能")
    print("=" * 60)
    
    demo_proficiency_system()
    demo_learning_mechanism()
    demo_ui_features()
    show_usage_tips()
    
    print("🎉 功能演示完成！")
    print("🚀 现在可以运行主程序体验完整功能了！")
    print("💻 运行命令: python main.py")
    print("📦 或直接运行: dist/英语学习助手.exe")


if __name__ == "__main__":
    main() 