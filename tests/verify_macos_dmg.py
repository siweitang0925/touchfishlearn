#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
验证macOS DMG配置
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

def check_workflow_macos():
    """检查workflow文件中的macOS DMG配置"""
    print("🔍 检查GitHub Actions macOS DMG配置...")
    
    workflow_file = '.github/workflows/build.yml'
    if not os.path.exists(workflow_file):
        print("❌ workflow文件不存在")
        return False
    
    with open(workflow_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查macOS DMG相关配置
    macos_checks = [
        ("create-dmg安装", "brew install create-dmg"),
        ("DMG包名称", "DMG_NAME=\"English-Learning-Assistant-macOS.dmg\""),
        ("应用名称", "APP_NAME=\"English-Learning-Assistant.app\""),
        ("临时目录创建", "TEMP_DIR=$(mktemp -d)"),
        ("Applications软链接", "ln -s /Applications"),
        ("应用复制", "cp -R \"dist/English-Learning-Assistant\""),
        ("create-dmg命令", "create-dmg \\"),
        ("卷名称", "--volname \"English Learning Assistant\""),
        ("窗口位置", "--window-pos 200 120"),
        ("窗口大小", "--window-size 600 400"),
        ("图标大小", "--icon-size 100"),
        ("应用图标", "--icon \"$APP_NAME\" 175 120"),
        ("隐藏扩展名", "--hide-extension \"$APP_NAME\""),
        ("Applications链接", "--app-drop-link 425 120"),
        ("清理临时文件", "rm -rf \"$TEMP_DIR\""),
    ]
    
    print("\n📋 macOS DMG配置检查:")
    passed = 0
    total = len(macos_checks)
    
    for check_name, check_content in macos_checks:
        if check_content in content:
            print(f"  ✅ {check_name}")
            passed += 1
        else:
            print(f"  ❌ {check_name} - 缺失")
    
    print(f"\n📊 macOS DMG配置检查: {passed}/{total} 通过")
    return passed == total

def check_dmg_script():
    """检查DMG构建脚本"""
    print("\n🔍 检查DMG构建脚本...")
    
    script_file = 'build_mac_dmg.sh'
    if not os.path.exists(script_file):
        print(f"❌ {script_file} 不存在")
        return False
    
    with open(script_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查脚本配置
    script_checks = [
        ("脚本头部", "#!/bin/bash"),
        ("编码设置", "export PYTHONIOENCODING=utf-8"),
        ("create-dmg检查", "command -v create-dmg"),
        ("brew安装", "brew install create-dmg"),
        ("PyInstaller构建", "python -m PyInstaller"),
        ("DMG名称", "DMG_NAME=\"English-Learning-Assistant-macOS.dmg\""),
        ("应用名称", "APP_NAME=\"English-Learning-Assistant.app\""),
        ("临时目录", "TEMP_DIR=$(mktemp -d)"),
        ("Applications软链接", "ln -s /Applications"),
        ("create-dmg命令", "create-dmg \\"),
        ("卷名称", "--volname \"English Learning Assistant\""),
        ("清理临时文件", "rm -rf \"$TEMP_DIR\""),
    ]
    
    print("\n📋 DMG构建脚本检查:")
    passed = 0
    total = len(script_checks)
    
    for check_name, check_content in script_checks:
        if check_content in content:
            print(f"  ✅ {check_name}")
            passed += 1
        else:
            print(f"  ❌ {check_name} - 缺失")
    
    print(f"\n📊 DMG构建脚本检查: {passed}/{total} 通过")
    return passed == total

def show_macos_dmg_summary():
    """显示macOS DMG配置总结"""
    print("\n📋 macOS DMG配置总结:")
    print("=" * 60)
    print("✅ 添加了macOS DMG打包功能:")
    print("   - 在GitHub Actions中安装create-dmg工具")
    print("   - 构建可执行文件后自动创建DMG包")
    print("   - DMG包名称: English-Learning-Assistant-macOS.dmg")
    print("\n✅ DMG包特性:")
    print("   - 包含Applications软链接")
    print("   - 美观的安装界面")
    print("   - 拖拽安装支持")
    print("   - 自动清理临时文件")
    print("\n✅ 创建了独立的DMG构建脚本:")
    print("   - build_mac_dmg.sh")
    print("   - 支持本地测试DMG打包")
    print("   - 包含完整的错误处理")
    print("\n🚀 现在macOS版本将生成标准的DMG安装包！")

def main():
    """主函数"""
    print("🚀 macOS DMG配置验证")
    print("=" * 60)
    
    # 检查workflow配置
    workflow_ok = check_workflow_macos()
    
    # 检查DMG脚本
    script_ok = check_dmg_script()
    
    # 显示配置总结
    show_macos_dmg_summary()
    
    # 总结
    print("\n" + "=" * 60)
    print("📊 验证结果总结:")
    print(f"  Workflow配置: {'✅ 正确' if workflow_ok else '❌ 有问题'}")
    print(f"  DMG脚本: {'✅ 正确' if script_ok else '❌ 有问题'}")
    
    if workflow_ok and script_ok:
        print("\n🎉 macOS DMG配置完成！")
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