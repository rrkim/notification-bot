import json
from bot.notification_bot import NotificationBot


def lambda_handler(event, context):
    __CONFIG_YAML = "bot/config.yml"

    notification_bot = NotificationBot(__CONFIG_YAML)
    notification_bot.send_notification()

    return {
        'statusCode': 200,
        'body': json.dumps('Success!')
    }
