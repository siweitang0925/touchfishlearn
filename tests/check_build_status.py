#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
检查构建状态和产物
"""

import os
import sys
import subprocess
import json

def check_local_build():
    """检查本地构建产物"""
    print("🔍 检查本地构建产物...")
    
    dist_dir = "dist"
    if not os.path.exists(dist_dir):
        print("❌ dist目录不存在")
        return False
    
    files = os.listdir(dist_dir)
    if not files:
        print("❌ dist目录为空")
        return False
    
    print(f"✅ 找到 {len(files)} 个构建产物:")
    for file in files:
        file_path = os.path.join(dist_dir, file)
        size = os.path.getsize(file_path)
        size_mb = size / (1024 * 1024)
        print(f"  📦 {file} ({size_mb:.1f} MB)")
    
    return True

def check_github_workflow():
    """检查GitHub Actions配置"""
    print("\n🔍 检查GitHub Actions配置...")
    
    workflow_file = '.github/workflows/build.yml'
    if not os.path.exists(workflow_file):
        print("❌ workflow文件不存在")
        return False
    
    with open(workflow_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查关键配置
    checks = [
        ("上传产物配置", "actions/upload-artifact@v4"),
        ("产物名称", "英语学习助手-${{ runner.os }}"),
        ("产物路径", "path: dist/"),
        ("保留时间", "retention-days: 30"),
    ]
    
    all_passed = True
    for check_name, check_content in checks:
        if check_content in content:
            print(f"  ✅ {check_name}")
        else:
            print(f"  ❌ {check_name} - 缺失")
            all_passed = False
    
    return all_passed

def show_download_instructions():
    """显示下载说明"""
    print("\n📥 如何下载GitHub Actions构建产物:")
    print("=" * 60)
    print("1. 访问你的GitHub仓库")
    print("2. 点击 'Actions' 标签页")
    print("3. 找到成功的构建记录（绿色✓）")
    print("4. 点击构建记录")
    print("5. 在页面底部找到 'Artifacts' 部分")
    print("6. 下载对应平台的文件:")
    print("   - 英语学习助手-Windows (Windows版本)")
    print("   - 英语学习助手-macOS (macOS版本)")
    print("   - 英语学习助手-Linux (Linux版本)")
    print("\n💡 提示: 构建产物会保留30天")

def show_build_commands():
    """显示构建命令"""
    print("\n🔨 本地构建命令:")
    print("=" * 60)
    print("Windows:")
    print("  python -m PyInstaller --onefile --windowed --name '英语学习助手' main.py")
    print("\nmacOS:")
    print("  python3 -m PyInstaller build_mac.spec")
    print("\nLinux:")
    print("  python -m PyInstaller --onefile --name '英语学习助手' main.py")

def check_dependencies():
    """检查构建依赖"""
    print("\n🔍 检查构建依赖...")
    
    deps = ['pyinstaller', 'pystray', 'pillow']
    missing_deps = []
    
    for dep in deps:
        try:
            __import__(dep)
            print(f"  ✅ {dep}")
        except ImportError:
            print(f"  ❌ {dep} - 未安装")
            missing_deps.append(dep)
    
    if missing_deps:
        print(f"\n⚠️  缺少依赖: {missing_deps}")
        print("安装命令:")
        print(f"  pip install {' '.join(missing_deps)}")
        return False
    
    return True

def main():
    """主函数"""
    print("🚀 构建状态检查")
    print("=" * 60)
    
    # 检查本地构建
    local_build = check_local_build()
    
    # 检查GitHub Actions配置
    workflow_ok = check_github_workflow()
    
    # 检查依赖
    deps_ok = check_dependencies()
    
    # 显示说明
    show_download_instructions()
    show_build_commands()
    
    # 总结
    print("\n" + "=" * 60)
    print("📊 检查结果总结:")
    print(f"  本地构建产物: {'✅ 存在' if local_build else '❌ 不存在'}")
    print(f"  GitHub Actions配置: {'✅ 正确' if workflow_ok else '❌ 有问题'}")
    print(f"  构建依赖: {'✅ 完整' if deps_ok else '❌ 缺失'}")
    
    if local_build and workflow_ok and deps_ok:
        print("\n🎉 一切正常！可以开始构建了。")
        return True
    else:
        print("\n⚠️  请先解决上述问题。")
        return False

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"❌ 检查脚本异常: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1) 