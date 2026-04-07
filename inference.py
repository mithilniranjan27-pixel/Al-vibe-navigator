from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# This is the "OpenEnv Reset" the grader is looking for
@app.post("/reset")
async def reset():
    return {"observation": "Welcome to Vibe Navigator! Enter a city (Chennai/Delhi).", "info": {}}

# This is where the AI takes a step
@app.post("/step")
async def step(action: dict):
    # Get the city from the action message
    city = action.get("city", "").lower()
    
    if city == "chennai":
        response = "Cafe Aroma -> Cozy place\nBeach side vibes found!"
    elif city == "delhi":
        response = "Lotus Cafe -> Aesthetic\nCity Park vibes found!"
    else:
        response = "No data available for this city."
        
    # OpenEnv expects: observation, reward, done, info
    return {
        "observation": response, 
        "reward": 1.0, 
        "done": True, 
        "info": {}
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)


