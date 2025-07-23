"""
测试主程序最小化后弹框独立显示功能
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.gui.main_window import MainWindow
import threading
import time

def test_minimized_popup():
    """测试最小化后弹框独立显示"""
    print("=== 测试最小化后弹框独立显示功能 ===")
    
    # 创建主窗口
    main_window = MainWindow()
    
    # 添加一些测试单词
    word_manager = main_window.word_manager
    if len(word_manager.words) == 0:
        print("添加测试单词...")
        word_manager.add_word("apple", "苹果", "I eat an apple every day.")
        word_manager.add_word("book", "书", "I read a book.")
        word_manager.add_word("cat", "猫", "The cat is sleeping.")
        word_manager.add_word("dog", "狗", "The dog is running.")
        word_manager.add_word("elephant", "大象", "The elephant is big.")
        word_manager.add_word("fish", "鱼", "The fish is swimming.")
    
    print("主窗口已创建")
    print("请手动启动摸鱼学习模式，然后最小化到系统托盘")
    print("观察弹框是否能独立显示（不依赖主窗口）")
    
    # 运行主窗口
    main_window.run()

if __name__ == "__main__":
    test_minimized_popup() 