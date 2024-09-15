from updatefy.commands import check_dependencies
from updatefy.log import debug
from updatefy.updates import check_updates, needs_checking


def main():
    debug("Starting...")
    check_dependencies()

    if needs_checking():
        check_updates()


if __name__ == "__main__":
    main()
