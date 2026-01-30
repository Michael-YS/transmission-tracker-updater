# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-01-30

### Added
- Initial release
- Support for fetching tracker lists from multiple URL sources
- Batch update tracker lists for all active torrents
- Automatic torrent reannounce functionality
- Comprehensive logging system
- systemd timer support (Linux)
- Flexible configuration file system

### Features
- Support for Transmission RPC connections (HTTP/HTTPS)
- Automatic tracker list merge and deduplication
- Preserve existing trackers, only add new ones
- Configurable timeout and log levels
