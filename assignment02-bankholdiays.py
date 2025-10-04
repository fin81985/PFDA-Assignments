# Bank holidays in the northern Ireland
# Author: Finian Doonan

import datetime

def get_bank_holidays(year):
    # List of fixed-date bank holidays in Northern Ireland
    bank_holidays = [
        datetime.date(year, 1, 1),   # New Year's Day
        datetime.date(year, 3, 17),  # St. Patrick's Day
        datetime.date(year, 4, 17),  # Easter Monday
        datetime.date(year, 5, 1),   # May Day
        datetime.date(year, 7, 12),  # Orangemen's Day
        datetime.date(year, 8, 28),  # Late Summer Bank Holiday
        datetime.date(year, 12, 25), # Christmas Day
        datetime.date(year, 12, 26), # Boxing Day
    ]
    return bank_holidays
def is_bank_holiday(date):
    bank_holidays = get_bank_holidays(date.year)
    return date in bank_holidays 

print("Bank holidays in Northern Ireland for 2025:")
for holiday in get_bank_holidays(2025):
    print(holiday.strftime("%d-%m-%y"))