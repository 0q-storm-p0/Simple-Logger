import datetime
import os
import threading
import platform


class Logger:
    DATE_PLACEHOLDERS = ("%YY", "%MM", "%DD")
    TIME_PLACEHOLDERS = ("%HH", "%MM", "%SS")
    DEFAULT_LOG_LEVELS = ("INFO", "WARNING", "ERROR")

    # ANSI escape codes for colors
    LOG_COLORS = {
        "INFO": "\033[37m",  # White
        "WARNING": "\033[33m",  # Yellow
        "ERROR": "\033[31m",  # Red
        "RESET": "\033[0m",  # Reset to default
    }

    def __init__(
        self,
        save: bool = True,
        set_date: bool = True,
        backup_location: str = "./",
        date_format: str = "%YY/%MM/%DD",
        time_format: str = "%HH:%MM:%SS",
        log_levels: tuple = DEFAULT_LOG_LEVELS,
        max_file_size: int = 1024 * 1024,  # 1 MB
        console_output: bool = True,
    ) -> None:
        self.save = save
        self.set_date = set_date
        self.backup_location = backup_location
        self.date_format = date_format
        self.time_format = time_format
        self.log_levels = log_levels
        self.max_file_size = max_file_size
        self.console_output = console_output
        self.lock = threading.Lock()

        # Check if the OS supports ANSI escape codes
        self.supports_colors = self._check_ansi_support()

        if not all(
            placeholder in date_format for placeholder in self.DATE_PLACEHOLDERS
        ):
            raise ValueError('Invalid date format! Example: "%YY/%MM/%DD"')
        if not all(
            placeholder in time_format for placeholder in self.TIME_PLACEHOLDERS
        ):
            raise ValueError('Invalid time format! Example: "%HH/%MM/%SS"')

    def log(self, message: str, level: str = "INFO", save: bool = None) -> None:
        if level not in self.log_levels:
            raise ValueError(
                f"Invalid log level: {level}. Allowed levels: {self.log_levels}"
            )

        save = self.save if save is None else save

        now = datetime.datetime.now()
        formatted_date = (
            self.date_format.replace("%YY", str(now.year).zfill(2))
            .replace("%MM", str(now.month).zfill(2))
            .replace("%DD", str(now.day).zfill(2))
        )
        formatted_time = (
            self.time_format.replace("%HH", str(now.hour).zfill(2))
            .replace("%MM", str(now.minute).zfill(2))
            .replace("%SS", str(now.second).zfill(2))
        )

        log_message = (
            f"[{level}] [ {formatted_date} - {formatted_time} ] {message}"
            if self.set_date
            else f"[{level}] [ {formatted_time} ] {message}"
        )

        if save:
            self._save_log(log_message, now)

        if self.console_output:
            self._print_colored(log_message, level)

    def _print_colored(self, log_message: str, level: str) -> None:
        """Prints the log message with the appropriate color."""
        if self.supports_colors:
            color = self.LOG_COLORS.get(
                level, self.LOG_COLORS["RESET"]
            )  # Default to reset
            print(f"{color}{log_message}{self.LOG_COLORS['RESET']}")
        else:
            print(log_message)  # Fallback to plain text if colors are not supported

    def _save_log(self, log_message: str, now: datetime.datetime) -> None:
        bk_path = os.path.join(
            self.backup_location,
            "Logs",
            str(now.year).zfill(2),
            str(now.month).zfill(2),
            str(now.day).zfill(2),
        )
        os.makedirs(bk_path, exist_ok=True)

        log_file_path = os.path.join(bk_path, f"{str(now.hour).zfill(2)}h.txt")

        with self.lock:  # Ensure thread-safe logging
            if (
                os.path.exists(log_file_path)
                and os.path.getsize(log_file_path) > self.max_file_size
            ):
                self._rotate_log(log_file_path)

            try:
                with open(log_file_path, mode="a") as log_file:
                    log_file.write(log_message + "\n")
            except IOError as e:
                print(f"Failed to write to log file {log_file_path}: {e}")

    def _rotate_log(self, log_file_path: str) -> None:
        base, ext = os.path.splitext(log_file_path)
        rotated_file_path = f"{base}_backup{ext}"
        os.rename(log_file_path, rotated_file_path)

    def _check_ansi_support(self) -> bool:
        """Checks if the current OS and terminal support ANSI escape codes."""
        if platform.system() == "Windows":
            return os.getenv("ANSICON") is not None or "WT_SESSION" in os.environ
        return True  # Assume ANSI support for non-Windows systems
