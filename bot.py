import config
import telegram
import re


def send_message(chat_id, msg):
    bot = telegram.Bot(token=config.TELEGRAM_BOT_TOKEN)
    bot.send_message(
        chat_id=chat_id,
        text=msg,
        parse_mode=telegram.ParseMode.MARKDOWN
    )


def load_groups(filepath):
    groups = []
    with open(filepath) as f:
        for line in f.readlines():
            r = re.match(r'\s*(\S+)\s*=\s*(\S+)', line.strip())
            if r:
                groups.append(r.groups())
    return dict(groups)


print(load_groups(config.GROUPS_FILENAME))
