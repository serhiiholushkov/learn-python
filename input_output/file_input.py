def read_file(file_path: str) -> str:
    """Reads the content of a file and returns it as a string."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()
    # if you're not using with, remember to close the file:
    # file = open(file_path, "r", encoding="utf-8")
    # content = file.read()
    # file.close()
    # check: file.closed  # should be True if closed properly


def write_file(file_path: str, content: str) -> None:
    """Writes the given content to a file."""
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)


def append_to_file(file_path: str, content: str) -> None:
    """Appends the given content to a file."""
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(content)


print(read_file("input_output/file_example.txt"))  # Reads the content of the file
write_file("input_output/new_file.txt", "This is a new file.")  # Writes to a new file
append_to_file(
    "input_output/new_file.txt", "\nThis is appended text."
)  # Appends text to the existing file
print(read_file("input_output/new_file.txt"))  # Reads the content of the new file
