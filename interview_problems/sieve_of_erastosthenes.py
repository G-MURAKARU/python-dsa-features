# used to find prime numbers
import math


def find_primes(limit: int) -> list[int]:
    """
    find_primes finds all prime integers in the closed interval [0, limit]

    Args:
        limit (int): the upper limit of the search

    Returns:
        list[int]: list of prime integers
    """

    # initialises a list of <limit> Trues
    # by default all numbers are assumed prime, the sieve then filters out imposters
    primes = [True] * (limit + 1)

    # setting 0 and 1 to False, they are not primes (base cases)
    primes[0], primes[1] = False, False

    # loop from 2 to the square root of limit, setting their multiples to False
    sqrt_limit = math.ceil(math.sqrt(limit))

    # for numbers in [2, sqrt_limit], eliminate their multiples as they are def not prime
    for number in range(2, sqrt_limit + 1):
        # range begins at number**2 because number's multiples before that are already handled by previous numbers
        for others in range(number**2, limit + 1, number):
            primes[others] = False

    # since the indices of the values in the primes list of boolean represent integers,
    # indices where 'True' is located are prime integers
    for index, value in enumerate(primes):
        if value:
            print(index)


find_primes(169)
