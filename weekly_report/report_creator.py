#!/usr/bin/python
# -*- encoding : utf-8 -*-

import os
import common
import excel_handler as ex
from datetime import date
import const

report_name = os.path.join(const.File.path, const.File.report_name)


def init_report_file():
    for name in const.members:
        file_name = os.path.join(const.File.path, f"{name}.xlsx")
        if not os.path.exists(file_name):
            ex.init_report(file_name)


def merge_content():
    tmp_list = []
    for file_name in const.members:
        tmp_df = ex.read_excel_to_dataframe(os.path.join(const.File.path, f"{file_name}.xlsx"))
        tmp_list.append(tmp_df)
    ex.merge_content(tmp_list).to_excel(report_name)


def create_report():
    init_report_file()
    if common.is_report_day(const.weekday.Sat):
        merge_content()


if __name__ == "__main__":
    create_report()
