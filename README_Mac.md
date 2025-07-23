# 英语学习助手 - Mac版本

## 编译说明

### 环境要求
- macOS 10.14 或更高版本
- Python 3.7 或更高版本
- pip3

### 编译步骤

1. **快速编译（推荐）**
   ```bash
   chmod +x build_mac_simple.sh
   ./build_mac_simple.sh
   ```

2. **完整编译**
   ```bash
   chmod +x build_mac.sh
   ./build_mac.sh
   ```

3. **手动编译**
   ```bash
   # 安装依赖
   pip3 install pyinstaller pystray pillow
   
   # 编译
   python3 -m PyInstaller build_mac.spec
   ```

4. **兼容性测试**
   ```bash
   python3 test_mac_compatibility.py
   ```

### 运行程序

编译完成后，可执行文件位于 `dist/英语学习助手`

```bash
# 方式1: 使用启动脚本（推荐）
chmod +x run_mac.sh
./run_mac.sh

# 方式2: 在终端中运行
./dist/英语学习助手

# 方式3: 双击运行
open dist/英语学习助手

# 方式4: 直接运行Python脚本
python3 main.py
```

## Mac特有注意事项

### 1. 权限设置
首次运行时，macOS可能会阻止程序运行。解决方法：
- 打开"系统偏好设置" > "安全性与隐私"
- 点击"仍要打开"允许程序运行

### 2. 系统托盘功能
Mac版本的系统托盘功能可能与其他平台略有不同：
- 托盘图标会显示在菜单栏顶部
- 右键点击托盘图标显示菜单
- 某些Mac版本可能需要额外的权限

### 3. 文件路径
程序会自动在用户目录下创建数据文件：
- `~/words.json` - 单词数据
- `~/settings.json` - 设置文件

### 4. 兼容性
- 支持 Intel 和 Apple Silicon (M1/M2) Mac
- 建议使用 macOS 10.14 或更高版本

## 故障排除

### 编译失败
1. 确保Python版本正确：`python3 --version`
2. 重新安装依赖：`pip3 install --upgrade pyinstaller pystray pillow`
3. 清理缓存：`rm -rf build dist __pycache__`

### 运行失败
1. 检查权限设置
2. 在终端中运行查看错误信息
3. 确保数据文件路径可写

### 系统托盘不工作
1. 检查菜单栏权限
2. 尝试重启程序
3. 某些Mac版本可能需要手动启用菜单栏图标

## 功能特性

✅ 生词本管理（添加、编辑、删除单词）
✅ 强制学习模式（定时弹出测试）
✅ 无关闭按钮（必须答对才能关闭）
✅ 例句支持
✅ 学习进度跟踪
✅ 数据持久化存储
✅ 搜索功能
✅ 学习间隔设置
✅ 熟练度系统
✅ 系统托盘支持
✅ 内置雅思词汇

## 技术支持

如遇到问题，请检查：
1. Python版本是否为3.7+
2. 是否安装了所有依赖
3. 系统权限设置
4. 终端错误信息 