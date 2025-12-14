# readrides.py

import csv
from dataclasses import dataclass
from collections import namedtuple


def read_rides_as_tuples(filename):
    """
    Read the bus ride data as a list of tuples
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records


def read_rides_as_dictionaries(filename):
    """
    Read the bus ride data as a list of dictionaries.
    """
    records = []
    with open(filename) as f:
        _ = f.readline()
        for line in f:
            data = line.split(",")
            route = data[0]
            date = data[1]
            daytype = data[2]
            rides = int(data[3])
            record = {"route": route, "date": date, "daytype": daytype, "rides": rides}
            records.append(record)
    return records


@dataclass
class RowDataClass:
    route: str
    date: str
    daytype: str
    rides: int


class Row:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


def read_rides_as_class(filename):
    """
    Read the bus ride data as a list of classes.
    """
    records = []
    with open(filename) as f:
        _ = f.readline()
        for line in f:
            data = line.split(",")
            route = data[0]
            date = data[1]
            daytype = data[2]
            rides = int(data[3])
            row = Row(route, date, daytype, rides)
            records.append(row)
    return records


class RowSlots:
    __slots__ = ("route", "date", "daytype", "rides")

    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


def read_rides_as_slots_class(filename):
    """
    Read the bus ride data as a list of classes.
    """
    records = []
    with open(filename) as f:
        _ = f.readline()
        for line in f:
            data = line.split(",")
            route = data[0]
            date = data[1]
            daytype = data[2]
            rides = int(data[3])
            row = RowSlots(route, date, daytype, rides)
            records.append(row)
    return records


def read_rides_as_data_class(filename):
    """
    Read the bus ride data as a list of data classes.
    """
    records = []
    with open(filename) as f:
        _ = f.readline()
        for line in f:
            data = line.split(",")
            route = data[0]
            date = data[1]
            daytype = data[2]
            rides = int(data[3])
            row = RowDataClass(route, date, daytype, rides)
            records.append(row)
    return records


RowNamedTuple = namedtuple("RowNamedTuple", ["rouse", "date", "daytype", "rides"])


def read_rides_as_named_tuple(filename):
    """
    Read the bus ride data as list of named tuples.
    """
    records = []
    with open(filename) as f:
        _ = f.readline()
        for line in f:
            data = line.split(",")
            route = data[0]
            date = data[1]
            daytype = data[2]
            rides = int(data[3])
            row = RowNamedTuple(route, date, daytype, rides)
            records.append(row)
    return records


if __name__ == "__main__":
    import tracemalloc

    tracemalloc.start()
    rows = read_rides_as_slots_class("../../Data/ctabus.csv")
    print("Memory Use: Current %d, Peak %d" % tracemalloc.get_traced_memory())


"""
some insights: 
    Data class and Class really don't make any difference in terms of memory usage
    Dictionaries take up more space than classes, presumably, because all keys need to be stored as strings.
    Named tuples take up less comparatively.
    Using a class with slots takes up the least amount of memory, but only slightly less than the named tuples.
    The choice made here comes with advantages and drawbacks however, namely flexibility with named tuples and slots.
"""
