from fastapi import FastAPI, HTTPException
from Customer import Customer
from service import CustomerService

app = FastAPI()
customer_service = CustomerService()

@app.post("/customers/", status_code=201)
def create_customer(customer: Customer):
    return customer_service.add_customer(customer)

@app.get("/customers/")
def read_customers():
    return customer_service.get_all_customers()

@app.get("/customers/{customer_id}")
def read_customer(customer_id: int):
    customer = customer_service.get_customer(customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@app.put("/customers/{customer_id}")
def update_customer(customer_id: int, customer: Customer):
    if customer_id != customer.id:
        raise HTTPException(status_code=400, detail="ID mismatch")

    if not customer_service.update_customer(customer):
        raise HTTPException(status_code=404, detail="Customer not found")

    return {"message": "Updated successfully"}

@app.delete("/customers/{customer_id}")
def delete_customer(customer_id: int):
    if not customer_service.remove_customer(customer_id):
        raise HTTPException(status_code=404, detail="Customer not found")

    return {"message": "Deleted successfully"}
