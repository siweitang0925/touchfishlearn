# 英语学习助手 - Mac版本完整说明

## 📁 Mac版本专用文件

### 编译相关文件
- `build_mac.spec` - Mac平台PyInstaller配置文件
- `build_mac.sh` - 完整编译脚本（包含详细检查）
- `build_mac_simple.sh` - 简化编译脚本（推荐使用）

### 运行相关文件
- `run_mac.sh` - Mac版本启动脚本
- `test_mac_compatibility.py` - Mac兼容性测试脚本

### 文档文件
- `README_Mac.md` - Mac版本详细说明文档

## 🚀 快速开始

### 1. 环境检查
```bash
# 运行兼容性测试
python3 test_mac_compatibility.py
```

### 2. 编译程序
```bash
# 使用简化脚本（推荐）
chmod +x build_mac_simple.sh
./build_mac_simple.sh
```

### 3. 运行程序
```bash
# 使用启动脚本（推荐）
chmod +x run_mac.sh
./run_mac.sh
```

## 🔧 编译配置说明

### build_mac.spec 特点
- 包含完整的依赖列表
- 自动打包assets目录
- 支持Intel和Apple Silicon
- 优化的隐藏导入配置

### 主要改进
1. **数据文件打包**: 自动包含`assets/data/ielts_1000_words.json`
2. **模块路径**: 包含整个`src`目录
3. **隐藏导入**: 预配置所有必要的模块
4. **跨架构支持**: 支持Intel和M1/M2芯片

## 🐛 常见问题解决

### 编译失败
```bash
# 清理缓存
rm -rf build dist __pycache__

# 重新安装依赖
pip3 install --upgrade pyinstaller pystray pillow

# 重新编译
./build_mac_simple.sh
```

### 权限问题
1. 在"系统偏好设置 > 安全性与隐私"中允许程序运行
2. 确保脚本有执行权限：`chmod +x *.sh`

### 系统托盘问题
- Mac版本的系统托盘显示在菜单栏顶部
- 某些Mac版本可能需要额外权限
- 建议使用右键菜单而不是单击

## 📋 功能对比

| 功能 | Windows | Mac | 说明 |
|------|---------|-----|------|
| 基础GUI | ✅ | ✅ | tkinter跨平台支持 |
| 系统托盘 | ✅ | ✅ | 菜单栏显示 |
| 弹窗测试 | ✅ | ✅ | 完全兼容 |
| 数据存储 | ✅ | ✅ | JSON文件存储 |
| 搜索功能 | ✅ | ✅ | 完全兼容 |
| 熟练度系统 | ✅ | ✅ | 完全兼容 |

## 🎯 使用建议

### 开发环境
- 推荐使用Python 3.7+
- 使用虚拟环境避免依赖冲突
- 定期运行兼容性测试

### 部署建议
- 编译前先运行测试脚本
- 在不同Mac版本上测试
- 提供详细的安装说明

### 用户体验
- 首次运行需要权限设置
- 系统托盘功能可能需要适应
- 建议提供多种启动方式

## 📞 技术支持

如遇到问题，请按以下顺序检查：

1. **运行兼容性测试**: `python3 test_mac_compatibility.py`
2. **检查Python版本**: `python3 --version`
3. **检查依赖安装**: `pip3 list | grep -E "(pyinstaller|pystray|pillow)"`
4. **查看错误日志**: 在终端中运行程序查看详细错误信息

## 🔄 更新日志

### v1.0.0 (Mac版本)
- ✅ 创建Mac专用编译配置
- ✅ 添加兼容性测试脚本
- ✅ 优化系统托盘功能
- ✅ 完善文档和说明
- ✅ 支持Intel和Apple Silicon 