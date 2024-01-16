from fastapi import FastAPI

from .schema.request import Text
from .schema.response import Vector
from .service import RetrieveService


app = FastAPI()
service = RetrieveService()


@app.post("/vectorize", response_model=Vector)
def vectorize(request: Text) -> Vector:
    values = service.retrieve(request)
    return Vector(values=values)
