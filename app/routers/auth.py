from fastapi import APIRouter, HTTPException, status
from app.auth.jwt_handler import create_access_token
from app.schemas import UserLogin

router = APIRouter()

@router.post("/login")
def login(user: UserLogin):
    token_data = {
        "sub": user.email
    }
    access_token = create_access_token(token_data)
    return {"access_token": access_token, "token_type": "bearer"}
