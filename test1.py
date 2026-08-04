from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Address(BaseModel):
    city: str
    state: str
    pincode: int

class Student(BaseModel):
    Name: str
    Age: int
    address: Address

student = Student(
    Name="Honey",
    Age=20,
    address=Address(
        city="Mumbai",
        state="Maharashtra",
        pincode=400097
    )
)

print(student)
