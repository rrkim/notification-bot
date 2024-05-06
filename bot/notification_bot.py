from bot.target.impl.icalendar import CalendarTarget
from bot.target.impl.weather import WeatherTarget
from bot.sender.impl.slack_sender import SlackSender
import yaml


class NotificationBot:

    def __init__(self, config_file_path):
        with open(config_file_path, 'r') as f:
            self.__config = yaml.safe_load(f)

    def send_notification(self):
        targets = self._create_instances_from_config("target")
        receivers = self._create_instances_from_config("receiver")
        notifications = []

        for target in targets:
            notification = {"title": target.get_title(), "items": target.get_notifications()}
            notifications.append(notification)

        for receiver in receivers:
            receiver.set_notifications(notifications)
            receiver.send_notification()

    def _create_instances_from_config(self, category):
        instances = []
        for item_key, item_value in self.__config[category].items():
            if not item_value.get("enable", False):
                continue

            instance = NotificationBot._create_instance_by_type(item_value)
            instances.append(instance)
        return instances

    @staticmethod
    def _create_instance_by_type(config):
        type = config["type"]
        if type == "icalendar":
            instance = CalendarTarget()
        elif type == "weather":
            instance = WeatherTarget()
        elif type == "slack":
            instance = SlackSender()
        else:
            print(type)
            raise Exception("정의되지 않은 유형입니다.")

        instance.set_config(config)
        return instance

    def __get_config(self, category, key):
        return self.__config[category][key]