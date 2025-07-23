@echo off
echo ========================================
echo 英语学习助手 - Windows编译Mac版本
echo ========================================

echo.
echo 检查Docker是否安装...
docker --version >nul 2>&1
if errorlevel 1 (
    echo ❌ 错误: 未找到Docker
    echo 请先安装Docker Desktop: https://www.docker.com/products/docker-desktop/
    pause
    exit /b 1
)

echo ✅ Docker已安装

echo.
echo 构建Docker镜像...
docker build -t learnenglish-mac-builder .

if errorlevel 1 (
    echo ❌ Docker镜像构建失败
    pause
    exit /b 1
)

echo ✅ Docker镜像构建成功

echo.
echo 开始编译Mac版本...
docker run --rm -v "%cd%":/app learnenglish-mac-builder

if errorlevel 1 (
    echo ❌ 编译失败
    pause
    exit /b 1
)

echo.
echo ✅ Mac版本编译成功！
echo 📁 可执行文件位置: dist/英语学习助手
echo.
echo 注意: 这个文件需要在Mac系统上运行
echo 可以将整个dist目录复制到Mac电脑上使用

pause 