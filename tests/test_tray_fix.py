"""
测试托盘图标修复
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.gui.main_window import MainWindow
import tkinter as tk

def test_tray_fix():
    """测试托盘图标修复"""
    print("=== 测试托盘图标修复 ===")
    
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
    print("修复内容:")
    print("1. 避免重复最小化事件触发")
    print("2. 改进托盘图标创建和启动逻辑")
    print("3. 添加调试信息")
    print("4. 优化单击事件处理")
    
    print("\n测试步骤:")
    print("1. 启动摸鱼学习模式")
    print("2. 观察控制台输出，应该只显示一次'程序已最小化到系统托盘'")
    print("3. 单击系统托盘图标")
    print("4. 观察控制台输出，应该显示'托盘图标被单击'和'正在显示主窗口'")
    print("5. 主窗口应该显示出来")
    
    # 运行主窗口
    main_window.run()

if __name__ == "__main__":
    test_tray_fix() 