from pydantic import BaseModel,ConfigDict

class CustomerCreate(BaseModel):
    id: int
    name: str
    email: str
    active: bool

class CustomerResponse(CustomerCreate):
    
    model_config= ConfigDict(
        from_attributes=True
    )
