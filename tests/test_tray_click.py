"""
测试托盘单击功能
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.gui.main_window import MainWindow
import tkinter as tk

def test_tray_click():
    """测试托盘单击功能"""
    print("=== 测试托盘单击功能 ===")
    
    # 创建主窗口
    main_window = MainWindow()
    
    # 添加一些测试单词
    word_manager = main_window.word_manager
    if len(word_manager.words) == 0:
        print("添加测试单词...")
        word_manager.add_word("apple", "苹果", "I eat an apple every day.")
        word_manager.add_word("book", "书", "I read a book.")
        word_manager.add_word("cat", "猫", "The cat is sleeping.")
    
    print("主窗口已创建")
    print("请手动启动摸鱼学习模式，然后最小化到系统托盘")
    print("测试功能:")
    print("1. 单击托盘图标应该显示主窗口")
    print("2. 右键托盘图标应该显示菜单")
    print("3. 菜单中的'显示主窗口'应该也能显示主窗口")
    
    # 运行主窗口
    main_window.run()

if __name__ == "__main__":
    test_tray_click() 