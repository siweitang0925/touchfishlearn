# 使用Python 3.11的官方镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    git \
    wget \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 复制项目文件
COPY . /app/

# 安装Python依赖
RUN pip install --no-cache-dir pyinstaller pystray pillow

# 设置环境变量
ENV PYTHONPATH=/app/src

# 编译Mac版本
CMD ["python", "-m", "PyInstaller", "build_mac.spec"] 