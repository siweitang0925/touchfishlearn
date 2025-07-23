#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试中文编码修复
"""

import sys
import os

# 设置控制台编码为UTF-8
if sys.platform.startswith('win'):
    try:
        import codecs
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())
        sys.stderr = codecs.getwriter('utf-8')(sys.stderr.detach())
    except:
        pass

def test_encoding_settings():
    """测试编码设置"""
    print("🔍 测试编码设置...")
    
    # 检查环境变量
    env_vars = [
        ('PYTHONIOENCODING', 'utf-8'),
        ('PYTHONUTF8', '1'),
        ('LANG', 'en_US.UTF-8'),
        ('LC_ALL', 'en_US.UTF-8')
    ]
    
    for var_name, expected_value in env_vars:
        actual_value = os.environ.get(var_name, '')
        if actual_value == expected_value:
            print(f"  ✅ {var_name} = {actual_value}")
        else:
            print(f"  ⚠️  {var_name} = {actual_value} (期望: {expected_value})")
    
    # 检查Python编码
    print(f"  📝 Python默认编码: {sys.getdefaultencoding()}")
    print(f"  📝 文件系统编码: {sys.getfilesystemencoding()}")

def test_chinese_display():
    """测试中文显示"""
    print("\n🔍 测试中文显示...")
    
    test_texts = [
        "英语学习助手",
        "摸鱼学习",
        "生词本",
        "例句",
        "熟练度"
    ]
    
    for text in test_texts:
        try:
            print(f"  ✅ {text}")
        except UnicodeEncodeError as e:
            print(f"  ❌ {text} - 编码错误: {e}")

def test_workflow_config():
    """测试workflow配置"""
    print("\n🔍 测试GitHub Actions配置...")
    
    workflow_file = '.github/workflows/build.yml'
    if not os.path.exists(workflow_file):
        print("❌ workflow文件不存在")
        return False
    
    with open(workflow_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查编码相关配置
    encoding_checks = [
        ("环境变量设置", "PYTHONIOENCODING: utf-8"),
        ("UTF-8支持", "PYTHONUTF8: 1"),
        ("语言设置", "LANG: en_US.UTF-8"),
        ("区域设置", "LC_ALL: en_US.UTF-8"),
        ("PowerShell编码设置", "$env:PYTHONIOENCODING"),
        ("bash编码设置", "export PYTHONIOENCODING"),
        ("UTF-8 spec文件", "build_utf8.spec"),
        ("隐藏导入", "--hidden-import=tkinter")
    ]
    
    passed = 0
    total = len(encoding_checks)
    
    for check_name, check_content in encoding_checks:
        if check_content in content:
            print(f"  ✅ {check_name}")
            passed += 1
        else:
            print(f"  ❌ {check_name} - 缺失")
    
    print(f"\n📊 编码配置检查: {passed}/{total} 通过")
    return passed == total

def test_spec_file():
    """测试spec文件"""
    print("\n🔍 测试spec文件...")
    
    spec_file = 'build_utf8.spec'
    if not os.path.exists(spec_file):
        print(f"❌ {spec_file} 不存在")
        return False
    
    with open(spec_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查spec文件配置
    spec_checks = [
        ("UTF-8编码声明", "# -*- mode: python ; coding: utf-8 -*-"),
        ("中文文件名", "name='英语学习助手'"),
        ("tkinter导入", "'tkinter'"),
        ("数据文件", "assets/data/ielts_1000_words.json"),
        ("src目录", "'src', 'src'")
    ]
    
    passed = 0
    total = len(spec_checks)
    
    for check_name, check_content in spec_checks:
        if check_content in content:
            print(f"  ✅ {check_name}")
            passed += 1
        else:
            print(f"  ❌ {check_name} - 缺失")
    
    print(f"\n📊 spec文件检查: {passed}/{total} 通过")
    return passed == total

def show_fix_summary():
    """显示修复总结"""
    print("\n📋 中文编码修复总结:")
    print("=" * 60)
    print("✅ 添加了环境变量设置:")
    print("   - PYTHONIOENCODING=utf-8")
    print("   - PYTHONUTF8=1")
    print("   - LANG=en_US.UTF-8")
    print("   - LC_ALL=en_US.UTF-8")
    print("\n✅ 创建了UTF-8 spec文件:")
    print("   - build_utf8.spec")
    print("   - 包含正确的编码声明")
    print("   - 包含所有必要的隐藏导入")
    print("\n✅ 更新了GitHub Actions配置:")
    print("   - 为每个平台设置编码环境变量")
    print("   - 使用UTF-8 spec文件")
    print("   - 添加了tkinter隐藏导入")
    print("\n🚀 现在可以:")
    print("   1. 推送代码触发GitHub Actions构建")
    print("   2. 生成的可执行文件应该正确显示中文")
    print("   3. 不再出现中文乱码问题")

def main():
    """主函数"""
    print("🚀 中文编码修复验证")
    print("=" * 60)
    
    # 测试编码设置
    test_encoding_settings()
    
    # 测试中文显示
    test_chinese_display()
    
    # 测试workflow配置
    workflow_ok = test_workflow_config()
    
    # 测试spec文件
    spec_ok = test_spec_file()
    
    # 显示修复总结
    show_fix_summary()
    
    # 总结
    print("\n" + "=" * 60)
    print("📊 验证结果总结:")
    print(f"  Workflow配置: {'✅ 正确' if workflow_ok else '❌ 有问题'}")
    print(f"  Spec文件: {'✅ 正确' if spec_ok else '❌ 有问题'}")
    
    if workflow_ok and spec_ok:
        print("\n🎉 中文编码修复完成！")
        return True
    else:
        print("\n⚠️  请检查上述问题。")
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