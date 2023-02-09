# %%

# ITERATORS
# these give us the ability to iterate through a
# container without actually storing the data values in
# memory

# e.g. the map() function is an iterator, it creates an
# iterable object
x = map(lambda i: i**2, list(range(1, 11)))
print(f"This is what the created x actually is: {x}")
# print(list(x))

# what a for loop does is it calls the next() function
# on the iterator, e.g. (observe output):
print(next(x))
print(x.__next__())
# the first 3 values in x will not be repeated in the
# output of the for loop below

# for a in x:
#     print(a)

# for loop fleshed out:
while True:
    try:
        value = next(x)
        print(value)
    except StopIteration:
        print("Done")
        break

# %%

# ITERATORS CONTINUED

# iter() function: returns an iterator from an object
# example: range() function
x = range(1, 11)
x = iter(x)
print(x)

while True:
    try:
        value = next(x)
        print(value)
    except StopIteration:
        print("Done")
        break

# %%

# ITERATORS CONTINUED

# creating your own iterator: legacy method
class MyIterator:
    def __init__(self, n) -> None:
        self.n = n

    def __iter__(self):
        self.current = -1
        return self

    def __next__(self):
        if self.current >= self.n:
            raise StopIteration
        self.current += 1
        return self.current


iterator = MyIterator(10)
for i in iterator:
    print(i)

# %%

# ITERATORS CONTINUED

# creating a generator using the yield keyword


def gen(n):
    # for i in range(1, n):
    #     yield i
    yield from range(1, n)


my_gen = gen(11)
print(my_gen)
for i in my_gen:
    print(i)

# %%

# ITERATORS CONTINUED

# creating a generator using generator comprehension
# my_gen = (i for i in range(11))
my_gen = iter(range(11))
for x in my_gen:
    print(x)
