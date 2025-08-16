# python version of the switch statement
from enum import Enum


def http_error_handler(status_code):
    match status_code:
        case 400:
            return "Bad Request"
        case 401:
            return "Unauthorized"
        case 403:
            return "Forbidden"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Error"


def http_error_handler_with_guard(status_code):
    match status_code:
        case 400 | 401 | 403 | 404 | 500:
            return http_error_handler(status_code)
        case _ if isinstance(status_code, int):
            return "Unknown Error"
        case _:
            return "Invalid Status Code"


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# We can add an if clause to a pattern, known as a “guard”. If the guard is false, match goes on to try the next case block.
# Note that value capture happens before the guard is evaluated:
def point_handler(point):
    match point:
        case Point(x, y) if x == y:
            return "Point is on the line y = x"
        case Point(x, y) if x > y:
            return "Point is above the line y = x"
        case Point(x, y):
            return "Point is below the line y = x"
        case _:
            return "Not a valid point"


class Color(Enum):
    RED = "red"  # 1
    GREEN = "green"  # 2
    BLUE = "blue"  # 3


def color_handler(color):
    match color:
        case Color.RED:
            return "Color is Red"
        case Color.GREEN:
            return "Color is Green"
        case Color.BLUE:
            return "Color is Blue"
        case _:
            return "Unknown Color"


# instead of null it is None in Python
def f(a: int | None):
    match a:
        case None:
            return "a is None"
        case _:
            return f"a is {a}"


def add_to_list(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
