from fastapi import FastAPI
import uvicorn
import sys

app = FastAPI()

@app.post("/reset")
async def reset():
    # Standard OpenEnv Log
    print("START")
    sys.stdout.flush() 
    return {
        "observation": "Vibe Navigator Ready. Please enter a city (Chennai/Delhi).", 
        "info": {}
    }

@app.post("/step")
async def step(action: dict):
    # Standard OpenEnv Log
    print("STEP")
    sys.stdout.flush()
    
    city = action.get("city", "").lower()
    
    if "chennai" in city:
        res = "Vibe: Coastal & Cultural. Recommended: Marina Beach."
    elif "delhi" in city:
        res = "Vibe: Historic & Vibrant. Recommended: Chandni Chowk."
    else:
        res = "City not recognized in the current vibe database."

    # Standard OpenEnv Log
    print("END")
    sys.stdout.flush()
    
    return {
        "observation": res, 
        "reward": 1.0, 
        "done": True, 
        "info": {}
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)



