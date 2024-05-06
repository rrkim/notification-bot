from abc import *


class Sender(metaclass=ABCMeta):

    def __init__(self):
        self._notifications = None
        self._config = None

    def set_config(self, config):
        self._config = config

    def set_notifications(self, notifications):
        self._notifications = notifications

    @abstractmethod
    def send_notification(self):
        pass