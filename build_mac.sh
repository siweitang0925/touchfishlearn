#!/bin/bash

# Mac版本编译脚本
echo "开始编译Mac版本的英语学习助手..."

# 检查Python是否安装
if ! command -v python3 &> /dev/null; then
    echo "错误: 未找到Python3，请先安装Python3"
    exit 1
fi

# 检查PyInstaller是否安装
if ! python3 -c "import PyInstaller" &> /dev/null; then
    echo "安装PyInstaller..."
    pip3 install pyinstaller
fi

# 检查必要的依赖
echo "检查依赖..."
pip3 install pystray pillow

# 清理之前的构建
echo "清理之前的构建文件..."
rm -rf build dist

# 编译Mac版本
echo "开始编译..."
python3 -m PyInstaller build_mac.spec

# 检查编译结果
if [ -f "dist/英语学习助手" ]; then
    echo "编译成功！"
    echo "可执行文件位置: dist/英语学习助手"
    echo ""
    echo "使用说明:"
    echo "1. 双击运行 dist/英语学习助手"
    echo "2. 或者在终端中运行: ./dist/英语学习助手"
    echo ""
    echo "注意: 首次运行时可能需要授予权限"
else
    echo "编译失败，请检查错误信息"
    exit 1
fi 