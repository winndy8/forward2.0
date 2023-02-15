import os
import logging
class Config:
    
    API_ID = int(os.environ.get("API_ID", "25374857"))
    API_HASH = os.environ.get("API_HASH", "8dbe7ae242089f75162fbd3c4ddeb381")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6283718959:AAEV7j00OCFVa19qyQXHhxfiQI7Wc7d4l8U") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "") 
    OWNER_ID = os.environ.get("OWNER_ID", "5708373263")
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://clone:clone@cluster0.go11yez.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Forward_Files')
    SESSION = os.environ.get("SESSION", "")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001676349938"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "wadefrtbot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
