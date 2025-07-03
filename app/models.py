from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Voter(Base):
    __tablename__ = "voters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    has_voted = Column(Boolean, default=False)

    vote = relationship("Vote", back_populates="voter", uselist=False)

class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    party = Column(String(255))
    votes_count = Column(Integer, default=0)

    votes_received = relationship("Vote", back_populates="candidate")

class Vote(Base):
    __tablename__ = "votes"

    id = Column(Integer, primary_key=True, index=True)
    voter_id = Column(Integer, ForeignKey("voters.id"), nullable=False, unique=True)
    candidate_id = Column(Integer, ForeignKey("candidates.id"), nullable=False)

    voter = relationship("Voter", back_populates="vote")
    candidate = relationship("Candidate", back_populates="votes_received")

