#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
英语学习助手 - 完整功能演示
"""

import sys
import os
import json

# 添加src目录到Python路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from data.word_model import WordManager


def demo_all_features():
    """演示所有功能"""
    print("🎓 英语学习助手 - 完整功能演示")
    print("=" * 60)
    
    # 创建管理器
    manager = WordManager("demo_all.json")
    
    # 添加示例单词
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
    
    print("📚 1. 生词本管理功能")
    print("-" * 30)
    for word, meaning, example in sample_words:
        success = manager.add_word(word, meaning, example)
        print(f"   {'✅' if success else '❌'} 添加: {word} - {meaning}")
    
    print(f"\n   总单词数: {manager.get_word_count()}")
    
    print("\n🔍 2. 搜索功能演示")
    print("-" * 30)
    search_tests = [
        ("apple", "英文单词搜索"),
        ("程序", "中文含义搜索"),
        ("prog", "部分英文搜索"),
        ("技术", "中文关键词搜索"),
        ("learn", "例句内容搜索")
    ]
    
    for search_term, description in search_tests:
        results = manager.search_words(search_term)
        print(f"   📝 {description}: '{search_term}' -> 找到 {len(results)} 个结果")
        for word in results:
            print(f"      ✓ {word.word} ({word.meaning})")
    
    print("\n⏰ 3. 学习间隔设置演示")
    print("-" * 30)
    
    # 演示设置保存和加载
    settings = {
        'study_interval': 15
    }
    
    with open("demo_settings.json", 'w', encoding='utf-8') as f:
        json.dump(settings, f, ensure_ascii=False, indent=2)
    
    with open("demo_settings.json", 'r', encoding='utf-8') as f:
        loaded_settings = json.load(f)
    
    interval = loaded_settings.get('study_interval', 10)
    print(f"   💾 设置保存: 学习间隔 {interval} 分钟")
    print(f"   📖 设置加载: 成功读取配置")
    
    # 演示间隔验证
    test_intervals = [5, 15, 30, 0, 100]
    print(f"   🔧 间隔验证:")
    for test_interval in test_intervals:
        valid_interval = max(1, min(60, test_interval))
        status = "✅" if test_interval == valid_interval else "⚠️"
        print(f"      {status} {test_interval}分钟 -> {valid_interval}分钟")
    
    print("\n🎯 4. 强制学习机制演示")
    print("-" * 30)
    print("   🚫 无关闭按钮 - 必须答对才能关闭弹窗")
    print("   ⏱️  自定义间隔 - 可设置1-60分钟的学习间隔")
    print("   🔄 后台运行 - 不影响正常工作")
    print("   💾 自动保存 - 设置和单词数据自动保存")
    
    print("\n🖥️  5. 系统托盘功能演示")
    print("-" * 30)
    print("   📦 自动最小化 - 启动学习后自动最小化到托盘")
    print("   🖱️  托盘菜单:")
    print("      - 显示主窗口")
    print("      - 停止学习")
    print("      - 退出程序")
    print("   🎨 托盘图标 - 蓝色'EN'图标，易于识别")
    
    print("\n💡 6. 使用建议")
    print("-" * 30)
    tips = [
        "合理添加20-50个单词，避免选项重复",
        "利用搜索功能快速找到特定单词",
        "根据工作强度调整学习间隔",
        "学习时程序最小化到托盘，不干扰工作",
        "坚持每天使用，效果更佳"
    ]
    
    for i, tip in enumerate(tips, 1):
        print(f"   {i}. {tip}")
    
    # 清理演示文件
    if os.path.exists("demo_all.json"):
        os.remove("demo_all.json")
    if os.path.exists("demo_settings.json"):
        os.remove("demo_settings.json")
    
    print("\n" + "=" * 60)
    print("🎉 功能演示完成！")
    print("🚀 现在可以运行主程序体验完整功能了！")
    print("💻 运行命令: python main.py")


if __name__ == "__main__":
    demo_all_features() 