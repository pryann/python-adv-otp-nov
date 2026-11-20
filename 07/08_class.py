class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"first_name: {self.first_name}, last_name {self.last_name}, age: {self.age}"

    def __repr__(self):
        return f"{self.__class__.__name__} ({self.first_name}, {self.last_name}, {self.age})"

    def __eq__(self, other):
        if self is other:
            return True
        elif not isinstance(other, Person):
            return False
        else:
            # fmt: off
            return (
                self.first_name == other.first_name 
                and self.last_name == other.last_name 
                and self.age == other.age
            )


person = Person("John", "Doe", 33)
person2 = Person("John", "Doe", 33)
print(person)
print(repr(person))
print(person == person2)
