# 测试套件说明

本目录包含英语学习助手项目的所有测试和演示脚本。

## 📁 目录结构

```
tests/
├── README.md                    # 本说明文件
├── run_tests.py                 # 测试套件入口文件
├── 功能测试/                    # 核心功能测试
├── GitHub Actions测试/          # CI/CD相关测试
├── 演示脚本/                    # 功能演示脚本
├── 兼容性测试/                  # 跨平台兼容性测试
└── 构建测试/                    # 构建相关测试
```

## 🚀 快速开始

### 运行所有测试
```bash
python tests/run_tests.py all
```

### 运行特定类别测试
```bash
# 功能测试
python tests/run_tests.py category 功能测试

# GitHub Actions测试
python tests/run_tests.py category GitHub Actions测试

# 演示脚本
python tests/run_tests.py category 演示脚本
```

### 运行单个测试
```bash
python tests/run_tests.py test_encoding_fix.py
```

### 交互模式
```bash
python tests/run_tests.py
```

### 列出所有测试
```bash
python tests/run_tests.py list
```

## 📋 测试分类

### 功能测试
- `test_app.py` - 应用程序基本功能测试
- `test_proficiency.py` - 熟练度系统测试
- `test_popup_*.py` - 弹框功能测试
- `test_tray_*.py` - 系统托盘功能测试
- `test_minimize.py` - 最小化功能测试
- `test_new_features.py` - 新功能测试
- `test_three_states.py` - 三种状态测试
- `test_daily_correct.py` - 每日正确率测试
- `test_ielts_data.py` - IELTS数据测试
- `test_transparent_popup.py` - 透明弹框测试

### GitHub Actions测试
- `test_github_actions.py` - GitHub Actions配置测试
- `test_github_actions_fix.py` - GitHub Actions修复验证
- `check_build_status.py` - 构建状态检查
- `verify_github_actions_fix.py` - GitHub Actions修复验证

### 演示脚本
- `完整功能演示.py` - 完整功能演示
- `完整功能演示_v*.py` - 各版本功能演示
- `功能演示.py` - 基础功能演示
- `demo_features.py` - 特性演示

### 兼容性测试
- `test_mac_compatibility.py` - Mac兼容性测试

### 构建测试
- `test_encoding_fix.py` - 编码修复测试
- `final_test.py` - 最终测试

## 🧪 测试说明

### 功能测试
测试应用程序的核心功能，包括：
- 单词管理
- 学习模式
- 弹框功能
- 系统托盘
- 数据持久化

### GitHub Actions测试
验证CI/CD配置的正确性：
- 构建配置
- 跨平台支持
- 编码设置
- 依赖管理

### 演示脚本
展示应用程序的各种功能：
- 基本操作演示
- 高级功能展示
- 用户界面演示

### 兼容性测试
确保应用程序在不同平台上的兼容性：
- Windows兼容性
- macOS兼容性
- Linux兼容性

### 构建测试
验证构建过程的正确性：
- 编码问题
- 依赖问题
- 打包问题

## 🔧 添加新测试

### 1. 创建测试文件
在tests目录下创建新的测试文件，命名规范：
- 功能测试：`test_功能名称.py`
- 演示脚本：`演示_功能名称.py`
- 兼容性测试：`test_平台_功能.py`

### 2. 测试文件结构
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试描述
"""

import sys
import os

# 添加项目根目录到Python路径
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

def test_function():
    """测试函数"""
    # 测试代码
    pass

def main():
    """主函数"""
    # 运行测试
    pass

if __name__ == "__main__":
    main()
```

### 3. 更新分类
如果需要新的测试类别，请修改`run_tests.py`中的`categorize_tests()`函数。

## 📊 测试结果

### 成功标准
- 所有功能测试通过
- 无错误或异常
- 输出符合预期

### 失败处理
- 检查错误信息
- 验证依赖是否正确安装
- 确认环境配置

## 🛠️ 故障排除

### 常见问题

1. **导入错误**
   - 确保项目根目录在Python路径中
   - 检查模块是否存在

2. **依赖缺失**
   - 安装所需依赖：`pip install -r requirements.txt`
   - 检查版本兼容性

3. **权限问题**
   - 确保有足够的文件系统权限
   - 检查网络连接（如果需要）

4. **编码问题**
   - 确保文件使用UTF-8编码
   - 检查环境变量设置

### 调试技巧

1. **单独运行测试**
   ```bash
   python tests/test_file.py
   ```

2. **查看详细输出**
   ```bash
   python -v tests/test_file.py
   ```

3. **使用调试器**
   ```bash
   python -m pdb tests/test_file.py
   ```

## 📝 维护说明

### 定期维护
- 更新测试用例
- 检查测试覆盖率
- 优化测试性能

### 版本控制
- 测试文件应随代码一起提交
- 保持测试与功能同步
- 记录测试变更

## 🤝 贡献指南

1. 添加新功能时，同时添加相应的测试
2. 修复bug时，添加回归测试
3. 保持测试代码的简洁和可读性
4. 遵循项目的编码规范

## 📞 获取帮助

如果遇到测试问题，请：
1. 查看错误信息
2. 检查本文档
3. 查看项目主README
4. 创建Issue描述问题 