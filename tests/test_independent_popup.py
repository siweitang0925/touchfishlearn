"""
测试独立弹框功能
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.data.word_model import Word, WordManager
from src.gui.study_popup import StudyPopup
import tkinter as tk

def test_independent_popup():
    """测试独立弹框"""
    print("=== 测试独立弹框功能 ===")
    
    # 创建单词管理器
    word_manager = WordManager()
    
    # 确保有测试数据
    if len(word_manager.words) == 0:
        print("添加测试单词...")
        word_manager.add_word("apple", "苹果", "I eat an apple every day.")
        word_manager.add_word("book", "书", "I read a book.")
        word_manager.add_word("cat", "猫", "The cat is sleeping.")
        word_manager.add_word("dog", "狗", "The dog is running.")
        word_manager.add_word("elephant", "大象", "The elephant is big.")
        word_manager.add_word("fish", "鱼", "The fish is swimming.")
    
    # 获取一个测试单词
    word = word_manager.get_random_word()
    if not word:
        print("没有可用的单词进行测试")
        return
    
    print(f"测试单词: {word.word} - {word.meaning}")
    print("创建独立弹框...")
    
    # 创建独立弹框（不传递父窗口）
    popup = StudyPopup(None, word, word_manager)
    
    def on_popup_closed():
        print("弹框已关闭")
    
    popup.set_close_callback(on_popup_closed)
    
    print("显示弹框...")
    popup.show()

if __name__ == "__main__":
    test_independent_popup() 