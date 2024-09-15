from os import getenv
from sys import stderr, stdout

from colorama import Fore, Style

from updatefy.datetime import now

DEBUG: bool = getenv("DEBUG", "0") == "1"


# Messages
def write_message(
    level: str, color: str, message: str, use_stderr: bool = False
) -> None:
    print(
        f"{Fore.BLACK}{now()} {Style.BRIGHT}{color}[{level}]{Style.RESET_ALL} {message}",
        file=(stderr if use_stderr else stdout),
    )


# Debug
def debug(message: str) -> None:
    if DEBUG:
        write_message("DEBUG", Fore.CYAN, message)


# Info
def info(message: str) -> None:
    write_message("INFO", Fore.GREEN, message)


# Warning
def warn(message: str) -> None:
    write_message("WARN", Fore.YELLOW, message, use_stderr=True)


# Error
def error(message: str) -> None:
    write_message("ERROR", Fore.RED, message, use_stderr=True)


# Fatal
def fatal(message: str, code: int = 1) -> None:
    error(message)
    exit(code)
