import config
import telegram


def send_message(chat_id, msg):
    bot = telegram.Bot(token=config.TELEGRAM_BOT_TOKEN)
    bot.send_message(
        chat_id=chat_id,
        text=msg,
        parse_mode=telegram.ParseMode.MARKDOWN
    )
