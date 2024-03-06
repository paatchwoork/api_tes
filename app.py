from fastapi import FastAPI
import os

PORT = os.environ.get('PORT', 8000)
app = FastAPI(port=PORT)

@app.get('/')
async def root():
    return {'Status': 'Alive!'}

@app.get('/hello')
async def say_hello(usr: str = 'Anon'):
    return {'Message': f'Hello {usr}!'}
