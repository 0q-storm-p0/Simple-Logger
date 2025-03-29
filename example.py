from logger import Logger

# Initialize the Logger with custom settings
logger = Logger(
    save=True,  # Enable saving logs to files
    set_date=True,  # Include date in log messages
    backup_location="./logs",  # Directory to save log files
    date_format="%YY-%MM-%DD",  # Custom date format
    time_format="%HH:%MM:%SS",  # Custom time format
    log_levels=("INFO", "WARNING", "ERROR", "DEBUG"),  # Custom log levels
    max_file_size=1024 * 10,  # Set max log file size to 10 KB for testing
    console_output=True,  # Enable console output
)

# Log an informational s
logger.log("This is an informational message.", level="INFO")

# Log a warning message
logger.log("This is a warning message.", level="WARNING")

# Log an error message
logger.log("This is an error message.", level="ERROR")

# Log a debug message
logger.log("This is a debug message for developers.", level="DEBUG")

# Simulate a large number of logs to test log rotation
for i in range(50):
    logger.log(f"Log entry #{i + 1}", level="INFO")

# Example of logging without saving to a file
logger.log("This message will not be saved to a file.", level="INFO", save=False)

# Example of logging with only console output
logger.console_output = False  # Disable console output
logger.log("This message will only be saved to a file.", level="INFO")

# Re-enable console output
logger.console_output = True
logger.log("Console output re-enabled.", level="INFO")
