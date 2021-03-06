from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


import random


app = FastAPI()

# CORS setup
origins = [
    "http://localhost:3000",
    "localhost:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Hello, world!"}


@app.get("/data")
async def get_sample() -> dict:
    choices = ['foo', 'bar', 'baz']
    colors = [
        'primary', 'secondary', 
        'success', 'warning', 'error', 
        'info'
    ]
    return {
        "val": random.choice(choices),
        "number": random.random(),
        "color": random.choice(colors),
    }