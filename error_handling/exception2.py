from exceptions.age_exception import AgeException


def register_user(name: str, age: int) -> str:
    """Registers a user with the given name and age."""
    if not (0 <= age <= 120):
        raise AgeException(age)
    return f"User {name} registered successfully with age {age}."


try:
    register_user("Alice", 150)
except AgeException as e:
    print(e)

try:
    register_user("Bob", 25)
except AgeException as e:
    print(e)
else:
    print("User registered successfully.")
finally:
    print("Registration process completed.")
