"""Hello module for Python CI test."""


def get_greeting(name):
    """Return a greeting message."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(get_greeting("World"))
