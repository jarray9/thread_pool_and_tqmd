#!/user/bin/python
# -*- encoding : utf-8 -*-

from openpyxl import Workbook
from openpyxl.utils import get_column_letter
import const

wb = Workbook()

dest_file_name = "weekly_report.xlsx"

header = [r"Ticket_No", r"Task_Title", r"Stats_Description", r"Input_Date"]

ws1 = wb.active
ws1.title = const.member_qin
ws1.append(header)

ws2 = wb.create_sheet(title=const.member_ren)
ws2.append(header)

ws3 = wb.create_sheet(title=const.member_jiang)
ws3.append(header)

wb.save(filename=dest_file_name)


