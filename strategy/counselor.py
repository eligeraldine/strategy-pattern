class Counselor:
    def __init__(self, name, specialization, rating, price):
        self.name = name
        self.specialization = specialization
        self.rating = rating
        self.price = price

    # String representation of the Counselor object
    def __str__(self):
        return f"Name: {self.name} - Spec: {self.specialization} - Rating: {self.rating} - Price: {self.price}"
