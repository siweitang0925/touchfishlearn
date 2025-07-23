"""
测试托盘单击功能修复
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.gui.main_window import MainWindow
import tkinter as tk

def test_tray_click_fix():
    """测试托盘单击功能修复"""
    print("=== 测试托盘单击功能修复 ===")
    
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
    print("测试步骤:")
    print("1. 启动摸鱼学习模式")
    print("2. 程序会最小化到系统托盘")
    print("3. 测试单击托盘图标 - 应该显示主窗口")
    print("4. 再次最小化到托盘")
    print("5. 再次测试单击托盘图标 - 应该再次显示主窗口")
    print("6. 测试右键托盘图标菜单功能")
    
    print("\n修复内容:")
    print("- 托盘图标不再在显示主窗口时停止")
    print("- 托盘图标保持运行，可以重复使用")
    print("- 支持多次最小化和显示操作")
    
    # 运行主窗口
    main_window.run()

if __name__ == "__main__":
    test_tray_click_fix() 