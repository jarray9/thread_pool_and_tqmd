#!/user/bin/python
# -*- encoding : utf-8 -*-

from openpyxl import Workbook
from openpyxl.utils import get_column_letter
import openpyxl
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


def read_excel_to_dataframe(file_name, sort_by=const.excel_header[2]):
    try:
        df = pd.read_excel(file_name)
        return df.sort_values(by=[sort_by])
    except FileNotFoundError:
        raise Exception(f"File is not exits :{file_name}")
    except Exception as e:
        raise Exception(f"Unexpected error occurred.{e.args}")


def read_excel_file(file_name):
    try:
        wb = openpyxl.load_workbook(file_name=file_name)
        if const.default_sheet_name in wb.sheetnames:
            return wb[const.default_sheet_name]
        else:
            raise Exception(f"Expected sheet name does not exist. {file_name}")
    except FileNotFoundError:
        raise Exception(f"File is not exits :{file_name}")
    except Exception as e:
        raise Exception(f"Unexpected error occurred.{e.args}")


def merge_content(data_frame_list):
    """
    Concat multiple dataframe into 1
    """
    return pd.concat(data_frame_list)
