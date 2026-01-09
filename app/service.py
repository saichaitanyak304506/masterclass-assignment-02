from Customer import Customer
from repo import CustomerRepository

class CustomerService:
    def __init__(self):
        self.repository = CustomerRepository()

    def add_customer(self, customer: Customer):
        return self.repository.create(customer)

    def get_customer(self, customer_id: int):
        return self.repository.get_by_id(customer_id)

    def get_all_customers(self):
        return self.repository.list_all()

    def update_customer(self, customer: Customer):
        return self.repository.update(customer)

    def remove_customer(self, customer_id: int):
        return self.repository.delete(customer_id)