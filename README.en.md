# Transmission Tracker Updater

A Python tool that automatically updates tracker lists for all active torrents in Transmission BT client.

## Features

- 🔄 Automatically fetch latest trackers from specified sources
- 📦 Batch update tracker lists for all active torrents
- 🔔 Automatically trigger torrent reannounce
- 📝 Comprehensive logging functionality
- ⚙️ Flexible configuration options

## Requirements

- Python 3.10 or higher
- Transmission BT client (with RPC enabled) (Running locally or remotely)

## Installation

1. Clone or download this project:
```bash
git clone <your-repo-url>
cd transmission-tracker-updater
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

Edit `config.py` according to your environment:

### Tracker List Sources
```python
TRACKER_LIST = [
    "https://example.com/trackers.txt",  # Tracker list URL
    "https://another.com/best-trackers.txt",
]
```

### Transmission RPC Connection Settings
```python
TRANSMISSION_RPC_HOST = "localhost"      # Transmission host address
TRANSMISSION_RPC_PORT = 9091            # RPC port (default 9091)
TRANSMISSION_RPC_PATH = "/transmission/rpc"  # RPC path
TRANSMISSION_RPC_USERNAME = "admin"     # RPC username (if authentication is enabled)
TRANSMISSION_RPC_PASSWORD = "password"  # RPC password
USE_HTTPS = False                       # Whether to use HTTPS
TIMEOUT = 30.0                          # Request timeout (seconds)
```

### Logging Configuration
```python
LOG_LEVEL = logging.INFO                # Log level
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_FILE = "/var/log/myapp/app.log"    # Log file path (Windows users need to modify path format)
```

## Usage

### Manual Execution

```bash
python main.py
```

### Scheduled Task (Linux)

Use systemd timer for scheduled execution:

1. Create symbolic links to systemd directory:
```bash
sudo ln -s $(pwd)/updateTracker.service /etc/systemd/system/
sudo ln -s $(pwd)/updateTracker.timer /etc/systemd/system/
```

2. Edit the service file and modify paths:
```bash
nano updateTracker.service
# Modify WorkingDirectory and ExecStart to your actual paths
```

3. Enable and start the timer:
```bash
sudo systemctl daemon-reload
sudo systemctl enable updateTracker.timer
sudo systemctl start updateTracker.timer
```

4. Check status:
```bash
sudo systemctl status updateTracker.timer
sudo systemctl list-timers
```

### Scheduled Task (Windows)

Use Task Scheduler:

1. Open "Task Scheduler"
2. Create Basic Task
3. Set trigger (e.g., run daily)
4. Action: "Start a program"
5. Program/script: `C:\Path\To\Your\venv\Scripts\python.exe`
6. Add arguments: `main.py`
7. Start in: `C:\Path\To\This\Project\transmission-tracker-updater`

## How It Works

1. **Fetch Tracker Lists**: Download latest tracker addresses from configured URLs
2. **Merge and Deduplicate**: Combine all fetched trackers and remove duplicates
3. **Get Active Torrents**: Retrieve recently active torrent list from Transmission
4. **Update Trackers**: Add new trackers to each torrent (keeping existing trackers)
5. **Reannounce**: Trigger torrents to reannounce to all trackers for faster connections

## FAQ

### Q: How to find Transmission RPC settings?
A: Check the "Remote" options in Transmission settings, ensure it's enabled and note the port and authentication info.

### Q: Where is the log file?
A: Default location is set in `config.py` via `LOG_FILE`. Windows users should modify it to something like `C:\\logs\\tracker_updater.log`.

### Q: What tracker list formats are supported?
A: Plain text format with one tracker URL per line.

### Q: Will it overwrite existing trackers?
A: No. The script preserves existing trackers and only adds new ones.

## Dependencies

- `requests` - HTTP request library
- `transmission-rpc` - Transmission RPC client

## License

This project is licensed under the MIT License.

## Contributing

Issues and Pull Requests are welcome!

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history and updates.
