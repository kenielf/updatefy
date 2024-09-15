from shutil import which
from typing import NoReturn

from updatefy.log import debug, error, fatal

DEPENDENCIES: dict[str, str] = {
    "checkupdates": "pacman-contrib",
    "notify-send": "libnotify",
}


def check_dependencies() -> None | NoReturn:
    missing: bool = False

    for command, package in DEPENDENCIES.items():
        if not which(command):
            error(f"Dependencies: '{command}' from package '{package}' was not found!")
            missing = True
        else:
            debug(f"Dependencies: '{command}' found!")

    if missing:
        fatal("Dependencies: There are essential commands missing, exiting!")
