# -*- encoding : utf-8 -*-

from enum import Enum

report_file_name = r"weekly_report.xlsx"
# excel_header = [r"Ticket_No", r"Task_Title", r"Stats_Description", r"Input_Date", r"Report_Date"]
excel_header = [r"res", r"チケット番号", r"タスク名", r"説明", r"ステータス", r"入力日付"]
excel_content = [r"○", r"1023", r"test_task_name", r"normally processing", r"正常", r"2021-03-03"]
excel_content_2 = [r"", r"1023", r"test_task_name", r"normally processing", r"正常", r"2021-03-03"]

report_sheet_name = r"Report"
default_sheet_name = r"Sheet1"
members = [r"秦", r"任", r"江", r"趙"]


class Weekday(Enum):
    Monday = 0,
    Tuesday = 1,
    Wednesday = 2,
    Thursday = 3,
    Friday = 4,
    Saturday = 5,
    Sunday = 6
