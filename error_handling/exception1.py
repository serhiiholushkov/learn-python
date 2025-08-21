class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass


for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print(D)
    except C:
        print(C)
    except B:
        print(B)
    except Exception:
        print(Exception)


def divide(x: int, y: int) -> float:
    """Divides x by y and returns the result."""
    try:
        return x / y
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return float("inf")  # Return infinity if division by zero occurs
    except TypeError as e:
        print(f"Error: {e}")
        return None  # Return None if types are incorrect
    finally:
        print("Execution completed.")


print(divide(10, 2))  # Should print 5.0
print(divide(10, 0))  # Should print an error message and return infinity
print(divide(10, "a"))  # Should print an error message and return None
