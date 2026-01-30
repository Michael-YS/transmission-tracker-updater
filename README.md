# Transmission Tracker Updater

一个自动更新 Transmission BT 客户端中所有活跃种子 tracker 列表的 Python 工具。

## 功能特性

- 🔄 自动从指定的 tracker 列表源获取最新 tracker
- 📦 批量更新所有活跃种子的 tracker 列表
- 🔔 自动触发种子重新宣告（reannounce）
- 📝 完整的日志记录功能
- ⚙️ 灵活的配置选项

## 系统要求

- Python 3.10 或更高版本
- Transmission BT 客户端（支持 RPC）（本地或远程运行）

## 安装步骤

1. 克隆或下载本项目：
```bash
git clone <your-repo-url>
cd transmission-tracker-updater
```

2. 创建虚拟环境（推荐）：
```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. 安装依赖：
```bash
pip install -r requirements.txt
```

## 配置说明

编辑 `config.py` 文件，根据你的环境进行配置：

### Tracker 列表源
```python
TRACKER_LIST = [
    "https://example.com/trackers.txt",  # tracker 列表 URL
    "https://another.com/best-trackers.txt",
]
```

### Transmission RPC 连接设置
```python
TRANSMISSION_RPC_HOST = "localhost"      # Transmission 主机地址
TRANSMISSION_RPC_PORT = 9091            # RPC 端口（默认 9091）
TRANSMISSION_RPC_PATH = "/transmission/rpc"  # RPC 路径
TRANSMISSION_RPC_USERNAME = "admin"     # RPC 用户名（如果启用了认证）
TRANSMISSION_RPC_PASSWORD = "password"  # RPC 密码
USE_HTTPS = False                       # 是否使用 HTTPS
TIMEOUT = 30.0                          # 请求超时时间（秒）
```

### 日志配置
```python
LOG_LEVEL = logging.INFO                # 日志级别
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_FILE = "/var/log/myapp/app.log"    # 日志文件路径（Windows 需修改路径格式）
```

## 使用方法

### 手动运行

```bash
python main.py
```

### 定时任务（Linux）

使用 systemd timer 实现定时运行：

1. 创建符号链接到 systemd 目录：
```bash
sudo ln -s $(pwd)/updateTracker.service /etc/systemd/system/
sudo ln -s $(pwd)/updateTracker.timer /etc/systemd/system/
```

2. 编辑服务文件，修改路径：
```bash
nano updateTracker.service
# 修改 WorkingDirectory 和 ExecStart 为你的实际路径
```

3. 启用并启动定时器：
```bash
sudo systemctl daemon-reload
sudo systemctl enable updateTracker.timer
sudo systemctl start updateTracker.timer
```

4. 检查状态：
```bash
sudo systemctl status updateTracker.timer
sudo systemctl list-timers
```

### 定时任务（Windows）

使用任务计划程序：

1. 打开"任务计划程序"
2. 创建基本任务
3. 设置触发器（如每天运行）
4. 操作选择"启动程序"
5. 程序/脚本：`C:\Path\To\Your\venv\Scripts\python.exe`
6. 添加参数：`main.py`
7. 起始于：`C:\Path\To\This\Project\transmission-tracker-updater`

## 工作原理

1. **获取 Tracker 列表**：从配置的 URL 列表中下载最新的 tracker 地址
2. **合并去重**：将所有获取的 tracker 合并并去除重复项
3. **获取活跃种子**：从 Transmission 中获取最近活跃的种子列表
4. **更新 Tracker**：为每个种子添加新的 tracker（保留原有 tracker）
5. **重新宣告**：触发种子向所有 tracker 重新宣告，加速连接

## 常见问题

### Q: 如何找到 Transmission 的 RPC 设置？
A: 在 Transmission 设置中查看"远程控制"选项，确保已启用并记下端口号和认证信息。

### Q: 日志文件在哪里？
A: 默认位置在 `config.py` 的 `LOG_FILE` 设置中。Windows 用户建议修改为类似 `C:\\logs\\tracker_updater.log` 的路径。

### Q: 支持哪些 tracker 列表格式？
A: 支持纯文本格式，每行一个 tracker URL。

### Q: 会覆盖现有的 tracker 吗？
A: 不会。脚本会保留现有 tracker，只添加新的 tracker。

## 依赖项

- `requests` - HTTP 请求库
- `transmission-rpc` - Transmission RPC 客户端

## 许可证

本项目遵循 MIT 许可证。

## 贡献

欢迎提交 Issue 和 Pull Request！

## 更新日志

详见 [CHANGELOG.md](CHANGELOG.md)。