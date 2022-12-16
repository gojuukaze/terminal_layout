import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)


def disable_logger():
    handler = logging.NullHandler()
    logger.handlers = [handler]


def enable_logger():
    handler = logging.FileHandler("terminal_layout.log")
    handler.setLevel(logging.DEBUG)
    # formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    formatter = logging.Formatter('%(levelname)s : %(message)s')

    handler.setFormatter(formatter)
    logger.addHandler(handler)


disable_logger()
