#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试最小化功能
"""

import sys
import os

# 添加src目录到Python路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_tray_import():
    """测试系统托盘模块导入"""
    print("=== 测试系统托盘模块 ===")
    
    try:
        import pystray
        from PIL import Image, ImageDraw
        print("✅ pystray 和 PIL 模块导入成功")
        print("pystray 模块可用")
        return True
    except ImportError as e:
        print(f"❌ 导入失败: {e}")
        print("请运行: pip install pystray Pillow")
        return False

def test_image_creation():
    """测试图标创建"""
    print("\n=== 测试图标创建 ===")
    
    try:
        from PIL import Image, ImageDraw
        
        # 创建测试图标
        image = Image.new('RGB', (64, 64), color='blue')
        draw = ImageDraw.Draw(image)
        draw.text((10, 20), "EN", fill='white')
        
        print("✅ 图标创建成功")
        return True
    except Exception as e:
        print(f"❌ 图标创建失败: {e}")
        return False

def test_tray_creation():
    """测试托盘创建"""
    print("\n=== 测试托盘创建 ===")
    
    try:
        import pystray
        from PIL import Image, ImageDraw
        
        # 创建图标
        image = Image.new('RGB', (64, 64), color='blue')
        draw = ImageDraw.Draw(image)
        draw.text((10, 20), "EN", fill='white')
        
        # 创建菜单
        def test_action():
            print("托盘菜单被点击")
        
        menu = pystray.Menu(
            pystray.MenuItem("测试", test_action)
        )
        
        # 创建托盘图标
        icon = pystray.Icon("test", image, "测试", menu)
        
        print("✅ 托盘图标创建成功")
        print("注意: 托盘图标会在后台运行，测试完成后请手动停止")
        
        return True
    except Exception as e:
        print(f"❌ 托盘创建失败: {e}")
        return False

def show_usage_instructions():
    """显示使用说明"""
    print("\n=== 使用说明 ===")
    print("1. 启动摸鱼学习后，程序会自动最小化到系统托盘")
    print("2. 在系统托盘中可以看到蓝色的'EN'图标")
    print("3. 右键点击托盘图标可以:")
    print("   - 显示主窗口")
    print("   - 停止学习")
    print("   - 退出程序")
    print("4. 学习弹窗会正常弹出，不受最小化影响")

if __name__ == "__main__":
    print("系统托盘功能测试")
    print("=" * 40)
    
    # 测试各个功能
    tray_available = test_tray_import()
    
    if tray_available:
        test_image_creation()
        test_tray_creation()
        show_usage_instructions()
    else:
        print("\n请先安装必要的依赖:")
        print("pip install pystray Pillow")
    
    print("\n测试完成！") 