def say_hello(name=None):
    if not name:
        name = "World"

    return f'Hello, {name} - from version 1.0'
