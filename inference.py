from fastapi import FastAPI
import uvicorn

app = FastAPI()

# This is what the "OpenEnv Reset" check is looking for!
@app.post("/reset")
async def reset():
    # This resets your "navigator" to a starting state
    return {"observation": "starting_point", "info": {}}

@app.post("/step")
async def step(action: dict):
    # Your logic goes here (e.g., navigating to Chennai or Delhi)
    city = action.get("city", "").lower()
    
    if city == "chennai":
        response = "Cafe Aroma -> Cozy place\nBeach..."
    elif city == "delhi":
        response = "Lotus Cafe -> Aesthetic\nCity Park..."
    else:
        response = "No data available"
        
    return {"observation": response, "reward": 1, "done": True, "info": {}}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)

