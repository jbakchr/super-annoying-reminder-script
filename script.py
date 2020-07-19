import time
import os
import datetime
import pyautogui


today = str(datetime.date.today())
last_run = open(
    "./last-run.txt", "r").read()

if today != last_run:
    answer = pyautogui.confirm(
        "Har du husket at .. ?", "Reminder!", buttons=['Ja', 'Nej'])
    if answer == "Ja":
        f = open(
            "./last-run.txt", "w")
        f.write(str(datetime.date.today()))
