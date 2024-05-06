import datetime


def get_date_object(date_string, format):
    return datetime.datetime.strptime(date_string, format)


def get_date_string(date_object, format):
    return date_object.strftime(format)


def get_today_date():
    return datetime.datetime.now()


def calculate_date(date_object, days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0):
    return date_object + datetime.timedelta(days, seconds, microseconds, milliseconds, minutes, hours, weeks)


def get_week_day_str(date_object):
    day_of_week = date_object.weekday()
    days = ["월", "화", "수", "목", "금", "토", "일"]

    return days[day_of_week]