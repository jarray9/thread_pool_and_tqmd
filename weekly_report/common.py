#!/usr/bin/python
# -*- encoding : utf-8 -*-

from datetime import datetime
from datetime import date
from datetime import timedelta
from const import weekday


def get_weekday(date_str):
    return trans_to_date(date_str).weekday()


def trans_to_date(date_str: str):
    new_str = date_str.translate(date_str.maketrans("", "", "-/"))
    if len(new_str) != 8 or not new_str.isnumeric():
        raise Exception(f"Wrong input {date_str}")
    return datetime.strptime(new_str, "%Y%m%d").date()


def get_day_of_week(day=weekday.Wed):
    """Get a day of a week return a datetime.date.
    ex. When want Friday plz input 4
    Default is Wednesday"""
    offset = date.today().weekday().numerator - day.value
    return date.today() + timedelta(offset)


def is_report_day(wd=weekday.Wed.value):
    return date.today() == get_day_of_week(wd)
