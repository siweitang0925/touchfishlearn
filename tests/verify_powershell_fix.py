#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
验证PowerShell语法修复
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

def check_workflow_file():
    """检查workflow文件中的PowerShell语法"""
    print("🔍 检查GitHub Actions workflow文件...")
    
    workflow_file = '.github/workflows/build.yml'
    if not os.path.exists(workflow_file):
        print("❌ workflow文件不存在")
        return False
    
    with open(workflow_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查PowerShell语法
    powershell_checks = [
        ("PowerShell条件判断", "if (Test-Path"),
        ("PowerShell大括号", "} else {"),
        ("PowerShell命令", "Write-Host"),
        ("PowerShell环境变量", "$env:PYTHONIOENCODING"),
        ("PowerShell文件检查", "Test-Path"),
        ("PowerShell目录检查", "Test-Path \"dist\""),
        ("PowerShell文件列表", "Get-ChildItem"),
        ("PowerShell文件大小", "ForEach-Object"),
    ]
    
    bash_checks = [
        ("bash条件判断", "if [ -f"),
        ("bash文件检查", "if [ -d"),
        ("bash命令", "echo"),
        ("bash环境变量", "export"),
        ("bash文件列表", "ls -la"),
        ("bash文件大小", "du -h"),
    ]
    
    print("\n📋 PowerShell语法检查:")
    powershell_passed = 0
    total_powershell = len(powershell_checks)
    
    for check_name, check_content in powershell_checks:
        if check_content in content:
            print(f"  ✅ {check_name}")
            powershell_passed += 1
        else:
            print(f"  ❌ {check_name} - 缺失")
    
    print(f"\n📋 bash语法检查:")
    bash_passed = 0
    total_bash = len(bash_checks)
    
    for check_name, check_content in bash_checks:
        if check_content in content:
            print(f"  ✅ {check_name}")
            bash_passed += 1
        else:
            print(f"  ❌ {check_name} - 缺失")
    
    # 检查是否有错误的语法混合
    print("\n🔍 检查语法混合问题:")
    mixed_issues = []
    
    # 检查Windows步骤中是否有bash语法
    windows_section = content.split("Build executable (Windows)")[1].split("Build executable (macOS)")[0]
    if "if [" in windows_section or "fi" in windows_section:
        mixed_issues.append("Windows步骤中包含bash语法")
    
    # 检查Unix步骤中是否有PowerShell语法
    unix_sections = content.split("Build executable (macOS)")[1] + content.split("Build executable (Linux)")[1]
    if "Write-Host" in unix_sections or "Test-Path" in unix_sections:
        mixed_issues.append("Unix步骤中包含PowerShell语法")
    
    if mixed_issues:
        print("  ❌ 发现语法混合问题:")
        for issue in mixed_issues:
            print(f"    - {issue}")
    else:
        print("  ✅ 没有发现语法混合问题")
    
    print(f"\n📊 检查结果:")
    print(f"  PowerShell语法: {powershell_passed}/{total_powershell} 通过")
    print(f"  bash语法: {bash_passed}/{total_bash} 通过")
    print(f"  语法混合: {'❌ 有问题' if mixed_issues else '✅ 正常'}")
    
    return powershell_passed == total_powershell and bash_passed == total_bash and not mixed_issues

def check_shell_specifications():
    """检查shell规范"""
    print("\n🔍 检查shell规范...")
    
    workflow_file = '.github/workflows/build.yml'
    with open(workflow_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    shell_checks = [
        ("Windows PowerShell", "shell: powershell"),
        ("macOS bash", "shell: bash"),
        ("Linux bash", "shell: bash"),
    ]
    
    passed = 0
    total = len(shell_checks)
    
    for check_name, check_content in shell_checks:
        if check_content in content:
            print(f"  ✅ {check_name}")
            passed += 1
        else:
            print(f"  ❌ {check_name} - 缺失")
    
    print(f"\n📊 shell规范检查: {passed}/{total} 通过")
    return passed == total

def check_platform_conditions():
    """检查平台条件"""
    print("\n🔍 检查平台条件...")
    
    workflow_file = '.github/workflows/build.yml'
    with open(workflow_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    condition_checks = [
        ("Windows条件", "if: runner.os == 'Windows'"),
        ("macOS条件", "if: runner.os == 'macOS'"),
        ("Linux条件", "if: runner.os == 'Linux'"),
    ]
    
    passed = 0
    total = len(condition_checks)
    
    for check_name, check_content in condition_checks:
        if check_content in content:
            print(f"  ✅ {check_name}")
            passed += 1
        else:
            print(f"  ❌ {check_name} - 缺失")
    
    print(f"\n📊 平台条件检查: {passed}/{total} 通过")
    return passed == total

def show_fix_summary():
    """显示修复总结"""
    print("\n📋 PowerShell语法修复总结:")
    print("=" * 60)
    print("✅ 修复了Windows PowerShell步骤中的bash语法:")
    print("   - 将 'if [ -f \"build_utf8.spec\" ]' 改为 'if (Test-Path \"build_utf8.spec\")'")
    print("   - 将 'else' 改为 '} else {'")
    print("   - 将 'fi' 改为 '}'")
    print("\n✅ 保持了Unix步骤中的bash语法:")
    print("   - macOS和Linux步骤继续使用bash语法")
    print("   - 保持了跨平台兼容性")
    print("\n✅ 确保了正确的shell规范:")
    print("   - Windows使用 'shell: powershell'")
    print("   - macOS和Linux使用 'shell: bash'")
    print("\n🚀 现在GitHub Actions应该可以正常构建了！")

def main():
    """主函数"""
    print("🚀 PowerShell语法修复验证")
    print("=" * 60)
    
    # 检查workflow文件
    workflow_ok = check_workflow_file()
    
    # 检查shell规范
    shell_ok = check_shell_specifications()
    
    # 检查平台条件
    condition_ok = check_platform_conditions()
    
    # 显示修复总结
    show_fix_summary()
    
    # 总结
    print("\n" + "=" * 60)
    print("📊 验证结果总结:")
    print(f"  Workflow语法: {'✅ 正确' if workflow_ok else '❌ 有问题'}")
    print(f"  Shell规范: {'✅ 正确' if shell_ok else '❌ 有问题'}")
    print(f"  平台条件: {'✅ 正确' if condition_ok else '❌ 有问题'}")
    
    if workflow_ok and shell_ok and condition_ok:
        print("\n🎉 PowerShell语法修复完成！")
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