from sqlalchemy.orm import Session
from app.models.student_model import Student

def get_student_by_email(db: Session, email: str):
    return db.query(Student).filter(Student.email == email).first()

def create_student(db: Session, student_data: dict):
    new_student = Student(**student_data)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student
