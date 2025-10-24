from fastapi import FastAPI
from app.database import Base, engine
from app.routes import student_routes

app = FastAPI(
    title="University Verifier Service",
    version="2.0",
    description="Microservicio de validación universitaria (modelo CSR)"
)

app.include_router(student_routes.router)

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)
    print("📘 Base de datos inicializada correctamente.")

@app.get("/")
def home():
    return {"message": "Microservicio de validación universitaria (modelo CSR)"}
