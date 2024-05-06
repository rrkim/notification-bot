from abc import *


class Target(metaclass=ABCMeta):

    def __init__(self):
        self._config = None

    def set_config(self, config):
        self._config = config

    def get_title(self):
        return self._config["title"]

    def get_notifications(self):
        title = self.get_title()

        try:
            return self._retrieve_notifications()
        except Exception as e:
            print(f'[오류] {title} 에서 알림 정보를 가져오는 중에 문제가 발생했습니다.\n오류 메시지: {e}')
            pass

    @abstractmethod
    def _retrieve_notifications(self):
        pass

