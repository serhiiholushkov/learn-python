# Decorator - A function that modifies the behavior of another function


def add_sprinkles(func):
    """A decorator that adds sprinkles to the output of the decorated function."""

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + " with sprinkles"

    return wrapper


def add_fundge(func):
    """A decorator that adds fundge to the output of the decorated function."""

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + " with fundge"

    return wrapper


@add_sprinkles
@add_fundge
def make_ice_cream(flavor):
    """A simple function that returns a string."""
    return "Ice cream " + flavor


print(make_ice_cream("vanilla"))  # Output: Ice cream with sprinkles
