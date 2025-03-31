from fastapi import FastAPI, HTTPException
import openai
import os
from dotenv import load_dotenv

# Load API Key from .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI
if not OPENAI_API_KEY:
    raise ValueError("Missing OpenAI API Key. Set it in .env file.")

openai.api_key = OPENAI_API_KEY

# Initialize FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to AI-Powered Mood-Based Song Recommender!"}

@app.get("/recommend")
async def recommend_songs(mood: str):
    """Fetches AI-generated song recommendations based on mood."""
    
    if not mood.strip():
        raise HTTPException(status_code=400, detail="Mood cannot be empty.")

    prompt = f"Suggest 5 songs that match the mood '{mood}' with song name and artist."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a music recommendation expert."},
                {"role": "user", "content": prompt}
            ]
        )
        
        songs = response['choices'][0]['message']['content'].split("\n")
        
        return {"songs": [song.strip() for song in songs if song.strip()]}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching songs: {str(e)}")
