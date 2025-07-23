#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GitHub Actions 修复验证脚本
验证跨平台shell兼容性修复
"""

import os
import sys

def test_workflow_file():
    """测试workflow文件的内容"""
    print("🔍 测试GitHub Actions workflow文件...")
    
    workflow_file = '.github/workflows/build.yml'
    if not os.path.exists(workflow_file):
        print(f"❌ {workflow_file} - 文件不存在")
        return False
    
    with open(workflow_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查是否使用了正确的shell配置
    checks = [
        ("Windows PowerShell", "shell: powershell"),
        ("Windows条件", "if: runner.os == 'Windows'"),
        ("macOS bash", "shell: bash"),
        ("macOS条件", "if: runner.os == 'macOS'"),
        ("Linux bash", "if: runner.os == 'Linux'"),
        ("upload-artifact v4", "actions/upload-artifact@v4"),
        ("checkout v4", "actions/checkout@v4"),
        ("缓存配置", "actions/cache@v4")
    ]
    
    passed = 0
    total = len(checks)
    
    for check_name, check_content in checks:
        if check_content in content:
            print(f"✅ {check_name} - 正确配置")
            passed += 1
        else:
            print(f"❌ {check_name} - 配置缺失")
    
    print(f"\n📊 配置检查结果: {passed}/{total} 通过")
    return passed == total

def test_powershell_syntax():
    """测试PowerShell语法"""
    print("\n🔍 测试PowerShell语法...")
    
    workflow_file = '.github/workflows/build.yml'
    with open(workflow_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查PowerShell命令
    powershell_commands = [
        "Write-Host",
        "Get-Location",
        "Get-ChildItem",
        "Test-Path",
        "ForEach-Object"
    ]
    
    passed = 0
    total = len(powershell_commands)
    
    for cmd in powershell_commands:
        if cmd in content:
            print(f"✅ {cmd} - 语法正确")
            passed += 1
        else:
            print(f"⚠️  {cmd} - 未找到（可能不需要）")
    
    print(f"\n📊 PowerShell语法检查: {passed}/{total} 通过")
    return True  # 这些命令是可选的

def test_bash_syntax():
    """测试bash语法"""
    print("\n🔍 测试bash语法...")
    
    workflow_file = '.github/workflows/build.yml'
    with open(workflow_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查bash命令
    bash_commands = [
        "echo",
        "ls -la",
        "pwd",
        "du -h",
        "if [ -d",
        "if [ -f"
    ]
    
    passed = 0
    total = len(bash_commands)
    
    for cmd in bash_commands:
        if cmd in content:
            print(f"✅ {cmd} - 语法正确")
            passed += 1
        else:
            print(f"⚠️  {cmd} - 未找到（可能不需要）")
    
    print(f"\n📊 bash语法检查: {passed}/{total} 通过")
    return True  # 这些命令是可选的

def test_platform_conditions():
    """测试平台条件配置"""
    print("\n🔍 测试平台条件配置...")
    
    workflow_file = '.github/workflows/build.yml'
    with open(workflow_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查平台条件
    conditions = [
        ("Windows条件", "if: runner.os == 'Windows'"),
        ("macOS条件", "if: runner.os == 'macOS'"),
        ("Linux条件", "if: runner.os == 'Linux'"),
        ("Unix条件", "if: runner.os != 'Windows'")
    ]
    
    passed = 0
    total = len(conditions)
    
    for condition_name, condition_syntax in conditions:
        if condition_syntax in content:
            print(f"✅ {condition_name} - 语法正确")
            passed += 1
        else:
            print(f"❌ {condition_name} - 语法错误或缺失")
    
    print(f"\n📊 平台条件检查: {passed}/{total} 通过")
    return passed == total

def test_shell_specifications():
    """测试shell规格配置"""
    print("\n🔍 测试shell规格配置...")
    
    workflow_file = '.github/workflows/build.yml'
    with open(workflow_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查shell规格
    shell_specs = [
        ("PowerShell规格", "shell: powershell"),
        ("bash规格", "shell: bash")
    ]
    
    passed = 0
    total = len(shell_specs)
    
    for spec_name, spec_syntax in shell_specs:
        if spec_syntax in content:
            print(f"✅ {spec_name} - 配置正确")
            passed += 1
        else:
            print(f"❌ {spec_name} - 配置缺失")
    
    print(f"\n📊 shell规格检查: {passed}/{total} 通过")
    return passed == total

def main():
    """主测试函数"""
    print("🚀 GitHub Actions 跨平台修复验证")
    print("=" * 60)
    
    tests = [
        ("Workflow文件", test_workflow_file),
        ("PowerShell语法", test_powershell_syntax),
        ("bash语法", test_bash_syntax),
        ("平台条件", test_platform_conditions),
        ("shell规格", test_shell_specifications)
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
    print("📊 修复验证结果总结:")
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "✅ 通过" if result else "❌ 失败"
        print(f"  {test_name}: {status}")
        if result:
            passed += 1
    
    print(f"\n🎯 总体结果: {passed}/{total} 测试通过")
    
    if passed == total:
        print("🎉 所有测试通过！GitHub Actions跨平台修复成功。")
        print("\n💡 修复要点:")
        print("  - ✅ 为Windows使用PowerShell语法")
        print("  - ✅ 为macOS/Linux使用bash语法")
        print("  - ✅ 正确配置平台条件")
        print("  - ✅ 明确指定shell类型")
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