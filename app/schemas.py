from pydantic import BaseModel, EmailStr
from typing import Optional
from pydantic import BaseModel

class VoterCreate(BaseModel):
    name: str
    email: EmailStr

class VoterResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    has_voted: bool

    class Config:
        from_attributes = True

# Alias para evitar errores en imports que usan VoterOut
VoterOut = VoterResponse

class CandidateCreate(BaseModel):
    name: str
    party: str | None = None

class CandidateResponse(BaseModel):
    id: int
    name: str
    party: str | None = None
    votes: int

    class Config:
        from_attributes = True

class VoteCreate(BaseModel):
    voter_id: int
    candidate_id: int

class VoteResponse(BaseModel):
    id: int
    voter_id: int
    candidate_id: int

    class Config:
        from_attributes = True
        
        
        # Esquema para crear candidato
class CandidateCreate(BaseModel):
    name: str
    party: Optional[str] = None

# Esquema para leer candidato (response_model)
class Candidate(BaseModel):
    id: int
    name: str
    party: str | None = None
    votes_count: int

    class Config:
        orm_mode = True

class VoteCreate(BaseModel):
    voter_id: int
    candidate_id: int

class VoteOut(BaseModel):
    id: int
    voter_id: int
    candidate_id: int

    class Config:
        from_attributes = True
        
class UserLogin(BaseModel):
    email: EmailStr
    password: str