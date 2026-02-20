from fastapi import FastAPI, Path, Depends, HTTPException
from typing import Annotated
from datetime import date
from sqlmodel import Session
from models import User, UserInput
from database import get_session

app = FastAPI()

@app.get("/")
async def root():
    return {
        "status": "healthy",
        "message": "Welcome to the Hello World API",
        "documentation": "/docs"
    }

@app.put("/hello/{username}", status_code=204)
async def update_register(
    username: Annotated[str, Path(min_length=3, pattern="^[a-zA-Z]+$")],
    user_data: UserInput,
    session: Session = Depends(get_session)
):
    db_user = session.get(User, username)
    if db_user:
        db_user.date_of_birth = user_data.dateOfBirth
    else:
        db_user = User(username=username, date_of_birth=user_data.dateOfBirth)
    
    session.add(db_user)
    session.commit()
    return None

@app.get("/hello/{username}")
async def calculate_bday(
    username : Annotated[
    str, Path(min_length=3, max_length=10, pattern="^[a-zA-Z]+$")],
    session: Session = Depends(get_session)
    ):
    db_user = session.get(User, username)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    today = date.today()
    next_bday = db_user.date_of_birth

    if next_bday >= today:
            days = (next_bday - today).days
            if days ==0:
                return {"message": f"Hello, {username}! Happy birthday"}
            else:
                return {"message": f"Hello, {username}! Your birthday is in {days} days"}
    else:
        next_bday = next_bday.replace(year=today.year+1)
        days = (next_bday - today).days
        return {"message": f"Hello, {username}! Your birthday is in {days} days"}
    