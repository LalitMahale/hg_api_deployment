from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from deep_translator import GoogleTranslator
from fastapi.responses import JSONResponse

# Create the FastAPI app instance
app = FastAPI()

# Root endpoint
@app.get("/")
async def home():
    return {"message": "Welcome to my FastAPI API on Hugging Face Spaces!"}

# Translate endpoint that accepts a query parameter 'text'
@app.get("/translate")
async def translate(text: str = ""):
    if not text:
        raise HTTPException(status_code=400, detail="No text provided")
    
    # Perform translation using deep_translator
    translator = GoogleTranslator(source="auto", target="mr")
    result = translator.translate(text)
    
    return {"result": result}
