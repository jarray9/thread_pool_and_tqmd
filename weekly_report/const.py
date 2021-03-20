# -*- encoding : utf-8 -*-

import os
from enum import Enum

members = [r"秦", r"任", r"趙"]
weekday = Enum('week', ('Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun'), start=0)
status_ok = "〇"
status_done = r"完了"


class File(object):
    report_name = r"weekly_report.xlsx"
    sheet_name = r"report"
    path = os.getcwd()
    header = [r"res", r"チケット番号", r"タスク名", r"説明", r"ステータス", r"入力日付"]
    content1 = [r"○", r"1023", r"test_task_name", r"normally processing", r"正常", r"2021-03-03"]
    content2 = [r"", r"1023", r"test_task_name", r"normally processing", r"正常", r"2021-03-03"]


