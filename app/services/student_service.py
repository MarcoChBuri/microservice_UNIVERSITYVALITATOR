from app.repositories import student_repository

def validate_student(db, email: str):
    student = student_repository.get_student_by_email(db, email)
    if student:
        return {
            "isValid": True,
            "name": student.name,
            "university": student.university,
            "message": "Estudiante verificado correctamente"
        }
    return {"isValid": False, "message": "Correo no encontrado en el registro universitario"}

def register_student(db, student_data: dict):
    existing = student_repository.get_student_by_email(db, student_data["email"])
    if existing:
        return {"error": "El estudiante ya está registrado"}
    student = student_repository.create_student(db, student_data)
    return {"message": "Estudiante registrado correctamente", "student": student}
