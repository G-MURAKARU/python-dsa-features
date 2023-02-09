import logging

import employee

# LOGGING LEVELS

# levels allow us to specify exacly what we want to log by separating them into categories
# there are 5 logging levels:

# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future
# (e.g. ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

# the logging level is set to WARNING by default


# some sample code
def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    try:
        result = x / y
    except ZeroDivisionError:
        # to log the error and the traceback, use .exception() instead of .error()
        # .exception() is only called from an exception handler
        logger.exception("Tried to divide by zero")
    else:
        return result


def create_logger() -> logging.Logger:
    # CUSTOM LOGGER SETTINGS

    # to create a custom logger (avoid using the root logger)
    logger = logging.getLogger(__name__)

    # to set the level of the custom logger
    logger.setLevel(logging.DEBUG)

    # CUSTOM FILE HANDLER SETTINGS

    # to create a formatter for the file handler (not the logger)
    file_formatter = logging.Formatter(
        "%(asctime)s: %(name)s: %(levelname)s: %(message)s"
    )

    # to create a custom file handler for the custom logger
    file_handler = logging.FileHandler("sample_log.log")

    # to add the created formatter to the created file handler
    file_handler.setFormatter(file_formatter)

    # custom loggers allow for flexibility
    # e.g. if the logger's log level is left at DEBUG but only WARNINGs and above are
    # logged in the log file
    file_handler.setLevel(logging.WARNING)

    # custom loggers also allow for multiple handlers with one logger
    # e.g. to create a custom stream handler (to print debug statements
    # to the console instead of logging them in a file)
    stream_handler = logging.StreamHandler()
    stream_formatter = logging.Formatter("%(levelname)s: %(name)s: %(message)s")
    stream_handler.setFormatter(stream_formatter)

    # to add the file handler and stream handler to the custom logger
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger


def main():
    num_1 = 50
    num_2 = 25

    add_result = add(num_1, num_2)
    logger.debug(f"Add: {num_1} + {num_2} = {add_result}")

    sub_result = subtract(num_1, num_2)
    logger.debug(f"Sub: {num_1} - {num_2} = {sub_result}")

    mul_result = multiply(num_1, num_2)
    logger.debug(f"Mul: {num_1} * {num_2} = {mul_result}")

    div_result = divide(num_1, num_2)
    logger.debug(f"Div: {num_1} / {num_2} = {div_result}")


if __name__ == "__main__":
    # initialising a custom logger
    logger: logging.Logger = create_logger()

    main()
