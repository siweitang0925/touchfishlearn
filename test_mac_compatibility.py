#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mac兼容性测试脚本
"""

import sys
import os
import platform

def test_imports():
    """测试模块导入"""
    print("=== 测试模块导入 ===")
    
    try:
        import tkinter
        print("✅ tkinter 导入成功")
    except ImportError as e:
        print(f"❌ tkinter 导入失败: {e}")
        return False
    
    try:
        from tkinter import ttk, messagebox
        print("✅ tkinter 子模块导入成功")
    except ImportError as e:
        print(f"❌ tkinter 子模块导入失败: {e}")
        return False
    
    try:
        import json
        print("✅ json 导入成功")
    except ImportError as e:
        print(f"❌ json 导入失败: {e}")
        return False
    
    try:
        import threading
        print("✅ threading 导入成功")
    except ImportError as e:
        print(f"❌ threading 导入失败: {e}")
        return False
    
    try:
        import pystray
        print("✅ pystray 导入成功")
    except ImportError as e:
        print(f"❌ pystray 导入失败: {e}")
        print("请运行: pip3 install pystray")
        return False
    
    try:
        from PIL import Image, ImageDraw
        print("✅ Pillow 导入成功")
    except ImportError as e:
        print(f"❌ Pillow 导入失败: {e}")
        print("请运行: pip3 install pillow")
        return False
    
    return True

def test_path_setup():
    """测试路径设置"""
    print("\n=== 测试路径设置 ===")
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    src_path = os.path.join(current_dir, 'src')
    
    print(f"当前目录: {current_dir}")
    print(f"src目录: {src_path}")
    print(f"src目录存在: {os.path.exists(src_path)}")
    
    if not os.path.exists(src_path):
        print("❌ src目录不存在")
        return False
    
    # 添加src到Python路径
    if src_path not in sys.path:
        sys.path.insert(0, src_path)
        print("✅ src目录已添加到Python路径")
    
    return True

def test_module_imports():
    """测试项目模块导入"""
    print("\n=== 测试项目模块导入 ===")
    
    try:
        from data.word_model import Word, WordManager
        print("✅ Word, WordManager 导入成功")
    except ImportError as e:
        print(f"❌ Word, WordManager 导入失败: {e}")
        try:
            from src.data.word_model import Word, WordManager
            print("✅ 使用绝对路径导入成功")
        except ImportError as e2:
            print(f"❌ 绝对路径导入也失败: {e2}")
            return False
    
    try:
        from gui.main_window import MainWindow
        print("✅ MainWindow 导入成功")
    except ImportError as e:
        print(f"❌ MainWindow 导入失败: {e}")
        try:
            from src.gui.main_window import MainWindow
            print("✅ 使用绝对路径导入成功")
        except ImportError as e2:
            print(f"❌ 绝对路径导入也失败: {e2}")
            return False
    
    try:
        from gui.study_popup import StudyPopup
        print("✅ StudyPopup 导入成功")
    except ImportError as e:
        print(f"❌ StudyPopup 导入失败: {e}")
        try:
            from src.gui.study_popup import StudyPopup
            print("✅ 使用绝对路径导入成功")
        except ImportError as e2:
            print(f"❌ 绝对路径导入也失败: {e2}")
            return False
    
    return True

def test_system_info():
    """测试系统信息"""
    print("\n=== 系统信息 ===")
    print(f"操作系统: {platform.system()}")
    print(f"系统版本: {platform.release()}")
    print(f"Python版本: {sys.version}")
    print(f"Python路径: {sys.executable}")
    
    if platform.system() == "Darwin":
        print("✅ 检测到macOS系统")
    else:
        print(f"⚠️ 当前系统: {platform.system()}")

def test_file_permissions():
    """测试文件权限"""
    print("\n=== 测试文件权限 ===")
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    test_file = os.path.join(current_dir, "test_permissions.json")
    
    try:
        # 测试写入权限
        with open(test_file, 'w', encoding='utf-8') as f:
            f.write('{"test": "data"}')
        print("✅ 文件写入权限正常")
        
        # 测试读取权限
        with open(test_file, 'r', encoding='utf-8') as f:
            data = f.read()
        print("✅ 文件读取权限正常")
        
        # 清理测试文件
        os.remove(test_file)
        print("✅ 文件删除权限正常")
        
    except Exception as e:
        print(f"❌ 文件权限测试失败: {e}")
        return False
    
    return True

def main():
    """主测试函数"""
    print("英语学习助手 - Mac兼容性测试")
    print("=" * 50)
    
    # 测试系统信息
    test_system_info()
    
    # 测试基础导入
    if not test_imports():
        print("\n❌ 基础模块导入失败，请安装必要的依赖")
        return False
    
    # 测试路径设置
    if not test_path_setup():
        print("\n❌ 路径设置失败")
        return False
    
    # 测试项目模块导入
    if not test_module_imports():
        print("\n❌ 项目模块导入失败")
        return False
    
    # 测试文件权限
    if not test_file_permissions():
        print("\n❌ 文件权限测试失败")
        return False
    
    print("\n" + "=" * 50)
    print("✅ 所有测试通过！Mac兼容性良好")
    print("可以开始编译Mac版本了")
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1) 