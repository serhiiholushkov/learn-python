from simple_module import some_function

# Or
# import simple_module

from multi_file_module import *

## Using functions from simple_module
some_function()  # This will call the function from simple_module
# Or if you import whole module
# simple_module.some_function()


## Using functions from multi_file_module
echo_result = echo.echo("Hello, World!")  # Calls the echo function
print(echo_result)
surround_result = surround.surroind("Hello, World!")  # Calls the surround function
print(surround_result)
reverse_result = reverse.reverse("Hello, World!")  # Calls the reverse function
print(reverse_result)

# But you can't call other_function if you import whole multi_file_module or *
# because they are not imported in __init__.py of multi_file_module
# Howver, you can call them if you import them directly
# from multi_file_module.other import other_function, another_function
# other_function()  # Calls the other_function from other.py
# another_function()  # Calls the another_function from other.py
