from fastapi import APIRouter, Depends, UploadFile
import sys
import logging
from database import SessionLocal
from sqlalchemy.orm import Session
from models import Document

router = APIRouter(tags=['RAG'])
logger = logging.getLogger(__name__)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.post('/file', summary='load a file')
def upload_file(file:UploadFile=None, db: Session = Depends(get_db)):
    try:
        file_name = file.filename.split('.')[0]
        file_type = file.filename.split('.')[1]
        user = Document(name=file_name, type=file_type)
        db.add(user)
        db.commit()
        db.refresh(user)
        return {'message': 'File uploaded successfully', 'data':user}
    except Exception as err:
        return {"error": f"{type(err).__name__} was raised: {err} Error on line " + format(
                sys.exc_info()[-1].tb_lineno)}

