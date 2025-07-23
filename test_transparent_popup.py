#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试透明弹框效果
"""

import sys
import os

# 添加src目录到Python路径
current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, 'src')
if src_path not in sys.path:
    sys.path.insert(0, src_path)

try:
    from data.word_model import Word, WordManager
    from gui.study_popup import StudyPopup
except ImportError:
    from src.data.word_model import Word, WordManager
    from src.gui.study_popup import StudyPopup

def test_transparent_popup():
    """测试透明弹框"""
    print("🎯 测试透明弹框效果")
    print("=" * 50)
    
    # 创建测试数据
    word_manager = WordManager()
    
    # 添加一些测试单词
    test_words = [
        Word("apple", "苹果", "I eat an apple every day.", proficiency=2),
        Word("beautiful", "美丽的", "She is a beautiful girl.", proficiency=3),
        Word("computer", "电脑", "I work on my computer.", proficiency=1),
        Word("delicious", "美味的", "This food is delicious.", proficiency=4),
        Word("education", "教育", "Education is important.", proficiency=0),
        Word("freedom", "自由", "Freedom is precious.", proficiency=5),
    ]
    
    for word in test_words:
        word_manager.add_word(word.word, word.meaning, word.example)
    
    print(f"✅ 已添加 {len(test_words)} 个测试单词")
    
    # 选择第一个单词进行测试
    test_word = test_words[0]
    print(f"📝 测试单词: {test_word.word} - {test_word.meaning}")
    print(f"⭐ 熟练度: {test_word.proficiency}")
    
    # 创建弹框
    print("\n🚀 创建透明弹框...")
    popup = StudyPopup(None, test_word, word_manager)
    
    # 设置关闭回调
    def on_popup_closed():
        print("✅ 弹框已关闭")
    
    popup.set_close_callback(on_popup_closed)
    
    print("🎨 弹框特性:")
    print("   - 半透明背景 (95% 透明度)")
    print("   - 现代化UI设计")
    print("   - 悬停效果")
    print("   - 平滑淡出动画")
    print("   - 颜色反馈 (绿色=正确, 红色=错误)")
    
    print("\n💡 使用说明:")
    print("   1. 选择一个答案")
    print("   2. 观察颜色变化")
    print("   3. 答对会看到淡出效果")
    print("   4. 答错需要手动关闭")
    
    # 显示弹框
    print("\n🎯 显示弹框...")
    popup.show()

if __name__ == "__main__":
    try:
        test_transparent_popup()
    except Exception as e:
        print(f"❌ 测试失败: {e}")
        import traceback
        traceback.print_exc() 