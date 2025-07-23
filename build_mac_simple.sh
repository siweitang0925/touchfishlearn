#!/bin/bash

echo "🐍 英语学习助手 - Mac版本编译"
echo "================================"

# 检查Python
if ! command -v python3 &> /dev/null; then
    echo "❌ 错误: 未找到Python3"
    echo "请先安装Python3: https://www.python.org/downloads/"
    exit 1
fi

echo "✅ Python3 已安装: $(python3 --version)"

# 安装依赖
echo "📦 安装依赖包..."
pip3 install pyinstaller pystray pillow

# 清理旧文件
echo "🧹 清理旧文件..."
rm -rf build dist __pycache__

# 编译
echo "🔨 开始编译..."
python3 -m PyInstaller build_mac.spec

# 检查结果
if [ -f "dist/英语学习助手" ]; then
    echo ""
    echo "🎉 编译成功！"
    echo "📁 可执行文件: dist/英语学习助手"
    echo ""
    echo "🚀 运行方式:"
    echo "   1. 双击运行: open dist/英语学习助手"
    echo "   2. 终端运行: ./dist/英语学习助手"
    echo ""
    echo "⚠️  注意: 首次运行可能需要在'系统偏好设置 > 安全性与隐私'中允许运行"
else
    echo "❌ 编译失败"
    exit 1
fi 