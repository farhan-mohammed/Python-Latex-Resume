from datetime import datetime
from enum import Enum


class DateDisplay(Enum):
    MONYEAR = 1


class Duration:
    def __init__(self, startDate, endDate):
        a = datetime(startDate[0], startDate[1], 1)
        b = datetime(endDate[0], endDate[1], 1)
        self.startDate = min(a, b)
        self.endDate = max(a, b)
        self.display = DateDisplay.MONYEAR

    @staticmethod
    def dateToString(date: datetime, type: DateDisplay = DateDisplay.MONYEAR) -> str:
        if type == DateDisplay.MONYEAR:
            return date.strftime("%b %Y").title()
        return str(date)

    def toString(self):
        return [self.dateToString(self.startDate), self.dateToString(self.endDate)]


class Link:
    def __init__(self, link: str, name: str = ""):
        self.link = link
        if name == "":
            self.name = link
        else:
            self.name = name


def existsNonEmpty(data, key: str):
    return key in data and data[key] != ""


def existsNonEmptyArr(data, key: str):
    return key in data and data[key] != []


def existsNonEmptyObj(data, key: str):
    return key in data and data[key] != {}
