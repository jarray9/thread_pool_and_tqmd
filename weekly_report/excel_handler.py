#!/user/bin/python
# -*- encoding : utf-8 -*-

from openpyxl import Workbook
from openpyxl.utils import get_column_letter
import const
import pandas as pd

pf = pd.DataFrame()
for name in const.members:
    pf.append(pd.read_excel(f"{name}.xlsx"))


def init_report(file_name: str):
    wb = Workbook()
    sheet = wb.active
    sheet.append(const.excel_header)
    for x in range(10):
        if x % 2 == 0:
            sheet.append(const.excel_content)
        else:
            sheet.append(const.excel_content_2)
    wb.save(filename=file_name)

