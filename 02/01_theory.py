#  fn is a first class citizen


def log_error(message):
    print("ERROR", message)


log_error_fn = log_error
log_error_fn("NotFound")


# def outer_fn(text):
#     message = text

#     def inner_fn():
#         print(message)

#     inner_fn()


# outer_fn("The message")


def outer_fn(text):
    message = text

    def inner_fn():
        print(message)

    # closure
    return inner_fn


result = outer_fn("message")
result()
