from Customer import Customer

class CustomerRepository:
    def __init__(self):
        self.customers: dict[int, Customer] = {}

    def create(self, customer: Customer):
        self.customers[customer.id] = customer
        return customer

    def get_by_id(self, customer_id: int):
        return self.customers.get(customer_id)

    def list_all(self):
        return list(self.customers.values())

    def update(self, customer: Customer):
        if customer.id in self.customers:
            self.customers[customer.id] = customer
            return True
        return False

    def delete(self, customer_id: int):
        return self.customers.pop(customer_id, None) is not None