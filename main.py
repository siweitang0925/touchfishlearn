#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
英语学习助手 - 主程序入口
"""

import sys
import os

# 获取当前文件所在目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 添加src目录到Python路径
src_path = os.path.join(current_dir, 'src')
if src_path not in sys.path:
    sys.path.insert(0, src_path)

# 添加当前目录到Python路径
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

def main():
    """主函数"""
    try:
        # 动态导入模块
        from src.gui.main_window import MainWindow
        
        # 创建并运行主窗口
        app = MainWindow()
        app.run()
    except ImportError as e:
        print(f"模块导入错误: {e}")
        print("尝试备用导入方式...")
        try:
            # 备用导入方式
            import importlib.util
            
            # 导入main_window
            main_window_path = os.path.join(current_dir, "src", "gui", "main_window.py")
            spec = importlib.util.spec_from_file_location("main_window", main_window_path)
            main_window_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(main_window_module)
            
            # 创建并运行主窗口
            app = main_window_module.MainWindow()
            app.run()
        except Exception as e2:
            print(f"备用导入也失败: {e2}")
            import traceback
            traceback.print_exc()
            input("按回车键退出...")
    except Exception as e:
        print(f"程序运行出错: {e}")
        import traceback
        traceback.print_exc()
        input("按回车键退出...")


if __name__ == "__main__":
    main() 