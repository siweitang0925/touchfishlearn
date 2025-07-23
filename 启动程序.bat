@echo off
echo 正在启动英语学习助手...
echo.

REM 检查是否存在编译后的exe文件
if exist "dist\英语学习助手.exe" (
    echo 找到可执行文件，正在启动...
    start "" "dist\英语学习助手.exe"
) else (
    echo 未找到可执行文件，尝试运行Python版本...
    python main.py
)

echo.
echo 程序已启动！
pause 