# *arguments are also called *args sometimes.
# They allow you to pass a variable number of arguments to a function.
# **keywords are also called **kwargs sometimes.
# They allow you to pass a variable number of keyword arguments to a function.
def cheeseshop(kind: str, *arguments: str, **keywords: str) -> None:
    """A function that simulates a cheeseshop."""
    print(f"Kind: {kind}")

    if arguments:
        print("Arguments:", ", ".join(arguments))

    if keywords:
        print("Keywords:", ", ".join(f"{k}={v}" for k, v in keywords.items()))
    print("Thank you for visiting the cheeseshop!")


cheeseshop("Cheddar", "Aged", "Sharp", flavor="Savory", region="Somerset")
