import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), verbose=True)


class Config:
    JWT_SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"