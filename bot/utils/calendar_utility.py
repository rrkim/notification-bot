import requests
import icalendar
import recurring_ical_events
from bot.utils.date_utility import get_today_date, calculate_date, get_date_object, get_date_string, get_week_day_str
from bot.utils.request_utility import get_content_from_request


def get_calendar_schedule_term(icalendar_url: str, before_days: int, after_days: int):
    new_date_format = "%Y-%m-%d"

    today_date = get_today_date()
    date1 = calculate_date(today_date, -after_days)
    date2 = calculate_date(today_date, before_days+1)

    ical_string = get_content_from_request(icalendar_url, {})
    calendar = icalendar.Calendar.from_ical(ical_string)
    events = recurring_ical_events.of(calendar).between((date1.year, date1.month, date1.day), (date2.year, date2.month, date2.day))
    schedules = sorted( list(map(lambda x: get_event_info(x, new_date_format), events)), key=lambda x: x[0])
    schedules = list(map(lambda x: x[1], schedules))

    return schedules


def get_event_info(event, date_format):
    origin_date_format = "%Y%m%d"
    schedule_name = event.get("SUMMARY")
    start_date = event.get("DTSTART").to_ical().decode("utf8")[:8]
    end_date = event.get("DTEND").to_ical().decode("utf8")[:8]

    start_date_object = get_date_object(start_date, origin_date_format).date()
    end_date_object = get_date_object(end_date, origin_date_format).date()

    reformat_start_date = get_date_string(start_date_object, date_format)
    reformat_end_date = get_date_string(end_date_object, date_format)
    start_weekday = get_week_day_str(start_date_object)
    end_weekday = get_week_day_str(end_date_object)

    schedule_text = f"{schedule_name} - {reformat_start_date} ({start_weekday}) ~ {reformat_end_date} ({end_weekday})"
    if reformat_start_date == reformat_end_date:
        schedule_text = f"{schedule_name} - {reformat_end_date} ({end_weekday})"

    return (reformat_start_date, schedule_text)

