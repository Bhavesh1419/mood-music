from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import random

app = FastAPI()

# Mood-based song database (Example data)
songs_db = {
    "happy": ["Happy - Pharrell Williams", "Can't Stop the Feeling - Justin Timberlake", "Shake It Off - Taylor Swift"],
    "sad": ["Someone Like You - Adele", "Fix You - Coldplay", "Stay With Me - Sam Smith"],
    "energetic": ["Eye of the Tiger - Survivor", "Stronger - Kanye West", "We Will Rock You - Queen"],
    "calm": ["Weightless - Marconi Union", "Thinking Out Loud - Ed Sheeran", "Better Together - Jack Johnson"]
}

class MoodRequest(BaseModel):
    mood: str

@app.get("/")
def home():
    return {"message": "Welcome to Mood-Based Song Recommender!"}

@app.post("/recommend", response_model=List[str])
def recommend_songs(request: MoodRequest):
    mood = request.mood.lower()
    if mood in songs_db:
        return random.sample(songs_db[mood], min(len(songs_db[mood]), 3))  # Return up to 3 songs
    return ["No songs found for this mood."]
