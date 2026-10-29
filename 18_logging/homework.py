import logging
from pathlib import Path

logger = logging.getLogger("homework")


def setup_logging():
    logger.setLevel(logging.DEBUG)
    logger.propagate = False
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
        handler.close()
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)
    file = logging.FileHandler(Path(__file__).with_name("homework.log"), encoding="utf-8")
    file.setLevel(logging.DEBUG)
    file.setFormatter(formatter)
    logger.addHandler(console)
    logger.addHandler(file)


def divide(a, b):
    logger.debug("divide викликана з a=%s, b=%s", a, b)
    try:
        result = a / b
    except ZeroDivisionError:
        logger.error("Не можна ділити на нуль: %s / %s", a, b)
        return None
    logger.info("Результат ділення: %s", result)
    return result


if __name__ == "__main__":
    setup_logging()
    divide(10, 2)
    divide(10, 0)
