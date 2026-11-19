def log_args(*args):
    print(type(args), args)


abc = "abcdef"
first, *_, last = abc
print(first, _, last)

log_args(1, 2, 3, 4, 5, True, lambda x: x**3)


def log_kwargs(**kwargs):
    print(type(kwargs), kwargs)


log_kwargs(name="John", age=22, hobbies=["reading", "swimming"])


def generate_filter_query(**filters):
    query = "SELECT * FROM products WEHERE "
    for k, v in filters.items():
        query += f"{k}='{v}' AND "
    return query[:-5]


print(generate_filter_query(color="red", size="L", material="cotton"))


# item: {name, quantity, price}
def calculate_total_price(*items, **kwargs):
    total_price = sum(i["price"] * i["quantity"] for i in items)
    if "vat" in kwargs:
        total_price *= 1 + kwargs["vat"]
    if "discount" in kwargs:
        total_price *= 1 - kwargs["discount"]
    return round(total_price)


total = calculate_total_price(
    {"name": "CPU", "quantity": 12, "price": 679},
    {"name": "VGA", "quantity": 1, "price": 1999},
    {"name": "Monitor", "quantity": 56, "price": 1200},
    vat=0.27,
    discount=0.05,
)

print(total)
