from datetime import datetime
from json import dumps, loads
from pathlib import Path
from subprocess import run

from updatefy.datetime import DATETIME_FMT, now
from updatefy.log import debug, fatal, info
from updatefy.notifications import send

MARKER: Path = Path.home() / ".local" / "state" / "updatefy.json"
MARKER.parent.mkdir(parents=True, exist_ok=True)
UPDATE_COMMAND: list[str] = ["checkupdates"]
UPDATE_DAYS: int = 3


def get_update_history() -> list[str]:
    with open(MARKER, "r") as file:
        return loads(file.read())["history"]


# Returns the last update's timestamp
def get_last_updated() -> datetime | None:
    # If updates have never been checked
    if not MARKER.exists():
        return None

    # Check updates
    updates = get_update_history()
    return datetime.strptime(updates[-1], DATETIME_FMT)


# Adds the current timestamp to the update history
def mark_checked() -> None:
    history: list[str] = []

    # If there are previous updates
    if MARKER.exists():
        history = get_update_history()

    # Add this check to the list
    with open(MARKER, "w") as file:
        # Otherwise, just append to the update list
        history.append(str(now()))
        file.write(dumps({"history": history}))


def check_updates() -> None:
    debug("Checking for updates...")
    output = run(UPDATE_COMMAND, capture_output=True, text=True)
    # There are updates
    if output.returncode == 0:
        packages = output.stdout.splitlines()
        info(f"Updates: {len(packages)} packages waiting for update, notifying...")
        send(
            title=f"Updatefy: {len(packages)} update(s)",
            body="\n".join(
                [
                    f"<b>{item[0]}</b> ({item[-1]})"
                    for item in (line.split() for line in packages)
                ]
            ),
        )
        mark_checked()
    # No updates
    elif output.returncode == 2:
        info("Updates: no updates available!")
        send(title="Updatefy: No updates", body="Packages are up to date!")
        mark_checked()
    # Error
    else:
        fatal(f"Updates: '{UPDATE_COMMAND[0]}' exited with code {output.returncode}!")
