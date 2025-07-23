#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
最终PowerShell语法验证
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

def main():
    """主函数"""
    print("🔍 最终验证PowerShell语法修复...")
    
    workflow_file = '.github/workflows/build.yml'
    if not os.path.exists(workflow_file):
        print("❌ workflow文件不存在")
        return False
    
    with open(workflow_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("\n📋 检查结果:")
    
    # 检查Windows步骤
    if "Build executable (Windows)" in content:
        windows_start = content.find("Build executable (Windows)")
        windows_end = content.find("Build executable (macOS)", windows_start)
        if windows_end == -1:
            windows_end = content.find("List build artifacts", windows_start)
        
        windows_section = content[windows_start:windows_end]
        
        # 检查Windows步骤中的语法
        if "if (Test-Path" in windows_section:
            print("  ✅ Windows步骤使用PowerShell语法")
        else:
            print("  ❌ Windows步骤语法错误")
            return False
        
        # 检查Windows步骤中是否有bash语法
        if "if [" in windows_section or "fi" in windows_section:
            print("  ❌ Windows步骤中仍有bash语法")
            return False
        else:
            print("  ✅ Windows步骤中没有bash语法")
    
    # 检查macOS和Linux步骤
    if "if [ -f \"build_utf8.spec\" ]" in content:
        print("  ✅ Unix步骤使用bash语法")
    else:
        print("  ❌ Unix步骤语法错误")
        return False
    
    # 检查shell规范
    if "shell: powershell" in content and "shell: bash" in content:
        print("  ✅ Shell规范正确")
    else:
        print("  ❌ Shell规范错误")
        return False
    
    # 检查编码设置
    if "$env:PYTHONIOENCODING" in content and "export PYTHONIOENCODING" in content:
        print("  ✅ 编码设置正确")
    else:
        print("  ❌ 编码设置错误")
        return False
    
    print("\n🎉 PowerShell语法修复验证通过！")
    print("GitHub Actions现在应该可以正常构建了。")
    
    return True

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"❌ 验证脚本异常: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1) 