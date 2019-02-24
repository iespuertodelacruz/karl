import json

from flask import Flask, request

import bot
import config
import re
import utils

app = Flask(__name__)


@app.route('/api/send_message', methods=['POST'])
def send_message():
    msg = request.form.get('msg', '')
    groups = re.split(r'\s*,\s*', request.form.get('groups', '').strip())
    for group in groups:
        chat_id = delivery_groups.get(group)
        print(chat_id)
        bot.send_message(chat_id, msg)
    return json.dumps({'status': 'ok'})


delivery_groups = utils.load_groups(config.GROUPS_FILENAME)
