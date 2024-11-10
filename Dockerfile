FROM python:3.11

# 设置环境变量
ENV PYTHONUNBUFFERED=1

# 设置工作目录
WORKDIR /app

# 复制依赖文件
COPY requirements.txt .

# 使用阿里云镜像源安装依赖
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

# 复制项目文件
COPY . .

# 运行命令
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

