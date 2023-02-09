"""
  Author: Enivar
  Date:
"""


import atexit
import heapq
import io
import sys
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import Counter, defaultdict
from ctypes import c_float, c_int, c_int8, c_int16, c_int32, c_int64
from ctypes import c_longlong as ll
from heapq import merge, nlargest, nsmallest
from math import ceil
from sys import exit, stderr, stdin, stdout

buffer = io.BytesIO()
stdout = buffer


copy = lambda array: list(array)
vector = lambda lim, fill: [fill for _ in range(lim)]
inList = lambda: [int(x) for x in input().split()]
Input = lambda: stdin.readline()

# @atexit.register
# def write():
#   sys.__stdout__.write(buffer.getvalue())


def debug(*args):
    for i in args:
        stderr.write(f"{str(i)} ")
    stderr.write("\n")


def Print(*args):
    for i in args:
        stdout.write(f"{str(i)} ")
    stdout.write("\n")


class Solve:
    def __init__(self):
        self.i = 0
        self.max = -(10**19)

    def inp(self, x):
        self.max = max(self.max, x)
        return x


for _ in range(int(Input())):
    n = int(Input())
    # obj = Solve()
    # a = [obj.inp(int(x)) for x in Input().split()]
    # x, , = map(int, Input().split())

# TO GENERATE ALL POSSIBLE SUBSTRINGS IN A STRING
# substrings = (
#     string[first_counter : first_counter + second_counter]
#     for second_counter in range(1, 1 + string_length)
#     for first_counter in range(1 + string_length - second_counter)
# )
