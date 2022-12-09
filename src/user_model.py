from typing import Optional
from pydantic import BaseModel

class UserQuery(BaseModel):
    movie_name: str
    no_of_recommendation: Optional[int] = 10


class OutputResponse(BaseModel):
    movie_name: str
    genra: str
