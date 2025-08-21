class AgeException(Exception):
    """Custom exception for invalid age values."""

    def __init__(self, age, message="Age must be between 0 and 130."):
        self.age = age
        self.message = message
        super().__init__(f"{self.message} Provided age: {self.age}")
