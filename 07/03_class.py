class Employee:
    __slots__ = ("__salary", "first_name", "job", "last_name")

    def __init__(self, first_name, last_name, job, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.__salary = salary

    @property
    def salary(self):
        return round(self.__salary, 2)

    @salary.setter
    def salary(self, value):
        top_salary = 100_000
        self.__salary = min(value, top_salary)

    @salary.deleter
    def salary(self):
        del self.__salary
        print("Person is unpaid")


person = Employee("Jack", "Black", "singer", 98_000)
print(person.salary)
person.salary = 99_000
print(person.salary)
person.salary = 120_000
print(person.salary)
del person.salary
# print(person.salary)
