from fastapi import FastAPI
from datetime import datetime
from icecream import ic
import logging


app = FastAPI()
hits: int = 0

@app.get('/')
def root():
    global hits
    hits += 1

    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    logging.debug(f'Hits: {hits}')

    ic(hits)

    return {
        'status': 'OK',
        'hits': hits,
        'timestamp': datetime.now(),
    }
