from abc import ABC, abstractmethod

# Abstract base class for filter strategies
class FilterStrategy(ABC):
    @abstractmethod
    def filter(self, counselors):
        pass

class FilterByName(FilterStrategy):
    def __init__(self, name):
        self.name = name.lower() # Normalize to lowercase for case-insensitive comparison

    def filter(self, counselors):
        return [
            k for k in counselors
            if self.name in k.name.lower()
        ]

class FilterBySpecialization(FilterStrategy):
    def __init__(self, specialization):
        self.specialization = specialization.lower()

    def filter(self, counselors):
        return [
            k for k in counselors
            if self.specialization in k.specialization.lower()
        ]

class FilterByRating(FilterStrategy):
    def __init__(self, rating):
        self.rating = rating

    def filter(self, counselors):
        return [
            k for k in counselors
            if k.rating == self.rating
        ]

class FilterByPrice(FilterStrategy):
    def __init__(self, price):
        self.price = price

    def filter(self, counselors):
        return [
            k for k in counselors
            if k.price == self.price
        ]

