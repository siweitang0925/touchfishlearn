#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
验证artifacts名称修复
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

def check_workflow_artifacts():
    """检查workflow文件中的artifacts配置"""
    print("🔍 检查GitHub Actions artifacts配置...")
    
    workflow_file = '.github/workflows/build.yml'
    if not os.path.exists(workflow_file):
        print("❌ workflow文件不存在")
        return False
    
    with open(workflow_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查artifacts名称
    artifacts_checks = [
        ("artifacts名称", "name: English-Learning-Assistant"),
        ("artifacts路径", "path: dist/"),
        ("保留天数", "retention-days: 30"),
        ("错误处理", "if-no-files-found: error"),
    ]
    
    print("\n📋 artifacts配置检查:")
    passed = 0
    total = len(artifacts_checks)
    
    for check_name, check_content in artifacts_checks:
        if check_content in content:
            print(f"  ✅ {check_name}")
            passed += 1
        else:
            print(f"  ❌ {check_name} - 缺失")
    
    # 检查是否还有中文名称
    chinese_names = [
        "英语学习助手",
        "name: 英语学习助手",
    ]
    
    print("\n📋 中文名称检查:")
    chinese_found = False
    for chinese_name in chinese_names:
        if chinese_name in content:
            print(f"  ❌ 发现中文名称: {chinese_name}")
            chinese_found = True
    
    if not chinese_found:
        print("  ✅ 没有发现中文名称")
        passed += 1
        total += 1
    
    print(f"\n📊 artifacts配置检查: {passed}/{total} 通过")
    return passed == total

def check_spec_file():
    """检查spec文件中的名称"""
    print("\n🔍 检查spec文件...")
    
    spec_file = 'build_utf8.spec'
    if not os.path.exists(spec_file):
        print(f"❌ {spec_file} 不存在")
        return False
    
    with open(spec_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查spec文件配置
    spec_checks = [
        ("英文名称", "name='English-Learning-Assistant'"),
        ("UTF-8编码声明", "# -*- mode: python ; coding: utf-8 -*-"),
    ]
    
    print("\n📋 spec文件检查:")
    passed = 0
    total = len(spec_checks)
    
    for check_name, check_content in spec_checks:
        if check_content in content:
            print(f"  ✅ {check_name}")
            passed += 1
        else:
            print(f"  ❌ {check_name} - 缺失")
    
    # 检查是否还有中文名称
    if "英语学习助手" in content:
        print("  ❌ 发现中文名称")
        return False
    else:
        print("  ✅ 没有中文名称")
        passed += 1
        total += 1
    
    print(f"\n📊 spec文件检查: {passed}/{total} 通过")
    return passed == total

def show_fix_summary():
    """显示修复总结"""
    print("\n📋 artifacts名称修复总结:")
    print("=" * 60)
    print("✅ 修复了artifacts名称:")
    print("   - 将 '英语学习助手-${{ runner.os }}' 改为 'English-Learning-Assistant-${{ runner.os }}'")
    print("   - 使用英文名称避免下载时乱码")
    print("\n✅ 修复了可执行文件名称:")
    print("   - 将 '英语学习助手' 改为 'English-Learning-Assistant'")
    print("   - 在所有平台的构建命令中统一使用英文名称")
    print("\n✅ 修复了spec文件:")
    print("   - 更新了build_utf8.spec中的名称")
    print("   - 保持了UTF-8编码支持")
    print("\n🚀 现在artifacts下载时应该不会出现乱码了！")

def main():
    """主函数"""
    print("🚀 artifacts名称修复验证")
    print("=" * 60)
    
    # 检查workflow文件
    workflow_ok = check_workflow_artifacts()
    
    # 检查spec文件
    spec_ok = check_spec_file()
    
    # 显示修复总结
    show_fix_summary()
    
    # 总结
    print("\n" + "=" * 60)
    print("📊 验证结果总结:")
    print(f"  Workflow配置: {'✅ 正确' if workflow_ok else '❌ 有问题'}")
    print(f"  Spec文件: {'✅ 正确' if spec_ok else '❌ 有问题'}")
    
    if workflow_ok and spec_ok:
        print("\n🎉 artifacts名称修复完成！")
        return True
    else:
        print("\n⚠️  请检查上述问题。")
        return False

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"❌ 验证脚本异常: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1) 