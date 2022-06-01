import requests
import pandas as pd
import json
from dotenv import load_dotenv
import os

load_dotenv()
# API_KEY = "AIzaSyCsnDbgMhTgCuh6B0z5CLTbSuSgLYLD3YE"
API_KEY = (os.getenv('API_KEY'))

channelID = "UCCezIgC97PvUuR4_gbFUs5g"

param = {'key' : API_KEY, 'channelID' : channelID, 'part' : 'snippet'}
response = requests.get("https://www.googleapis.com/youtube/v3/search", params=param)
print(response.json())