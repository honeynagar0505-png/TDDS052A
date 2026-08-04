from fastapi import FastAPI, BackgroundTasks

import time

app = FastAPI()

def send_email(email: str):
    print(f"Email sent to: {email}")
    time.sleep(5)

    print("Email sent successfully!")


@app.post("/send-email")
async def register(email: str, background_tasks: BackgroundTasks):
    print("User registered successfully!")

    background_tasks.add_task(send_email, email)

    return {
        "message": "User registered successfully",
        "status": "Please check your email for confirmation."
    }