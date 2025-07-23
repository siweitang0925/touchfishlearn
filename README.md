# LearnEnglish - 英语学习助手

一个专为"摸鱼学习"设计的英语单词学习桌面应用程序，具有强制学习功能。

## 功能特性

- 📚 生词本管理（添加、编辑、删除单词）
- 🎯 强制学习模式（每10分钟弹出测试）
- 🚫 无关闭按钮（必须答对才能关闭）
- 📖 例句支持
- 📊 学习进度跟踪
- 💾 数据持久化存储
- 🔍 搜索功能
- ⏰ 学习间隔设置
- ⭐ 熟练度系统
- 🖥️ 系统托盘支持
- 📝 内置雅思词汇

## 技术栈

- **Python 3.7+** - 主要编程语言
- **tkinter** - GUI框架
- **PyInstaller** - 打包工具
- **pystray** - 系统托盘支持
- **Pillow** - 图像处理
- **JSON** - 数据存储

## 快速开始

### Windows版本

1. **运行程序**
   ```bash
   # 方式1: 直接运行Python脚本
   python main.py
   
   # 方式2: 运行编译后的exe文件
   dist\英语学习助手.exe
   
   # 方式3: 使用批处理文件
   启动程序.bat
   ```

2. **编译exe文件**
   ```bash
   python -m PyInstaller --onefile --windowed --name "英语学习助手" main.py
   ```

### Mac版本

#### 在Mac上编译
1. **安装依赖**
   ```bash
   pip3 install pyinstaller pystray pillow
   ```

2. **编译Mac版本**
   ```bash
   # 方式1: 使用编译脚本
   chmod +x build_mac_simple.sh
   ./build_mac_simple.sh
   
   # 方式2: 手动编译
   python3 -m PyInstaller build_mac.spec
   ```

3. **运行程序**
   ```bash
   # 在终端中运行
   ./dist/英语学习助手
   
   # 或者双击运行
   open dist/英语学习助手
   ```

#### 在Windows上编译Mac版本
由于PyInstaller只能为当前平台生成可执行文件，在Windows上编译Mac版本需要使用特殊方法：

**方案1: 使用Docker（推荐）**
```bash
# 安装Docker Desktop后运行
build_mac_docker.bat

# 或使用PowerShell脚本
powershell -ExecutionPolicy Bypass -File build_mac_windows.ps1
```

**方案2: 使用GitHub Actions（推荐）**
- 将代码推送到GitHub仓库
- 自动触发多平台编译（Windows、macOS、Linux）
- 在Actions页面下载编译好的可执行文件
- 支持自动缓存和错误处理
- 如果遇到构建问题，请查看[故障排除指南](GitHub Actions故障排除.md)

**方案3: 使用虚拟机**
- 在Windows上安装macOS虚拟机
- 在虚拟机中编译程序

详细说明请参考：
- [README_Mac.md](README_Mac.md) - Mac版本详细说明
- [虚拟机编译指南.md](虚拟机编译指南.md) - Windows编译Mac版本指南

## 项目结构

```
learnEnglish/
├── main.py                    # 主程序入口
├── src/                       # 源代码目录
│   ├── gui/                  # GUI相关代码
│   │   ├── main_window.py    # 主窗口
│   │   └── study_popup.py    # 学习弹窗
│   └── data/                 # 数据相关代码
│       └── word_model.py     # 单词数据模型
├── assets/                   # 资源文件
│   └── data/                # 数据文件
│       └── ielts_1000_words.json
├── build_mac.spec           # Mac编译配置
├── build_mac.sh             # Mac编译脚本
├── build_mac_simple.sh      # 简化Mac编译脚本
├── run_mac.sh               # Mac启动脚本
├── build_mac_docker.bat     # Windows Docker编译脚本
├── build_mac_windows.ps1    # Windows PowerShell编译脚本
├── Dockerfile               # Docker配置文件
├── .github/workflows/build.yml # GitHub Actions工作流
├── tests/                    # 测试套件目录
│   ├── README.md            # 测试说明文档
│   ├── run_tests.py         # 测试套件入口
│   ├── 功能测试/            # 核心功能测试
│   ├── GitHub Actions测试/  # CI/CD相关测试
│   ├── 演示脚本/            # 功能演示脚本
│   ├── 兼容性测试/          # 跨平台兼容性测试
│   └── 构建测试/            # 构建相关测试
├── description/              # 项目文档目录
│   ├── README.md            # 文档说明
│   ├── 功能开发文档/        # 开发过程总结
│   ├── 功能说明文档/        # 功能使用说明
│   └── 构建部署文档/        # 构建部署指南
├── test_mac_compatibility.py   # Mac兼容性测试
```

## 使用说明

1. **添加单词**: 在输入框中输入单词、中文含义和例句，点击"添加单词"
2. **搜索单词**: 在搜索框中输入关键词，支持单词、含义、例句搜索
3. **开始学习**: 设置学习间隔，点击"开始摸鱼学习"
4. **系统托盘**: 学习开始后程序会最小化到系统托盘
5. **弹窗测试**: 定时弹出单词测试，必须答对才能关闭

## 数据文件

- `words.json` - 单词数据文件
- `settings.json` - 设置文件
- `assets/data/ielts_1000_words.json` - 内置雅思词汇

## 开发说明

### 环境设置
```bash
pip install -r requirements.txt
```

### 运行测试
```bash
# 运行所有测试
python tests/run_tests.py all

# 运行特定类别测试
python tests/run_tests.py category 功能测试
python tests/run_tests.py category GitHub Actions测试
python tests/run_tests.py category 演示脚本

# 运行单个测试
python tests/run_tests.py test_app.py

# 交互模式
python tests/run_tests.py

# 查看所有测试
python tests/run_tests.py list
```

### 代码规范
- 使用中文注释
- 遵循PEP 8编码规范
- 添加必要的错误处理

## 常见问题

### Windows版本
- **exe文件无法运行**: 检查是否被杀毒软件拦截
- **模块导入错误**: 确保所有依赖已正确安装

### Mac版本
- **权限问题**: 在"系统偏好设置"中允许程序运行
- **系统托盘**: 检查菜单栏权限设置
- **编译失败**: 确保Python版本为3.7+

## 更新日志

### v1.0.0
- ✅ 基础生词本功能
- ✅ 强制学习模式
- ✅ 系统托盘支持
- ✅ 熟练度系统
- ✅ 搜索功能
- ✅ 跨平台支持

## 许可证

本项目采用MIT许可证。 # touchfishlearn
