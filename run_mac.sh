#!/bin/bash

echo "🚀 启动英语学习助手 (Mac版本)"
echo "================================"

# 检查可执行文件是否存在
if [ -f "dist/英语学习助手" ]; then
    echo "✅ 找到可执行文件"
    echo "🎯 启动程序..."
    ./dist/英语学习助手
elif [ -f "main.py" ]; then
    echo "⚠️  未找到编译版本，使用Python脚本运行"
    echo "💡 建议先运行 ./build_mac_simple.sh 编译程序"
    echo ""
    echo "🎯 启动Python脚本..."
    python3 main.py
else
    echo "❌ 错误: 未找到可执行文件或main.py"
    echo "请确保在正确的目录中运行此脚本"
    exit 1
fi 