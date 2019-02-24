import json
import re

from flask import Flask, request

import bot
import config
import utils

app = Flask(__name__)


@app.route('/api/send_message', methods=['POST'])
def send_message():
    token = request.form.get('token', '')
    if token != config.AUTH_TOKEN:
        return json.dumps({'status': 'error', 'msg': 'bad auth token'}), 401
    msg = request.form.get('msg', '')
    groups = re.split(r'\s*,\s*', request.form.get('groups', '').strip())
    for group in groups:
        chat_id = delivery_groups.get(group)
        bot.send_message(chat_id, msg)
    return json.dumps({'status': 'success'}), 200


delivery_groups = utils.load_groups(config.GROUPS_FILENAME)
