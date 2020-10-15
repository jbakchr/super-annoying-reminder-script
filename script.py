import sys
import datetime
import pyautogui


def get_last_script_run_date():
    with open("./last-run.txt", "r") as file:
        return file.read()


def check_for_reminder(today, last_run, args):
    if today != last_run:
        answer = pyautogui.confirm(
            f"Har du husket at {args} ?", "Reminder!", buttons=['Ja', 'Nej'])
        if answer == "Ja":
            with open("./last-run.txt", "w") as file:
                file.write(str(datetime.date.today()))


# Get present date
today = str(datetime.date.today())

# Get date for when script was last run
last_run = get_last_script_run_date()

# Check for reminder
check_for_reminder(today, last_run, sys.argv[1])
