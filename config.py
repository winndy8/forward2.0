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
    SESSION = os.environ.get("SESSION", "BQGDMIkAAGV9w3L6fKhpL9D0uOBVE_SyHJwBvn1mLpBxTAzVxptEz4Ah-H8VIextUZZL0tpnZ8BFdBLYK5UPK-mOKAREBvkob-QyAaL4PR9AxhtzOjJpzK5_HoejbSFDHYNNxVB2slcAvvZUK2hw58ekIXOyoivSFcJZdoPRWhh10f5rKT59tWi2etv_OZ9XuhPIoVzs5fkZhwzzm_ILOlYWzF-iIR4tdponznGjgdUGegnVO8ZOMFqXRd4l609346aGReU1OmjO0cQl4fBmLxbhrLwiDbwZcFLBxUh2HQUleX5Nxo9ltTWb1V-1z0L3WL6540Sc0JUoQYmGJS5pVfzNzlYwAAAAFUPt0PAA")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001676349938"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "wadefrtbot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
