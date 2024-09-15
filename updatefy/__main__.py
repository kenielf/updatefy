from datetime import datetime

from updatefy.commands import check_dependencies
from updatefy.datetime import today
from updatefy.log import debug, info
from updatefy.updates import check_updates, get_last_updated


def main():
    debug("Starting...")
    check_dependencies()

    last_updated: datetime | None = get_last_updated()
    if not last_updated or (today() - last_updated).days > 1:
        check_updates()
    else:
        info(f"Last updated: {last_updated}")


if __name__ == "__main__":
    main()
