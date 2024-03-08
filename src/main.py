from fastapi import FastAPI
from datetime import datetime


app = FastAPI()
hits: int = 0

@app.get('/')
def root():
    global hits
    hits += 1

    return {
        'status': 'OK',
        'hits': hits,
        'timestamp': datetime.now(),
    }
