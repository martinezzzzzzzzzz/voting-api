from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db
from app.auth.basic_auth import get_current_user

router = APIRouter(
    dependencies=[Depends(get_current_user)]
)

@router.post("/", response_model=schemas.VoterOut, status_code=status.HTTP_201_CREATED)
def create_voter(voter: schemas.VoterCreate, db: Session = Depends(get_db)):
    existing_voter = db.query(models.Voter).filter(models.Voter.email == voter.email).first()
    if existing_voter:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El correo electrónico ya está registrado."
        )
    
    db_voter = models.Voter(name=voter.name, email=voter.email)
    db.add(db_voter)
    db.commit()
    db.refresh(db_voter)
    return db_voter

@router.get("/", response_model=list[schemas.VoterOut])
def get_all_voters(db: Session = Depends(get_db)):
    return db.query(models.Voter).all()

@router.get("/{voter_id}", response_model=schemas.VoterOut)
def get_voter_by_id(voter_id: int, db: Session = Depends(get_db)):
    voter = db.query(models.Voter).filter(models.Voter.id == voter_id).first()
    if not voter:
        raise HTTPException(status_code=404, detail="Votante no encontrado")
    return voter

@router.delete("/{voter_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_voter(voter_id: int, db: Session = Depends(get_db)):
    voter = db.query(models.Voter).filter(models.Voter.id == voter_id).first()
    if not voter:
        raise HTTPException(status_code=404, detail="Votante no encontrado")
    db.delete(voter)
    db.commit()
