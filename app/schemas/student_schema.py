from pydantic import BaseModel, EmailStr

class StudentCreate(BaseModel):
    name: str
    email: EmailStr
    university: str

    model_config = {"from_attributes": True}

class StudentResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    university: str

    model_config = {"from_attributes": True}

class ValidationRequest(BaseModel):
    email: EmailStr

    model_config = {"from_attributes": True}
