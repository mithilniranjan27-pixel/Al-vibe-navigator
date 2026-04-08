from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import sys

app = FastAPI()

# Internal State Management
class EnvState:
    def __init__(self):
        self.current_step = 0
        self.max_steps = 5
        self.location = "Start"

state = EnvState()

@app.post("/reset")
async def reset():
    """Resets the environment to the initial state."""
    print("START") # Required Log
    sys.stdout.flush()
    
    state.current_step = 0
    state.location = "Start"
    
    return {
        "observation": "System Initialized at Start. Available actions: Chennai, Delhi.",
        "info": {"status": "ready"}
    }

@app.post("/step")
async def step(action_data: dict):
    """Processes the agent's action and returns the next state."""
    print("STEP") # Required Log
    sys.stdout.flush()
    
    # Extract action
    action = action_data.get("action", "").lower()
    state.current_step += 1
    
    # Logic for State Transition and Reward
    if action == "chennai":
        obs = "Arrived at Marina Beach. Vibe: Peaceful."
        reward = 1.0
        state.location = "Chennai"
    elif action == "delhi":
        obs = "Arrived at Chandni Chowk. Vibe: Energetic."
        reward = 0.8
        state.location = "Delhi"
    else:
        obs = "Invalid action. Staying at Start."
        reward = -0.1
    
    # Check if the episode is finished
    done = state.current_step >= state.max_steps
    
    if done:
        print("END") # Required Log
        sys.stdout.flush()

    return {
        "observation": obs,
        "reward": reward,
        "done": done,
        "info": {"current_location": state.location, "step_count": state.current_step}
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)




