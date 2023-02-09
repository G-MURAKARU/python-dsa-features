# %%

# MODULE USED ON ITERATORS AND ITERABLES
import itertools

# ITERTOOLS.COUNT
# ITERTOOLS.ZIP_LONGEST
# ITERTOOLS.CYCLE
# ITERTOOLS.REPEAT
# ITERTOOLS.STARMAP
# ITERTOOLS.COMBINATIONS
# ITERTOOLS.PERMUTATIONS
# ITERTOOLS.PRODUCT
# ITERTOOLS.CHAIN
# ITERTOOLS.ISLICE
# ITERTOOLS.COMPRESS
# ITERTOOLS.FILTERFALSE
# ITERTOOLS.DROPWHILE
# ITERTOOLS.TAKEWHILE
# ITERTOOLS.ACCUMULATE
# ITERTOOLS.GROUPBY
# ITERTOOLS.TEE

# %%

# ITERTOOLS.COUNT
# it iteratively counts infinitely, unless we define
# a point to stop (implicit or explicit)

counter = itertools.count()

# example: giving indices to values
data = [100, 200, 300, 400, 500, 600, 700]
daily_data = list(zip(counter, data))
print(daily_data)

# can define a start point and step

# %%

# ITERTOOLS.ZIP_LONGEST

# works like zip(), except it stops when the longest
# iterable is exhausted instead of the shortest
# it pairs the excess with "None"

print(list(itertools.zip_longest(range(10), data)))

# %%

# ITERTOOLS.CYCLE

# takes an iterable and cycles through it indefinitely
cycler = itertools.cycle([1, 2, 3])
print(next(cycler))
print(next(cycler))
print(next(cycler))
print(next(cycler))
print(next(cycler))
print(next(cycler))

# %%

# ITERTOOLS.REPEAT

# takes a value then repeats it infinitely
repeater = itertools.repeat(2, times=3)
# times limits repetition
for i in repeater:
    print(i)

# application: finding the squares of numbers
squares = list(map(pow, range(1, 11), itertools.repeat(2)))
print(squares)
# function passes the current value from range() and a 2
# to the pow function on each iteration, until the
# shortest iterable is exhausted

# %%

# ITERTOOLS.STARMAP

# unlike map() above, takes tuple-paired arguments
print(list(itertools.starmap(pow, [(2, 2), (3, 2), (4, 2)])))

# %%

# ITERTOOLS.COMBINATIONS
# ITERTOOLS.PERMUTATIONS
# ITERTOOLS.PRODUCT

# used to obtain all the different ways in which a number
# of values in a given set can be combined

# combinations - order does not matter ((a, b) == (b, a))
# permutations - order matters ((a, b) != (b, a))
# product - allows repeats

letters = ["a", "b", "c", "d"]
numbers = [1, 2, 3, 4]
names = ["Gich", "Andrew", "Shawn"]

result1 = itertools.combinations(letters, 2)
result2 = itertools.permutations(names, 2)
result3 = itertools.product(numbers, repeat=2)
# allows combinations with repeats, similar to above
result4 = itertools.combinations_with_replacement(numbers, 2)

for item1 in result1:
    print(item1)

for item2 in result2:
    print(item2)

for item3 in result3:
    print(item3)

# %%

# ITERTOOLS.CHAIN

# allows us to chain iterables to loop through
# all of them at once

letters = ["a", "b", "c", "d"]
numbers = [1, 2, 3, 4]
names = ["Gich", "Andrew", "Shawn"]

combined = itertools.chain(letters, numbers, names)

for i in combined:
    print(i)

# %%

# ITERTOOLS.ISLICE

# allows us to pick a slice of an iterator
# like list slicing

result = itertools.islice(range(11), 1, 9, 2)

for i in result:
    print(i)

# can be used to extract snippets of really long iterators
# instead of committing the whole thing to memory
# example:

with open("filename", "r") as f:  # context manager
    first_lines = itertools.islice(f, 3)

    for i in first_lines:
        print(i)

# %%

# ITERTOOLS.COMPRESS

# used for filtering data following some criteria

people = ["Gicheru", "Shawn", "Andrew", "Kamara"]
male = [True, True, True, False]

result = itertools.compress(people, male)

for i in result:
    print(i)

other_result = filter(lambda x: x < 4, numbers)

for j in other_result:
    # print(j)
    pass

# ITERTOOLS.FILTERFALSE

# returns values that return False instead of True
other_other_result = itertools.filterfalse(lambda x: x < 4, numbers)

for k in other_other_result:
    print(k)

# %%

# ITERTOOLS.DROPWHILE
# ITERTOOLS.TAKEWHILE

# these stop filtering once a function returns False
# takewhile - takes what was looped through, drops rest
# dropwhile - opposite of takewhile

some_numbers = [1, 2, 3, 4, 3, 2, 1]

takewhile = itertools.takewhile(lambda x: x < 4, some_numbers)
dropwhile = itertools.dropwhile(lambda x: x < 4, some_numbers)

print("takewhile:")
for i in takewhile:
    print(i)

print("dropwhile:")
for j in dropwhile:
    print(j)

# %%

# ITERTOOLS.ACCUMULATE

# returns accumulated operations while looping through
# an iterable
# uses addition by default, can use other operations

some_numbers = [1, 2, 3, 4, 3, 2, 1]
their_sum = itertools.accumulate(some_numbers)

print("sum:")
for i in their_sum:
    print(i)

import operator

their_product = itertools.accumulate(some_numbers, operator.mul)

print("product:")
for i in their_product:
    print(i)

# %%

# ITERTOOLS.GROUPBY

# runs through an iterator/iterable, grouping items
# according to some key
# returns tuples of grouped data

# groupby() assumes the iterable is SORTED!

people = [
    {"name": "John Doe", "city": "Gotham", "state": "NY"},
    {"name": "Jane Doe", "city": "Kings Landing", "state": "NY"},
    {"name": "Corey Schafer", "city": "Boulder", "state": "CO"},
    {"name": "Al Einstein", "city": "Denver", "state": "CO"},
    {"name": "John Henry", "city": "Hinton", "state": "WV"},
    {"name": "Randy Moss", "city": "Rand", "state": "WV"},
    {"name": "Nicole K", "city": "Asheville", "state": "NC"},
    {"name": "Jim Doe", "city": "Charlotte", "state": "NC"},
    {"name": "Jane Taylor", "city": "Faketown", "state": "NC"},
]

person_group = itertools.groupby(people, lambda x: x["state"])

for key, group in person_group:
    print(key)
    for person in group:
        print(person, end="\n")
    print()

# ITERTOOLS.TEE

# used to replicate iterators/iterables

copy1, copy2 = itertools.tee(person_group)
# DO NOT USE THE ORIGINAL ITERATOR AFTER COPYING
# i.e. use the copies, not person_group

# %%
