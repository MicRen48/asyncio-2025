from fastapi import FastAPI, HTTPException
import asyncio
import random

app = FastAPI(title="Asynchronous Rocket Launcher")

# เก็บ task ของจรวด (optional)
rockets = []

async def launch_rocket(student_id: str):
    """
    Simulate rocket launch with random delay 1-2 seconds and print logs.
    """
    delay = random.uniform(1, 2)
    print(f"Rocket launched for student {student_id}")
    await asyncio.sleep(delay)
    print(f"Rocket reached destination for student {student_id}")

@app.get("/fire/{student_id}")
async def fire_rocket(student_id: str):
    """
    Validate student_id, create background task to launch rocket, wait random delay, and return response.
    """
    if len(student_id) != 10:
        raise HTTPException(status_code=400, detail="Student ID must be 10 digits")
    
    # Create background task to launch rocket
    task = asyncio.create_task(launch_rocket(student_id))
    rockets.append(task)
    
    # Wait random delay 1-2 seconds before responding
    delay = random.uniform(1, 2)
    await asyncio.sleep(delay)
    
    return {"message": f"Rocket fired for student {student_id}", "time_to_target": delay}
