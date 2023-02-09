# %%
# FIRST-CLASS FUNCTIONS
# functions that can be treated like any other python
# object e.g.:

# can be treated as variables
def square(x):
    return x * x


f = square  # here
print(f(5))

# can be passed as arguments to functions
def my_map(func, arg_list):
    return [func(x) for x in arg_list]


squares_list = my_map(square, [1, 2, 3, 4, 5])  # here
print(squares_list)

# can be returned by functions
def html_tag(tag):
    def wrap_text(msg):
        # note: does not take 'tag' as an arg
        print(f"<{tag}><{msg}></{tag}>")

    return wrap_text  # here


heading1 = html_tag("h1")  # here
print(heading1("This is a heading!"))

# a closure is an inner function that has access to
# free variables defined in its local scope, even after
# execution of the outer function is complete, heading1
# in this case accessing "h1"

# note: my_map and html_tag are acting as higher-order
# functions in this example

# %%

# DECORATORS
# decorators work similarly to first-class functions
# and closures, taking in a function as an argument
# adding some functionality then returning another
# function
# it does not alter the source code of the initial
# function

# example:
def decorator_function(original_function):
    def wrapper_function():
        # alter functionality without altering display()'s
        # source code
        print(f"This ran before {original_function.__name__}")
        return original_function()

    return wrapper_function


def display():
    print("display function ran")


decorated_display = decorator_function(display)
decorated_display()

# alternatively:
@decorator_function
def display():
    print("display function ran")


# does 'display = decorator_function(display)' in bkgd
display()


# %%

# DECORATORS CONTINUATION

# the above implementation cannot take input arguments,
# therefore it is prudent to define the wrapper_function
# to take in an arbitrary number of positional and
# keyword arguments


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        return original_function(*args, **kwargs)

    return wrapper_function


@decorator_function
def display_info(name, age):
    print(f"{name} is {age} years old.")


display_info("Gicheru", 23)

# %%

# DECORATORS CONTINUATION

# using classes as decorators instead of functions


class Decorator_Class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print(f"Call ran before {self.original_function.__name__}")
        return self.original_function(*args, **kwargs)


@Decorator_Class
def display_info(name, age):
    print(f"{name} is {age} years old.")


display_info("Gicheru", 23)

# %%

# DECORATORS CONTINUATION

# practical use case - logging
# e.g. checking how many times a function is ran and what
# arguments were passed to that function

# decorators make code cleaner by allowing us to write
# some functionality in one area of our code base, then
# apply it anywhere we need to in our code


def my_logger(original_function):
    import logging

    logging.basicConfig(
        filename=f"{original_function.__name__}.log", level=logging.INFO
    )

    def wrapper(*args, **kwargs):
        logging.info(f"Ran with args: {args} and kwargs: {kwargs}.")
        return original_function(*args, **kwargs)

    return wrapper


@my_logger
def display_info(name, age):
    print(f"{name} is {age} years old.")


display_info("Gicheru", 23)

# %%

# DECORATORS CONTINUATION

# practical use case - timing function runtime


def my_timer(original_function):
    import time

    def wrapper(*args, **kwargs):
        time1 = time.perf_counter()
        result = original_function(*args, **kwargs)
        time2 = time.perf_counter() - time1
        print(f"{original_function.__name__} ran in {time2} seconds.")
        return result

    return wrapper


@my_timer
def display_info(name, age):
    print(f"{name} is {age} years old.")


display_info("Gicheru", 23)

# %%

# DECORATORS CONTINUATION

# chaining multiple decorators
from functools import wraps


def my_logger(original_function):
    import logging

    logging.basicConfig(
        filename=f"{original_function.__name__}.log", level=logging.INFO
    )

    @wraps(original_function)  # here
    def wrapper(*args, **kwargs):
        logging.info(
            f"{original_function.__name__} ran with args: {args} and kwargs: {kwargs}."
        )
        return original_function(*args, **kwargs)

    return wrapper


def my_timer(original_function):
    import time

    @wraps(original_function)  # here
    def wrapper(*args, **kwargs):
        time1 = time.perf_counter()
        result = original_function(*args, **kwargs)
        time2 = time.perf_counter() - time1
        print(f"{original_function.__name__} ran in {time2} seconds.")
        return result

    return wrapper


# chaining
@my_logger
@my_timer
def display_info(name, age):
    print(f"display_info ran with args: ({name}, {age})")


# does 'display_info = my_logger(my_timer(display_info))
# in the bkgd
display_info("Maina", 17)
