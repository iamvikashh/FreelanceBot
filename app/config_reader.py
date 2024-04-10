import os
from dotenv import find_dotenv, load_dotenv
from piccolo.conf.apps import AppRegistry
from piccolo.engine.sqlite import SQLiteEngine
from pydantic_settings import BaseSettings

# Load environment variables from .env file
env_file = find_dotenv(".env")
print("url ", env_file)
load_dotenv(override=True)
# for key, value in os.environ.items():
#     print(f"{key}: {value}")
# with open(env_file, "r") as f:
#     env_content = f.read()
#     print(env_content)
class Settings(BaseSettings):
    piccolo_conf: str = os.getenv('PICCOLO_CONF', 'app.config_reader')
    kw_login: str = os.getenv('KW_LOGIN', '')
    kw_password: str = os.getenv('KW_PASSWORD', '')
    kw_phone_last: str = os.getenv('KW_PHONE_LAST', '')
    kw_categories: str = os.getenv('KW_CATEGORIES', '')
    up_securitytoken: str = os.getenv('UP_SECURITYTOKEN', '')
    up_useruid: str = os.getenv('UP_USERUID', '')
    up_orguid: str = os.getenv('UP_ORGUID', '')
    up_question: str = os.getenv('UP_QUESTION', '')
    up_subcategories: str = os.getenv('UP_SUBCATEGORIES', '')
    tg_token: str = os.getenv('TG_TOKEN', '')
    tg_group: int = int(os.getenv('TG_GROUP', 0))
    tg_group_link: str = os.getenv('TG_GROUP_LINK', '')
    tg_topic_id: int = int(os.getenv('TG_TOPIC_ID', 0))
    tg_admin: int = int(os.getenv('TG_ADMIN', 0))
    bot_username: str = os.getenv('BOT_USERNAME', 'your_bot')

    app_base_url: str = os.getenv('APP_BASE_URL', '')
    app_host: str = os.getenv('APP_HOST', 'localhost')
    app_port: int = int(os.getenv('APP_PORT', 8080))
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

# Ensure the directory for the database exists
db_path = os.path.join("app", "db", "local_db")
os.makedirs(db_path, exist_ok=True)

# Initialize SQLiteEngine with the database path
DB = SQLiteEngine(os.path.join(db_path, 'projects.db'))

# Define the AppRegistry
APP_REGISTRY = AppRegistry(apps=['app.db.piccolo_app'])
