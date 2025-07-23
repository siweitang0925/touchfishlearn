#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试套件入口文件
统一管理和运行所有测试
"""

import sys
import os
import subprocess
import importlib.util

# 添加项目根目录到Python路径
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

def list_test_files():
    """列出所有测试文件"""
    test_files = []
    for file in os.listdir(current_dir):
        if file.endswith('.py') and file != 'run_tests.py':
            test_files.append(file)
    return sorted(test_files)

def categorize_tests():
    """对测试文件进行分类"""
    categories = {
        '功能测试': [],
        'GitHub Actions测试': [],
        '演示脚本': [],
        '兼容性测试': [],
        '构建测试': []
    }
    
    for file in list_test_files():
        if file.startswith('test_'):
            if 'github' in file.lower() or 'actions' in file.lower():
                categories['GitHub Actions测试'].append(file)
            elif 'mac' in file.lower() or 'compatibility' in file.lower():
                categories['兼容性测试'].append(file)
            elif 'build' in file.lower() or 'check' in file.lower():
                categories['构建测试'].append(file)
            else:
                categories['功能测试'].append(file)
        elif '演示' in file or 'demo' in file.lower():
            categories['演示脚本'].append(file)
        else:
            categories['功能测试'].append(file)
    
    return categories

def run_test_file(test_file):
    """运行单个测试文件"""
    print(f"\n🚀 运行测试: {test_file}")
    print("=" * 60)
    
    try:
        # 构建完整的文件路径
        test_path = os.path.join(current_dir, test_file)
        
        # 使用subprocess运行测试文件
        result = subprocess.run([sys.executable, test_path], 
                              capture_output=True, text=True, 
                              cwd=project_root, timeout=300,
                              encoding='utf-8', errors='replace')
        
        if result.returncode == 0:
            print("✅ 测试通过")
            if result.stdout:
                print(result.stdout)
        else:
            print("❌ 测试失败")
            if result.stderr:
                print(result.stderr)
            if result.stdout:
                print(result.stdout)
        
        return result.returncode == 0
        
    except subprocess.TimeoutExpired:
        print("⏰ 测试超时")
        return False
    except Exception as e:
        print(f"❌ 运行测试时出错: {e}")
        return False

def show_test_menu():
    """显示测试菜单"""
    categories = categorize_tests()
    
    print("🧪 英语学习助手测试套件")
    print("=" * 60)
    
    all_tests = []
    test_index = 1
    
    for category, tests in categories.items():
        if tests:
            print(f"\n📁 {category}:")
            for test in tests:
                print(f"  {test_index:2d}. {test}")
                all_tests.append(test)
                test_index += 1
    
    print(f"\n🎯 选项:")
    print(f"  {test_index:2d}. 运行所有测试")
    print(f"  {test_index + 1:2d}. 运行功能测试")
    print(f"  {test_index + 2:2d}. 运行GitHub Actions测试")
    print(f"  {test_index + 3:2d}. 运行演示脚本")
    print(f"  {test_index + 4:2d}. 退出")
    
    return all_tests, test_index

def run_all_tests():
    """运行所有测试"""
    print("🚀 运行所有测试...")
    print("=" * 60)
    
    test_files = list_test_files()
    passed = 0
    total = len(test_files)
    
    for test_file in test_files:
        if run_test_file(test_file):
            passed += 1
    
    print(f"\n📊 测试结果: {passed}/{total} 通过")
    return passed == total

def run_category_tests(category_name):
    """运行指定类别的测试"""
    categories = categorize_tests()
    if category_name in categories:
        tests = categories[category_name]
        if tests:
            print(f"🚀 运行{category_name}...")
            print("=" * 60)
            
            passed = 0
            total = len(tests)
            
            for test_file in tests:
                if run_test_file(test_file):
                    passed += 1
            
            print(f"\n📊 {category_name}结果: {passed}/{total} 通过")
            return passed == total
        else:
            print(f"⚠️  {category_name}中没有测试文件")
            return True
    else:
        print(f"❌ 未知的测试类别: {category_name}")
        return False

def main():
    """主函数"""
    if len(sys.argv) > 1:
        # 命令行参数模式
        if sys.argv[1] == 'all':
            success = run_all_tests()
        elif sys.argv[1] == 'category':
            if len(sys.argv) > 2:
                success = run_category_tests(sys.argv[2])
            else:
                print("❌ 请指定测试类别")
                return False
        elif sys.argv[1] == 'list':
            categories = categorize_tests()
            for category, tests in categories.items():
                if tests:
                    print(f"\n📁 {category}:")
                    for test in tests:
                        print(f"  - {test}")
            return True
        else:
            # 运行指定的测试文件
            test_file = sys.argv[1]
            if os.path.exists(os.path.join(current_dir, test_file)):
                success = run_test_file(test_file)
            else:
                print(f"❌ 测试文件不存在: {test_file}")
                return False
    else:
        # 交互模式
        all_tests, menu_index = show_test_menu()
        
        while True:
            try:
                choice = input(f"\n请选择测试 (1-{menu_index + 4}): ").strip()
                
                if choice.isdigit():
                    choice_num = int(choice)
                    
                    if 1 <= choice_num <= len(all_tests):
                        # 运行单个测试
                        test_file = all_tests[choice_num - 1]
                        success = run_test_file(test_file)
                        break
                    elif choice_num == menu_index:
                        # 运行所有测试
                        success = run_all_tests()
                        break
                    elif choice_num == menu_index + 1:
                        # 运行功能测试
                        success = run_category_tests('功能测试')
                        break
                    elif choice_num == menu_index + 2:
                        # 运行GitHub Actions测试
                        success = run_category_tests('GitHub Actions测试')
                        break
                    elif choice_num == menu_index + 3:
                        # 运行演示脚本
                        success = run_category_tests('演示脚本')
                        break
                    elif choice_num == menu_index + 4:
                        # 退出
                        print("👋 再见！")
                        return True
                    else:
                        print("❌ 无效选择，请重试")
                else:
                    print("❌ 请输入数字")
                    
            except KeyboardInterrupt:
                print("\n👋 再见！")
                return True
            except Exception as e:
                print(f"❌ 输入错误: {e}")
    
    # 显示最终结果
    print("\n" + "=" * 60)
    if success:
        print("🎉 所有测试通过！")
    else:
        print("⚠️  部分测试失败，请检查上述问题")
    
    return success

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"❌ 测试套件异常: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1) 