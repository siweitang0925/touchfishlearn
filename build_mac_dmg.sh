#!/bin/bash
# -*- coding: utf-8 -*-
"""
macOS DMG打包脚本
"""

set -e

echo "🚀 开始构建macOS DMG包..."

# 设置编码
export PYTHONIOENCODING=utf-8
export PYTHONUTF8=1
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8

# 检查是否安装了create-dmg
if ! command -v create-dmg &> /dev/null; then
    echo "📦 安装create-dmg..."
    brew install create-dmg
fi

# 构建可执行文件
echo "🔨 构建可执行文件..."
if [ -f "build_mac.spec" ]; then
    python -m PyInstaller build_mac.spec
elif [ -f "build_utf8.spec" ]; then
    python -m PyInstaller build_utf8.spec
else
    echo "📝 使用默认配置构建..."
    python -m PyInstaller --onefile --windowed --name "English-Learning-Assistant" --hidden-import=tkinter --hidden-import=tkinter.ttk main.py
fi

# 检查构建结果
if [ ! -f "dist/English-Learning-Assistant" ]; then
    echo "❌ 可执行文件构建失败"
    exit 1
fi

echo "✅ 可执行文件构建成功"

# 创建DMG
echo "📦 创建DMG包..."
DMG_NAME="English-Learning-Assistant-macOS.dmg"
APP_NAME="English-Learning-Assistant.app"

# 创建临时目录
TEMP_DIR=$(mktemp -d)
MOUNT_DIR="$TEMP_DIR/mount"

# 创建Applications软链接
mkdir -p "$MOUNT_DIR"
ln -s /Applications "$MOUNT_DIR/Applications"

# 复制应用
cp -R "dist/English-Learning-Assistant" "$MOUNT_DIR/$APP_NAME"

# 创建DMG
create-dmg \
    --volname "English Learning Assistant" \
    --volicon "assets/images/icon.icns" \
    --window-pos 200 120 \
    --window-size 600 400 \
    --icon-size 100 \
    --icon "$APP_NAME" 175 120 \
    --hide-extension "$APP_NAME" \
    --app-drop-link 425 120 \
    --no-internet-enable \
    "dist/$DMG_NAME" \
    "$MOUNT_DIR/"

# 清理临时文件
rm -rf "$TEMP_DIR"

echo "✅ DMG包创建成功: dist/$DMG_NAME"

# 显示文件信息
echo "📊 文件信息:"
ls -la "dist/$DMG_NAME"
echo "文件大小: $(du -h "dist/$DMG_NAME" | cut -f1)" 