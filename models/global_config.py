
DB_HOST = '65.21.237.252'
DB_PORT = '5432'
DB_NAME = 'mark_bot_db'
DB_USER = 'mark_user'
DB_PASS = 'MAVTFedDX3'


SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
ASYNC_SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

TELEGRAM_BOT_TOKEN = '****'   #vpn_for_yutube_bot
TELEGRAM_PAYMENT_TOKEN = '*********:LIVE:*****'

YOOKASSA_SECRET_KEY = 'live_****************************************'
YOOKASSA_SHOP_ID = '******'


SENTRY_BACKEND = "https://29bc8bec5c0c4694a389ae5c330d27f5@sentry.digitalberd.com/8"


