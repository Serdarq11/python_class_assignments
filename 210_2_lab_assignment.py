def date():
    currentYear = 2023
    currentMonth = 10
    currentDay = 13
    return currentYear, currentMonth, currentDay


def hasBeenAliveDays (yearBorn, monthBorn, dayBorn):
    c_currentYear, c_currentMonth, c_currentDay = date()
    total_days = (c_currentYear - yearBorn) * 365 + (c_currentMonth - monthBorn) * 30 + c_currentDay - dayBorn
    return total_days

def hasBeenAliveHours ():
    c_total_days = hasBeenAliveDays(2001, 9, 15)
    return c_total_days * 24

yearBorn = 2001
monthBorn = 9
dayBorn = 15

result_age_days = str(hasBeenAliveDays(2001, 9, 15))
print('The person has been living for ' + result_age_days + ' days.')

result_age_hours = str(hasBeenAliveHours())
print('The person has been living for ' + result_age_hours + ' hours.')















