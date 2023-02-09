# COLLECTIONS MODULE

# COLLECTIONS.COUNTER
# COLLECTIONS.NAMEDTUPLE
# COLLECTIONS.ORDEREDDICT
# COLLECTIONS.DEFAULTDICT
# COLLECTIONS.DEQUE

# %%

# COLLECTIONS.COUNTER

from collections import Counter
from typing import OrderedDict

my_string = "aaabbbbbccccdddeeeefghhhhhiij"

my_counter = Counter(my_string)

print(my_counter)
# .keys(), .values(), .items()

print(my_counter.most_common(1))
# returns a list of tuples of most frequent elements

my_iterator = my_counter.elements()
# returns an iterator of all present elements
# iterator.chain object
for i in my_iterator:
    print(i)

# %%

# COLLECTIONS.NAMEDTUPLE

from collections import namedtuple

# gives tuple features with dictionary readability
# kind of like a class/struct

Colour = namedtuple("Colour", ["red", "green", "blue"])

white = Colour(red=255, green=255, blue=255)

# also allows for easy, readable access
print(white.blue)

# %%

# COLLECTIONS.ORDEREDDICT

# just a dictionary that remembers the order in which
# items were added to it

# since Python 3.7, the normal implementation of
# dictionaries has this feature

from collections import OrderedDict

ordered_dict = OrderedDict()

ordered_dict["a"] = 5
ordered_dict["c"] = 15
ordered_dict["b"] = 10

print(ordered_dict)

# %%

# COLLECTIONS.DEFAULTDICT

# same as normal dictionary, except a default value is
# given if the key has not been set yet

from collections import defaultdict

default_dict = defaultdict(int)
# the (int) is the default value

default_dict["a"] = 5
default_dict["c"] = 15

print(default_dict["f"])

# %%

# COLLECTIONS.DEQUE

# deque = double-ended queue

from collections import deque

de_que = deque()
