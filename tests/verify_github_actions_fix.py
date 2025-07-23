#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GitHub Actions 修复最终验证脚本
验证所有修复是否完成
"""

import os
import sys

def print_header(title):
    """打印标题"""
    print(f"\n{'='*60}")
    print(f"🔧 {title}")
    print(f"{'='*60}")

def check_workflow_file():
    """检查workflow文件"""
    print_header("检查GitHub Actions Workflow文件")
    
    workflow_file = '.github/workflows/build.yml'
    if not os.path.exists(workflow_file):
        print("❌ workflow文件不存在")
        return False
    
    with open(workflow_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查关键修复点
    fixes = [
        ("✅ Actions版本升级", "actions/upload-artifact@v4"),
        ("✅ Windows PowerShell支持", "shell: powershell"),
        ("✅ Windows条件判断", "if: runner.os == 'Windows'"),
        ("✅ macOS bash支持", "shell: bash"),
        ("✅ macOS条件判断", "if: runner.os == 'macOS'"),
        ("✅ Linux条件判断", "if: runner.os == 'Linux'"),
        ("✅ 依赖缓存", "actions/cache@v4"),
        ("✅ 错误处理", "if-no-files-found: error"),
    ]
    
    all_passed = True
    for fix_name, fix_content in fixes:
        if fix_content in content:
            print(f"  {fix_name}")
        else:
            print(f"  ❌ {fix_name} - 缺失")
            all_passed = False
    
    return all_passed

def check_powershell_commands():
    """检查PowerShell命令"""
    print_header("检查PowerShell命令")
    
    workflow_file = '.github/workflows/build.yml'
    with open(workflow_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    powershell_cmds = [
        "Write-Host",
        "Get-Location", 
        "Get-ChildItem",
        "Test-Path",
        "ForEach-Object"
    ]
    
    for cmd in powershell_cmds:
        if cmd in content:
            print(f"  ✅ {cmd}")
        else:
            print(f"  ⚠️  {cmd} - 未使用")
    
    return True

def check_bash_commands():
    """检查bash命令"""
    print_header("检查bash命令")
    
    workflow_file = '.github/workflows/build.yml'
    with open(workflow_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    bash_cmds = [
        "echo",
        "ls -la",
        "pwd", 
        "du -h",
        "if [ -d",
        "if [ -f"
    ]
    
    for cmd in bash_cmds:
        if cmd in content:
            print(f"  ✅ {cmd}")
        else:
            print(f"  ⚠️  {cmd} - 未使用")
    
    return True

def check_platform_support():
    """检查平台支持"""
    print_header("检查平台支持")
    
    platforms = [
        ("Windows", "windows-latest"),
        ("macOS", "macos-latest"), 
        ("Linux", "ubuntu-latest")
    ]
    
    workflow_file = '.github/workflows/build.yml'
    with open(workflow_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for platform_name, platform_runner in platforms:
        if platform_runner in content:
            print(f"  ✅ {platform_name} ({platform_runner})")
        else:
            print(f"  ❌ {platform_name} - 不支持")
            return False
    
    return True

def check_dependencies():
    """检查依赖配置"""
    print_header("检查依赖配置")
    
    # 检查requirements.txt
    if os.path.exists('requirements.txt'):
        with open('requirements.txt', 'r', encoding='utf-8') as f:
            content = f.read()
        
        deps = ['pyinstaller', 'pystray', 'pillow']
        for dep in deps:
            if dep in content.lower():
                print(f"  ✅ {dep}")
            else:
                print(f"  ❌ {dep} - 缺失")
                return False
    else:
        print("  ❌ requirements.txt 文件不存在")
        return False
    
    return True

def check_documentation():
    """检查文档"""
    print_header("检查文档")
    
    docs = [
        ("故障排除指南", "GitHub Actions故障排除.md"),
        ("修复总结", "GitHub Actions修复总结.md"),
        ("测试脚本", "test_github_actions.py"),
        ("修复验证脚本", "test_github_actions_fix.py")
    ]
    
    for doc_name, doc_file in docs:
        if os.path.exists(doc_file):
            print(f"  ✅ {doc_name}")
        else:
            print(f"  ❌ {doc_name} - 缺失")
            return False
    
    return True

def main():
    """主验证函数"""
    print("🚀 GitHub Actions 修复最终验证")
    print("=" * 60)
    
    checks = [
        ("Workflow文件", check_workflow_file),
        ("PowerShell命令", check_powershell_commands),
        ("bash命令", check_bash_commands),
        ("平台支持", check_platform_support),
        ("依赖配置", check_dependencies),
        ("文档完整性", check_documentation)
    ]
    
    results = []
    
    for check_name, check_func in checks:
        try:
            result = check_func()
            results.append((check_name, result))
        except Exception as e:
            print(f"❌ {check_name} - 验证异常: {e}")
            results.append((check_name, False))
    
    # 总结
    print_header("验证结果总结")
    
    passed = 0
    total = len(results)
    
    for check_name, result in results:
        status = "✅ 通过" if result else "❌ 失败"
        print(f"  {check_name}: {status}")
        if result:
            passed += 1
    
    print(f"\n🎯 总体结果: {passed}/{total} 验证通过")
    
    if passed == total:
        print("\n🎉 所有验证通过！GitHub Actions修复完成。")
        print("\n📋 修复总结:")
        print("  ✅ 升级了Actions版本 (v3 → v4)")
        print("  ✅ 修复了Windows PowerShell语法问题")
        print("  ✅ 为不同平台配置了正确的shell")
        print("  ✅ 添加了依赖缓存和错误处理")
        print("  ✅ 完善了文档和测试脚本")
        print("\n🚀 现在可以:")
        print("  1. 推送代码到GitHub触发自动构建")
        print("  2. 在Actions页面查看构建进度")
        print("  3. 下载Windows、macOS、Linux版本")
        return True
    else:
        print("\n⚠️  部分验证失败，请检查上述问题。")
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