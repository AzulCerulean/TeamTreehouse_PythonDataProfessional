def does_something(arg):
    """Takes one arg and does something based on type.
    If arg is a string, returns arg * 3;
    If arg is an int or float, returns arg + 10
    """
    if isinstance(arg, (int, float)):
        return arg + 10
    elif isinstance(arg, str):
        return str * 3
    else:
        raise TypeError("does_something only takes ints, floats, and strings")

# the added docstring to the function creates a help text
# available in the REPL.

# python3
# >>> import docstrings
# >>> help(docstrings.does_something)

# importing the file and then calling help(file.func)
