#!/usr/bin/python
# -*- encoding : utf-8 -*-

import os
import const
import common
import excel_handler as ex
from datetime import date


def init_report_file():
    for name in const.members:
        file_name = os.path.join(const.file_path, f"{name}".xlsx)
        if not os.path.exists(file_name):
            ex.init_report(file_name)


def create_report():
    init_report_file()
    if common.is_report_day(const.Weekday.Wednesday):
        pass


if __name__ == "main":
    create_report()