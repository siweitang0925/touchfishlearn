#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GitHub Actions 配置测试脚本
用于验证构建配置是否正确
"""

import sys
import os
import subprocess
import json

def test_imports():
    """测试所有必需的模块导入"""
    print("🔍 测试模块导入...")
    
    modules = [
        'tkinter',
        'pystray',
        'PIL',
        'json',
        'threading',
        'random',
        'datetime'
    ]
    
    failed_modules = []
    
    for module in modules:
        try:
            if module == 'PIL':
                import PIL
                print(f"✅ {module} - OK")
            else:
                __import__(module)
                print(f"✅ {module} - OK")
        except ImportError as e:
            print(f"❌ {module} - FAILED: {e}")
            failed_modules.append(module)
    
    if failed_modules:
        print(f"\n⚠️  失败的模块: {failed_modules}")
        return False
    else:
        print("✅ 所有模块导入成功")
        return True

def test_project_imports():
    """测试项目内部模块导入"""
    print("\n🔍 测试项目模块导入...")
    
    # 添加src目录到路径
    current_dir = os.path.dirname(os.path.abspath(__file__))
    src_path = os.path.join(current_dir, 'src')
    if src_path not in sys.path:
        sys.path.insert(0, src_path)
    
    project_modules = [
        ('data.word_model', 'Word'),
        ('data.word_model', 'WordManager'),
        ('gui.main_window', 'MainWindow'),
        ('gui.study_popup', 'StudyPopup')
    ]
    
    failed_modules = []
    
    for module_path, class_name in project_modules:
        try:
            module = __import__(module_path, fromlist=[class_name])
            getattr(module, class_name)
            print(f"✅ {module_path}.{class_name} - OK")
        except (ImportError, AttributeError) as e:
            print(f"❌ {module_path}.{class_name} - FAILED: {e}")
            failed_modules.append(f"{module_path}.{class_name}")
    
    if failed_modules:
        print(f"\n⚠️  失败的项目模块: {failed_modules}")
        return False
    else:
        print("✅ 所有项目模块导入成功")
        return True

def test_file_structure():
    """测试文件结构"""
    print("\n🔍 测试文件结构...")
    
    required_files = [
        'main.py',
        'requirements.txt',
        'src/__init__.py',
        'src/data/__init__.py',
        'src/data/word_model.py',
        'src/gui/__init__.py',
        'src/gui/main_window.py',
        'src/gui/study_popup.py',
        'assets/data/ielts_1000_words.json'
    ]
    
    missing_files = []
    
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path} - 存在")
        else:
            print(f"❌ {file_path} - 缺失")
            missing_files.append(file_path)
    
    if missing_files:
        print(f"\n⚠️  缺失的文件: {missing_files}")
        return False
    else:
        print("✅ 所有必需文件存在")
        return True

def test_pyinstaller():
    """测试PyInstaller配置"""
    print("\n🔍 测试PyInstaller...")
    
    try:
        # 检查PyInstaller是否安装
        result = subprocess.run(['pyinstaller', '--version'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print(f"✅ PyInstaller - {result.stdout.strip()}")
        else:
            print(f"❌ PyInstaller - 未安装或版本错误")
            return False
    except (subprocess.TimeoutExpired, FileNotFoundError):
        print("❌ PyInstaller - 未安装")
        return False
    
    # 检查spec文件
    spec_files = ['build_mac.spec']
    for spec_file in spec_files:
        if os.path.exists(spec_file):
            print(f"✅ {spec_file} - 存在")
        else:
            print(f"⚠️  {spec_file} - 缺失（可选）")
    
    return True

def test_github_actions_config():
    """测试GitHub Actions配置"""
    print("\n🔍 测试GitHub Actions配置...")
    
    workflow_file = '.github/workflows/build.yml'
    if os.path.exists(workflow_file):
        print(f"✅ {workflow_file} - 存在")
        
        # 检查配置内容
        with open(workflow_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 检查是否使用了v4版本的actions
        if 'actions/upload-artifact@v4' in content:
            print("✅ upload-artifact 使用 v4 版本")
        else:
            print("❌ upload-artifact 版本过旧")
            return False
            
        if 'actions/checkout@v4' in content:
            print("✅ checkout 使用 v4 版本")
        else:
            print("❌ checkout 版本过旧")
            return False
            
        return True
    else:
        print(f"❌ {workflow_file} - 缺失")
        return False

def test_requirements():
    """测试requirements.txt"""
    print("\n🔍 测试requirements.txt...")
    
    if not os.path.exists('requirements.txt'):
        print("❌ requirements.txt - 缺失")
        return False
    
    with open('requirements.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    
    required_packages = ['pyinstaller', 'pystray', 'pillow']
    missing_packages = []
    
    for package in required_packages:
        if package in content.lower():
            print(f"✅ {package} - 已包含")
        else:
            print(f"❌ {package} - 缺失")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n⚠️  缺失的包: {missing_packages}")
        return False
    else:
        print("✅ 所有必需包已包含")
        return True

def main():
    """主测试函数"""
    print("🚀 GitHub Actions 配置测试")
    print("=" * 60)
    
    tests = [
        ("模块导入", test_imports),
        ("项目模块导入", test_project_imports),
        ("文件结构", test_file_structure),
        ("PyInstaller", test_pyinstaller),
        ("GitHub Actions配置", test_github_actions_config),
        ("Requirements", test_requirements)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name} - 测试异常: {e}")
            results.append((test_name, False))
    
    # 总结
    print("\n" + "=" * 60)
    print("📊 测试结果总结:")
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "✅ 通过" if result else "❌ 失败"
        print(f"  {test_name}: {status}")
        if result:
            passed += 1
    
    print(f"\n🎯 总体结果: {passed}/{total} 测试通过")
    
    if passed == total:
        print("🎉 所有测试通过！GitHub Actions应该能正常工作。")
        return True
    else:
        print("⚠️  部分测试失败，请检查上述问题。")
        return False

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"❌ 测试脚本异常: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1) 