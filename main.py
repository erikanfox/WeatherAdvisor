"""Scrabble Microservice"""
from fastapi import FastAPI
import uvicorn


app = FastAPI()

@app.get("/")
async def root():
    """Scrabble Microservice Welcome"""
    return {"message": "Hello, welcome to ScrabbleHelper! Enter a word to calculate it's score."}

@app.get("/scrabblehelper/{word}")
async def scrabblehelper(word: str):
    """calculate scrabble score"""
    scores={ 'a':1,
            'b':3,
            'c':3,
            'd':2,
            'e':1,
            'f':4,
            'g':2,
            'h':4,
            'i':1,
            'j':8,
            'k':5,
            'l':1,
            'm':3,
            'n':1,
            'o':1,
            'p':3,
            'q':10,
            'r':1,
            's':1,
            't':1,
            'u':1,
            'v':4,
            'w':4,
            'x':8,
            'y':4,
            'z':10}
    sum1 = 0
    for char in word:
        sum1=sum1+scores[char]


    return {"score": sum1}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
