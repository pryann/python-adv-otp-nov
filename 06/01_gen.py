name = "John Doe"
str_iterator = iter(name)
print(next(str_iterator))
print(next(str_iterator))
print(next(str_iterator))

roles = ("admin", "user", "sysadmin")
roles_iter = iter(roles)
print(next(roles_iter))
print(next(roles_iter))
print(next(roles_iter))
# StopIteration
# print(next(roles_iter))

roles_iter = iter(roles)
for role in roles_iter:
    print(role)
