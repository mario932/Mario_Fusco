class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def is_adult(self):
        return self.age >= 18


person1 = Person("Mario", "Fusco", 26)
print(f"Full Name: {person1.full_name()}")
print(f"Is Adult: {person1.is_adult()}")
