def add_chesee(burger):
    burger["chesee"] = True
    return burger


def add_double_meal(burger):
    burger["double_meal"] = True
    return burger


def add_glutenfree_bun(burger):
    burger["glutenfree_bun"] = True
    return burger


def remove_onion(burger):
    burger["onion"] = False
    return burger


def make_burger(burger, *fns):

    for fn in fns:
        burger = fn(burger)
    return burger


custom_burger = make_burger({}, add_chesee, add_double_meal, remove_onion)
print(custom_burger)
