# class Category:
#     def __init__(self, *args):
#         if len(args) == 1:
#             self.name = args[0]
#         if len(args) == 2:
#             self.name = args[0]
#             self.description = args[1]


class Category:
    def __init__(self, name: str, description: str | None = None):
        self.name = name
        self.description = description

    @classmethod
    def from_dict(cls, data: dict) -> "Category":
        return cls(data["name"], data.get("description", None))

    @classmethod
    def from_string(cls, s: str) -> "Category":
        parts = s.split("|")
        return cls(*parts)


c1 = Category("Electronics")
print(c1.name, c1.description)
c2 = Category("Electronics", "Electronics Description")
print(c2.name, c2.description)
c3 = Category.from_dict({"name": "Electronics", "description": "Electronics Description"})
print(c3.name, c3.description)
c4 = Category.from_string("Electronics|Electronics Description")
print(c4.name, c4.description)
