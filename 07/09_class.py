from dataclasses import dataclass, field


@dataclass(slots=True, order=True)
class Person:
    sort_index: int = field(init=False, repr=False)
    first_name: str
    last_name: str
    age: int

    def __post_init__(self):
        object.__setattr__(self, "sort_index", self.age)


p = Person("Kiss", "Gizi", 88)
p2 = Person("Kiss", "Gizi", 88)
p3 = Person("Kiss", "Gizi", 89)
print(p)
print(repr(p))
print(p == p2)
print(p > p3)
print(p2 < p3)
# p.job = "mentor"
