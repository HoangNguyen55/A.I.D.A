### Use Black formatter

Black is a python formatter, it will make everyone's code look in the same style, that way its easier to read each other's code.

Set up the black formatter in vscode [here](https://code.visualstudio.com/docs/python/formatting)

Set up in pycharm [here](<https://www.jetbrains.com/help/pycharm/reformat-and-rearrange-code.html#format-python-code-with-black>)

### Use f strings
F string can be use to insert variable's values directly in a string, its more readable than `.format`.

```py
# Correct
def combine(x, y):
    print(f"x is {x}")
    print(f"y is {y}")
    print(f"x + y = {x + y}")
```

```py
# wrong 
def combine(x, y):
    print("x is {0}".format(x))
    print("y is {0}".format(y))
    print("x + y = {0}".format(x + y))
```

### Always use type hinting
Type hinting will make it a lot easier for other people to know what your function take in, and whats it returning.

```py
def add(x: int, y: int) -> int:
    return x + y
```

If your function works with multiple types, put all possible types in there.

```py
def combine(a: int | str, b: int | str) -> str:
    if a is int and b is int:
        return f"{a} + {b} = {a + b}"
    else:
        return f"{a} {b}"
```

### Docstrings
Use docstring to document your functions: https://peps.python.org/pep-0257/

### Use logging instead of print

Using logging statements will make it a whole lot easier to debug when something go wrong.

Only use print statements for something you want the user to see.

```py
import logging

logging.debug("") # for debug messages. I.e, checking output of a function, etc..
logging.info("") # for informational messages. I.e, 'connecting to a datbase...', etc..
logging.warning("") # for when something goes wrong, but the app is still functions normally 
logging.error("") # for when something goes wrong, the app still works, but someone need to check it
logging.critical("") # for when something goes horribly wrong, and the app can not functions
```

### Pep8
Also take a look at [pep8](https://peps.python.org/pep-0008)
