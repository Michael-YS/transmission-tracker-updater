import logging

# Configuration settings for tracker list
TRACKER_LIST = [
    "tracker1.example.com",
    "tracker2.example.com",
]

# Connection setting
TRANSMISSION_RPC_HOST = "localhost"
TRANSMISSION_RPC_PORT = 9091
TRANSMISSION_RPC_PATH = "/transmission/rpc"
TRANSMISSION_RPC_USERNAME = ""
TRANSMISSION_RPC_PASSWORD = ""
TIMEOUT = 30.0  # seconds
USE_HTTPS = False

# Logging configuration
LOG_LEVEL = logging.INFO
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_FILE = "/var/log/myapp/app.log"