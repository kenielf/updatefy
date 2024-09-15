from subprocess import run

from updatefy.log import error

NOTIFICATION_TIMEOUT: int = 30000
NOTIFICATION_ICON: str = r"pamac"
NOTIFICATION_COMMAND: str = "notify-send"


def send(
    title: str,
    body: str,
    timeout: int = NOTIFICATION_TIMEOUT,
    icon: str | None = NOTIFICATION_ICON,
):
    # Prepare command
    command: list[str]
    if icon:
        command = [
            NOTIFICATION_COMMAND,
            "-i",
            NOTIFICATION_ICON,
            "-t",
            str(timeout),
            title,
            body,
        ]
    else:
        command = [
            NOTIFICATION_COMMAND,
            "-t",
            str(timeout),
            title,
            body,
        ]

    # Send the notification
    if code := run(command).returncode != 0:
        error(f"Notifications: '{NOTIFICATION_COMMAND}' exited with code {code}")
