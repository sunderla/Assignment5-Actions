import math


def firstrun():
    return "success"


def circleArea(radius):
    pi = math.pi
    area = pi * (radius * radius)
    return area


def firstLast(l):
    first = l[0]
    last = l[-1]
    return first, last
