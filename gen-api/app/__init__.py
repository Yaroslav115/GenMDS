from .logging import setup_logging
setup_logging()
from fastapi import FastAPI
app = FastAPI()
