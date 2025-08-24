from dataclasses import dataclass


# Using dataclass to automatically generate init, repr, and other methods
# This is useful for classes that are primarily used to store data
# It is similar to structs or records in other languages
@dataclass
class Employee:
    name: str
    id: int
    department: str = "General"
    active: bool = True
    salary: float = 50000.0


e1 = Employee("Alice", 1, "HR", True, 60000.0)
e2 = Employee("Bob", 2)  # Uses default values for department, active, and salary
print(e1)
print(e2)
