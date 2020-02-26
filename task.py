import math
import datetime


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


def timeBetween(date1, date2):
    x = datetime.date(date1[0], date1[1], date1[2])
    y = datetime.date(date2[0], date2[1], date2[2])
    results = x - y
    return results
