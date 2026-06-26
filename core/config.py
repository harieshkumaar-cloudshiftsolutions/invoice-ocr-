import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # JWT Configuration
    SECRET_KEY = os.getenv("SECRET_KEY", "change_this_secret_key")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

settings = Settings()