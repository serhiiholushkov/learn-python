def full_name_str(first_name: str, last_name: str) -> str:
    """Formats the full name from first and last names."""
    return f"{first_name} {last_name}"


print(full_name_str("John", "Doe"))  # Output: John Doe

print("We sent him {} at {}.".format("an email", "8 PM"))
# Or with the named placeholders
print("We sent him {action} at {time}.".format(action="an email", time="8 PM"))
# Or with the f-string
action = "an email"
time = "8 PM"
print(f"We sent him {action} at {time}.")


def price_formatter(price: float, currency: str = "USD") -> str:
    """Formats the price with the currency."""
    return f"{price:,.2f} {currency}"


print(price_formatter(19.99))  # Output: 19.99 USD
print(price_formatter(19.99, "EUR"))  # Output: 19.99 EUR
print(price_formatter(345_356_342.67, "JPY"))  # Output: 345,356,342.67 JPY
print(price_formatter(-235_466_352.452, "GBP"))  # Output: -235,466,352.45 GBP


def format_date(day: int, month: int, year: int) -> str:
    """Formats the date in DD-MM-YYYY format."""
    return f"{day:02d}-{month:02d}-{year}"


print(format_date(5, 3, 2023))  # Output: 05-03-2023
