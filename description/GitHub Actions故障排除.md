# GitHub Actions 故障排除指南

## 🔧 常见问题及解决方案

### 1. actions/upload-artifact@v3 弃用错误

**错误信息**:
```
Error: This request has been automatically failed because it uses a deprecated version of `actions/upload-artifact: v3`.
```

**解决方案**:
- 将 `actions/upload-artifact@v3` 升级到 `actions/upload-artifact@v4`
- 已在 `.github/workflows/build.yml` 中修复

### 2. Windows PowerShell 语法错误

**错误信息**:
```
ParserError: Missing '(' after 'if' in if statement.
Error: Process completed with exit code 1.
```

**原因**:
- Windows环境使用PowerShell，而配置中使用了bash语法
- `if [ "$RUNNER_OS" = "Windows" ]` 是bash语法，在PowerShell中无效

**解决方案**:
- 为不同平台使用正确的shell语法
- Windows: 使用PowerShell语法 (`if: runner.os == 'Windows'`)
- macOS/Linux: 使用bash语法 (`if: runner.os == 'macOS'`)
- 明确指定shell类型: `shell: powershell` 或 `shell: bash`

### 2. PyInstaller 构建失败

**可能原因**:
- 缺少依赖包
- 模块导入错误
- 平台兼容性问题

**解决方案**:
```bash
# 确保安装所有依赖
pip install pyinstaller pystray pillow

# 检查模块导入
python -c "import tkinter; print('Tkinter OK')"
python -c "import pystray; print('Pystray OK')"
python -c "from PIL import Image; print('Pillow OK')"
```

### 3. 跨平台构建问题

#### Windows 构建问题
- 确保使用 `--windowed` 参数
- 检查系统托盘权限

#### macOS 构建问题
- 需要 `build_mac.spec` 文件
- 检查代码签名和权限

#### Linux 构建问题
- 确保有图形界面支持
- 检查系统托盘依赖

### 4. 依赖缓存问题

**解决方案**:
```yaml
- name: Cache pip dependencies
  uses: actions/cache@v4
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
    restore-keys: |
      ${{ runner.os }}-pip-
```

### 5. 文件路径问题

**常见错误**:
- 找不到 `main.py`
- 找不到 `build_mac.spec`
- 找不到 `dist/` 目录

**解决方案**:
```bash
# 检查文件结构
ls -la
find . -name "*.py" -type f
find . -name "*.spec" -type f
```

## 🚀 优化建议

### 1. 构建性能优化

```yaml
# 使用缓存
- name: Cache pip dependencies
  uses: actions/cache@v4

# 并行构建
strategy:
  matrix:
    os: [windows-latest, macos-latest, ubuntu-latest]
```

### 2. 错误处理

```yaml
# 添加条件检查
- name: Check build artifacts
  run: |
    if [ ! -d "dist" ]; then
      echo "Build failed: dist directory not found"
      exit 1
    fi

# 设置超时
timeout-minutes: 30
```

### 3. 调试信息

```yaml
# 显示详细日志
- name: Show debug info
  run: |
    echo "Python version:"
    python --version
    echo "Installed packages:"
    pip list
    echo "Current directory:"
    pwd
    ls -la
```

## 📋 检查清单

### 构建前检查
- [ ] 所有依赖已添加到 `requirements.txt`
- [ ] 代码能正常运行 (`python main.py`)
- [ ] 所有导入路径正确
- [ ] 文件结构完整

### 构建后检查
- [ ] 生成的可执行文件存在
- [ ] 文件大小合理
- [ ] 没有缺失的依赖
- [ ] 功能测试通过

## 🔍 调试步骤

### 1. 本地测试
```bash
# 安装依赖
pip install -r requirements.txt

# 测试运行
python main.py

# 测试构建
pyinstaller --onefile main.py
```

### 2. 检查日志
- 查看 GitHub Actions 的详细日志
- 检查构建步骤的输出
- 查看错误堆栈信息

### 3. 逐步调试
- 先在一个平台上测试
- 逐步添加其他平台
- 逐个解决平台特定问题

## 📞 获取帮助

### 1. 查看文档
- [GitHub Actions 文档](https://docs.github.com/en/actions)
- [PyInstaller 文档](https://pyinstaller.org/en/stable/)
- [项目 README](README.md)

### 2. 常见资源
- GitHub Issues
- Stack Overflow
- 项目 Wiki

### 3. 联系维护者
- 创建 Issue
- 提供详细的错误信息
- 包含复现步骤

## 🎯 最佳实践

### 1. 版本管理
- 使用语义化版本号
- 锁定依赖版本
- 定期更新依赖

### 2. 测试策略
- 本地测试
- 多平台测试
- 自动化测试

### 3. 文档维护
- 更新 README
- 记录变更日志
- 维护故障排除指南

## 📊 监控指标

### 构建指标
- 构建成功率
- 构建时间
- 文件大小变化

### 质量指标
- 代码覆盖率
- 测试通过率
- 用户反馈

### 性能指标
- 启动时间
- 内存使用
- CPU 使用率 