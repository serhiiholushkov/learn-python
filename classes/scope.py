def scope_test():
    """Demonstrates the concept of scope in Python."""

    def do_local():
        """A local function that modifies a local variable."""
        spam = "local spam"

    def do_nonlocal():
        """A nonlocal function that modifies a nonlocal variable."""
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        """A global function that modifies a global variable."""
        global spam
        spam = "global spam"

    spam = "test spam"  # This is a local variable in scope_test
    print("Before local:", spam)

    do_local()
    print("After local:", spam)  # Should still be "test spam"
    do_nonlocal()
    print("After nonlocal:", spam)  # Should be "nonlocal spam"
    do_global()
    print("After global:", spam)  # Should still be "nonlocal spam"
    # because spam here is a scope_test variable that overrides the global one
    # and do_global modifies the global variable spam


if __name__ == "__main__":
    scope_test()
    print("In global scope:", spam)  # Should be "global spam"
