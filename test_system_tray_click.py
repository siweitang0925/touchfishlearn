"""
测试系统栏图标单击功能
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.gui.main_window import MainWindow
import tkinter as tk

def test_system_tray_click():
    """测试系统栏图标单击功能"""
    print("=== 测试系统栏图标单击功能 ===")
    
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
    print("3. 测试单击系统栏图标 - 应该显示主窗口")
    print("4. 再次最小化程序")
    print("5. 再次测试单击系统栏图标 - 应该再次显示主窗口")
    print("6. 测试右键托盘图标菜单功能")
    
    print("\n新增功能:")
    print("- 支持单击系统栏图标显示主窗口")
    print("- 支持窗口最小化事件处理")
    print("- 支持窗口恢复事件处理")
    print("- 托盘图标保持运行，可以重复使用")
    
    print("\n测试方法:")
    print("- 方法1: 单击系统托盘区域的蓝色'EN'图标")
    print("- 方法2: 右键系统托盘图标，选择'显示主窗口'")
    print("- 方法3: 点击主窗口的最小化按钮，然后测试系统栏图标")
    
    # 运行主窗口
    main_window.run()

if __name__ == "__main__":
    test_system_tray_click() 