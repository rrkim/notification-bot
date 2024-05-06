from bot.notification_bot import NotificationBot

if __name__ == '__main__':
    __CONFIG_YAML = "bot/config.yml"

    notification_bot = NotificationBot(__CONFIG_YAML)
    notification_bot.send_notification()