#!/usr/bin/python
# -*- encoding : utf-8 -*-

import os
import const
from openpyxl import Workbook
from openpyxl import worksheet


def add_sheet(wb: Workbook, name: str):
    work_sheet = wb.create_sheet(name)
    work_sheet.append(const.excel_header)


def init_report():
    wb = Workbook()
    sheet1 = wb.active
    sheet1.title = const.report_sheet_name
    for name in const.members:
        add_sheet(wb, name)
    wb.save(filename=const.report_file_name)


if not os.path.exists(const.report_file_name):
    init_report()