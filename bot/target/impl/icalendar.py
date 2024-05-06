from bot.target.target import Target
from bot.utils.calendar_utility import get_calendar_schedule_term


class CalendarTarget(Target):

    def _retrieve_notifications(self):
        return get_calendar_schedule_term(self._config["url"], self._config["before_days"], self._config["after_days"])

