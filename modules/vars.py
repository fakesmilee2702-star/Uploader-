#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "11351636"))
API_HASH = environ.get("API_HASH", "4618bcb290722995b7073087de8b2737")
BOT_TOKEN = environ.get("BOT_TOKEN", "8226802740:AAFpv1k8IdkYUrCufMgKu2OwhwcLcPf85sc")

OWNER = int(environ.get("OWNER", "8412760331"))
CREDIT = environ.get("CREDIT", "ABHISHEK")
cookies_file_path = os.getenv("cookies_file_path", "youtube_cookies.txt")

TOTAL_USER = os.environ.get('TOTAL_USERS', '8412760331,6233692970').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '8412760331,6233692970').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))

