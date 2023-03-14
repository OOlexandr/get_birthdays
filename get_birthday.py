import datetime
import calendar

def get_birthdays_per_week(users):
    today = datetime.date.today()
    this_week_b_days = {}

    for user in users:
        b_day = user["birthday"]
        if b_day.month == 1 and today.month == 12:
            #handles case when the birthday might be this week but next year
            b_day = b_day.replace(today.year+1)
        else:
            b_day = b_day.replace(today.year)
        
        if b_day.weekday() >= today.weekday() and b_day.weekday() <= 6 \
        and b_day.isocalendar()[1] == today.isocalendar()[1]:
            if not b_day.strftime("%A") in this_week_b_days:
                this_week_b_days[b_day.weekday()] = [user["name"]]
            else:
                this_week_b_days[b_day.weekday()].append(user["name"])
    
    b_days = list(this_week_b_days.keys())
    b_days.sort()
    for day in b_days:
        message = calendar.day_name[day] + ':'
        for name in this_week_b_days[day]:
            message += ' ' + name +','
        print(message[:len(message)-1])#printing without last coma.
