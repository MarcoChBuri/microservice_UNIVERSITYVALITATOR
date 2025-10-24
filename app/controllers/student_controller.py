from sqlalchemy.orm import Session
from app.repositories import student_repository
from app.schemas import student_schema

def register_student(student: student_schema.StudentCreate, db: Session):
    existing = student_repository.get_student_by_email(db, student.email)
    if existing:
        return {"valid": False, "message": "El correo ya está registrado"}
    
    new_student = student_repository.create_student(db, student.dict())
    return {"valid": True, "message": "Usuario registrado", "student": new_student}

def validate_student(req: student_schema.ValidationRequest, db: Session):
    student = student_repository.get_student_by_email(db, req.email)
    if not student:
        return {"valid": False, "message": "Estudiante no encontrado"}
    
    if student.university != req.university:
        return {"valid": False, "message": "La universidad no coincide"}
    
    return {"valid": True, "message": "Estudiante válido"}
