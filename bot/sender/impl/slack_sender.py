from bot.sender.sender import Sender
from bot.utils.request_utility import post_request
from bot.utils.slack_utility import *


class SlackSender(Sender):

    def send_notification(self):
        blocks, block_cnt = self._create_blocks()
        if block_cnt > 0:
            notification_title = get_block_cnt_message(block_cnt)
            notification_object = {"text": notification_title, "blocks": blocks}

            post_request(self._config["url"], notification_object)

    def _create_blocks(self):
        blocks = []
        block_cnt = 0

        for notification in self._notifications:
            title = notification["title"]
            items = notification["items"]

            blocks.append(create_header(title))
            blocks.append(create_divider())

            if items:
                blocks.append(create_bullet_list(items))
                block_cnt += 1
            else:
                no_data_message = get_no_data_message()
                blocks.append(create_section(no_data_message))

        block_cnt_message = get_block_cnt_message(block_cnt)
        blocks.insert(0, create_section(block_cnt_message))
        return blocks, block_cnt

