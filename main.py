from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS to allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your frontend URL for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/recommend")
def recommend(mood: str):  # Ensures 'mood' matches frontend query
    mood = mood.lower()  # Normalize input

    mood_songs = {
        "happy": ["Happy - Pharrell Williams", "Can't Stop the Feeling - Justin Timberlake"],
        "sad": ["Someone Like You - Adele", "Fix You - Coldplay"],
        "excited": ["Uptown Funk - Bruno Mars", "Don't Stop Me Now - Queen"],
        "relaxed": ["Weightless - Marconi Union", "Clair de Lune - Debussy"],
    }

    return {"songs": mood_songs.get(mood, ["No recommendations available"])}

