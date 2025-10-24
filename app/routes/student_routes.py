from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.controllers import student_controller
from app.schemas import student_schema
from app.database import get_db
from app.repositories import student_repository

router = APIRouter(prefix="/students", tags=["Students"])

@router.post("/register")
def register_student(student: student_schema.StudentCreate, db: Session = Depends(get_db)):
    return student_controller.register_student(student, db)

@router.post("/validate")
def validate_student(req: student_schema.ValidationRequest, db: Session = Depends(get_db)):
    student = student_repository.get_student_by_email(db, req.email)
    if not student:
        return {"valid": False, "message": "Estudiante no encontrado"}
    
    return {"valid": True, "message": "Estudiante válido"}
