import logging
from logging.handlers import RotatingFileHandler

def setup_logging():
    fmt = "%(asctime)s %(levelname)s %(name)s | %(message)s"
    handler = RotatingFileHandler("/var/log/worker/worker.log", maxBytes=10_000_000, backupCount=5)
    handler.setFormatter(logging.Formatter(fmt))
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    root.addHandler(handler)

