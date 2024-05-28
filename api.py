from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import pandas as pd

def add_email(email):
    file_path = 'email_list.csv'
    """Add an email to the CSV file if it doesn't already exist."""
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        df = pd.DataFrame(columns=['emails'])

    if email in df['emails'].values:
        print(f"Email {email} already exists in {file_path}.")
    else:
        new_row = pd.DataFrame([[email]], columns=['emails'])
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_csv(file_path, index=False)
        print(f"Email {email} added to {file_path}.")

def delete_email(email):
    file_path = 'email_list.csv'
    """Delete an email from the CSV file."""
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return

    if email not in df['emails'].values:
        print(f"Email {email} not found in {file_path}.")
    else:
        df = df[df['emails'] != email]
        df.to_csv(file_path, index=False)
        print(f"Email {email} deleted from {file_path}.")

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

class TextIn(BaseModel):
    email: str
    mood: int 

class TextOut(BaseModel):
    add_emails: List[str]
    delt_emails: Optional[List[str]] = None

@app.post("/email", response_model=TextOut)
async def echo(text_in: TextIn):
    add_emails = []
    delt_emails = []
    
    if text_in.mood == 0:
        add_email(text_in.email)
        add_emails.append(text_in.email)
    elif text_in.mood == 1:
        delete_email(text_in.email)
        delt_emails.append(text_in.email)
        
    return {"add_emails": add_emails, "delt_emails": delt_emails}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5000)
