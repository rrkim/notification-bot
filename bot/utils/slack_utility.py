def get_block_cnt_message(block_cnt):
    return f"{block_cnt}건의 알림이 있습니다."


def get_no_data_message():
    return "새로운 정보가 없습니다."


def create_divider():
    return {"type": "divider"}


def create_header(message: str):
    return {"type": "header", "text": {"type": "plain_text", "text": message}}


def create_bullet_list(items):
    elements = []
    for item in items:
        elements.append({"type": "rich_text_section", "elements": [{"type": "text", "text": item}]})

    section = {"type": "rich_text",
               "elements": [{"type": "rich_text_list", "style": "bullet", "elements": elements}]}
    return section


def create_section(message: str):
    return {"type": "section", "text": {"type": "mrkdwn", "text": message}}
