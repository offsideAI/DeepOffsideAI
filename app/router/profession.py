import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from typing import List
from fastapi import APIRouter, Depends, status, HTTPException, Response, Query
import database, models
# from sqlalchemy.orm import Session
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select
import oauth2

router = APIRouter(
    tags = ['Professions']
)

###############################################################################
## Profession

@router.post('/professions/', response_model=models.ProfessionRead)
def create_profession(
    *,
    session: Session = Depends(database.get_session),
    current_user: models.User = Depends(oauth2.get_current_user),
    profession: models.ProfessionCreate
):
    db_profession = models.Profession.from_orm(profession)
    session.add(db_profession)
    session.commit()
    session.refresh(db_profession)
    return profession

@router.get('/professions', response_model=List[models.ProfessionRead])
def read_professions(
    *,
    session: Session = Depends(database.get_session),
    current_user: models.User = Depends(oauth2.get_current_user),
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
):
    professions = session.exec(select(models.Profession).offset(offset).limit(limit)).all()
    return professions

@router.get('/professions/{profession_id}', response_model=models.ProfessionReadWithUser)
def read_profession(
    *,
    session: Session = Depends(database.get_session),
    current_user: models.User = Depends(oauth2.get_current_user),
    profession_id: int
):
    profession = session.get(models.Profession, profession_id)
    if not profession:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Profession with id {profession_id} is not available")
    return profession

@router.patch('/professions/{profession_id}', response_model=models.ProfessionRead)
def update_profession(
    *,
    session: Session = Depends(database.get_session),
    current_user: models.User = Depends(oauth2.get_current_user),
    profession_id: int,
    profession: models.ProfessionUpdate
):
    db_profession = session.get(models.Profession, profession_id)
    if not db_profession:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Profession with id {profession_id} not found")
    profession_data = profession.dict(exclude_unset=True)
    for key, value in profession_data.items():
        setattr(db_profession, key, value)
    session.add(db_profession)
    session.commit()
    session.refresh(db_profession)
    return db_profession

@router.delete('/professions/{profession_id}')
def delete_profession(
    *,
    session: Session = Depends(database.get_session),
    current_user: models.User = Depends(oauth2.get_current_user),
    profession_id: int,
):
    profession = session.get(models.Profession, profession_id)
    if not profession:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Profession with id {profession_id} not found")
    session.delete(profession)
    session.commit()
    return {'detail': f"Profession with id {profession_id} was deleted"}


###############################################################################
