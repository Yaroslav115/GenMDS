import logging
from logging.handlers import RotatingFileHandler

def setup_logging():
    fmt = "%(asctime)s %(levelname)s %(name)s | %(message)s"
    datefmt = "%Y-%m-%d %H:%M:%S"

    logging.basicConfig(level=logging.INFO, format=fmt, datefmt=datefmt)

    file_handler = RotatingFileHandler("/var/log/api/app.log", maxBytes=10_000_000, backupCount=5)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter(fmt=fmt, datefmt=datefmt))

    root = logging.getLogger()
    root.addHandler(file_handler)

