class Customer:
    services = []
    def __init__(self, name):
        self.name = name

    def add_service(self, name, date, time_amount):
        service = Service(name, date, time_amount)
        self.services.append(service)

class Service:
    def __init__(self, name, date, time_amount):
        self.name = name
        self.date = date
        self.time_amount = time_amount
