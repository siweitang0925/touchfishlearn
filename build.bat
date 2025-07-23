@echo off
echo 正在编译英语学习助手...

REM 检查Python是否安装
python --version >nul 2>&1
if errorlevel 1 (
    echo 错误: 未找到Python，请先安装Python 3.8+
    pause
    exit /b 1
)

REM 检查PyInstaller是否安装
python -c "import PyInstaller" >nul 2>&1
if errorlevel 1 (
    echo 正在安装PyInstaller...
    pip install pyinstaller
)

REM 清理之前的构建
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist

REM 编译可执行文件
echo 正在打包程序...
pyinstaller --onefile --windowed --name "英语学习助手" main.py

if errorlevel 1 (
    echo 编译失败！
    pause
    exit /b 1
)

echo.
echo 编译成功！
echo 可执行文件位置: dist\英语学习助手.exe
echo.
pause 