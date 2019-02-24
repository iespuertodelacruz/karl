from prettyconf import config

TELEGRAM_BOT_TOKEN = config('TELEGRAM_BOT_TOKEN')
GROUPS_FILENAME = config('GROUPS_FILENAME', default='groups.dat')
FLASK_APP = config('FLASK_APP')
FLASK_ENV = config('FLASK_ENV')
AUTH_TOKEN = config('AUTH_TOKEN')
