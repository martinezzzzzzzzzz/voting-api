from fastapi import FastAPI
from app.routers import voters, candidates, votes

app = FastAPI()

app.include_router(voters.router, prefix="/voters", tags=["Voters"])
app.include_router(candidates.router, prefix="/candidates", tags=["Candidates"])
app.include_router(votes.router, prefix="/votes", tags=["Votes"])