# Logger Module 📝

A lightweight, thread-safe logging utility with file rotation and colored console output.

## Features ✨

- **Custom Log Levels**: INFO, WARNING, ERROR, DEBUG (configurable)
- **Colorful Console**: ANSI-colored output (auto-detects terminal support)
- **File Logging**: Automatically saves logs with date-based organization
- **Log Rotation**: Handles large files with automatic rotation
- **Thread-Safe**: Built with threading.Lock for concurrent usage
- **Custom Formats**: Flexible date/time formatting in logs

## Quick Start 🚀

```python
from logger import Logger

# Initialize logger
logger = Logger(
    save=True,
    set_date=True,
    backup_location="./logs",
    date_format="%YY-%MM-%DD",
    time_format="%HH:%MM:%SS",
    log_levels=("INFO", "WARNING", "ERROR", "DEBUG"),
    max_file_size=1024 * 10,  # 10KB
    console_output=True
)

# Usage examples
logger.log("System initialized", level="INFO")
logger.log("Low disk space", level="WARNING")
logger.log("Connection failed", level="ERROR")
logger.log("Variable value: 42", level="DEBUG")
```

## Configuration Options ⚙️

| Parameter         | Default                        | Description                     |
| ----------------- | ------------------------------ | ------------------------------- |
| `save`            | `True`                         | Enable file logging             |
| `set_date`        | `True`                         | Include date in log messages    |
| `backup_location` | `./`                           | Base directory for log files    |
| `date_format`     | `"%YY/%MM/%DD"`                | Custom date format              |
| `time_format`     | `"%HH:%MM:%SS"`                | Custom time format              |
| `log_levels`      | `("INFO", "WARNING", "ERROR")` | Enabled log levels              |
| `max_file_size`   | `1MB`                          | Size threshold for log rotation |
| `console_output`  | `True`                         | Print logs to console           |

## File Structure 📂

Logs are automatically organized by date:

logs/
├── Logs/
│   ├── 23/          # Year
│   │   ├── 12/      # Month
│   │   │   ├── 25/  # Day
│   │   │   │   ├── 14h.txt
│   │   │   │   └── 14h_backup.txt  # Rotated file

## Requirements 📦

- Python 3.6+
- No external dependencies

## License 📜

MIT License - Free for personal and commercial use
