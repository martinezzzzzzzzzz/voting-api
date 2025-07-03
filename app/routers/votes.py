from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session
from sqlalchemy import func
from app import models, schemas
from app.database import get_db

security = HTTPBasic()

def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = "admin"
    correct_password = "secret"

    if credentials.username != correct_username or credentials.password != correct_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas.",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

router = APIRouter()

@router.post("/", response_model=schemas.VoteOut, status_code=status.HTTP_201_CREATED)
def create_vote(
    vote: schemas.VoteCreate,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    voter = db.query(models.Voter).filter(models.Voter.id == vote.voter_id).first()
    if not voter:
        raise HTTPException(status_code=404, detail="Votante no encontrado")

    if voter.has_voted:
        raise HTTPException(status_code=400, detail="El votante ya ha votado")

    candidate = db.query(models.Candidate).filter(models.Candidate.id == vote.candidate_id).first()
    if not candidate:
        raise HTTPException(status_code=404, detail="Candidato no encontrado")

    db_vote = models.Vote(voter_id=vote.voter_id, candidate_id=vote.candidate_id)
    voter.has_voted = True
    candidate.votes_count += 1

    db.add(db_vote)
    db.commit()
    db.refresh(db_vote)
    return db_vote

@router.get("/", response_model=list[schemas.VoteOut])
def get_all_votes(
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    return db.query(models.Vote).all()

@router.get("/statistics")
def get_vote_statistics(
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    total_votes = db.query(func.count(models.Vote.id)).scalar()
    total_voters_voted = db.query(func.count(models.Voter.id)).filter(models.Voter.has_voted == True).scalar()

    candidates = db.query(models.Candidate).all()
    candidates_stats = []
    for candidate in candidates:
        percentage = 0.0
        if total_votes > 0:
            percentage = (candidate.votes_count / total_votes) * 100

        candidates_stats.append({
            "candidate_id": candidate.id,
            "name": candidate.name,
            "votes_count": candidate.votes_count,
            "percentage": round(percentage, 2)
        })

    return {
        "total_votes": total_votes,
        "total_voters_voted": total_voters_voted,
        "candidates": candidates_stats
    }
