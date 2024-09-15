from datetime import datetime

DATETIME_FMT = "%Y-%m-%dT%H:%M:%S"


def now() -> str:
    return datetime.now().strftime(DATETIME_FMT)


def today() -> datetime:
    return datetime.today()
