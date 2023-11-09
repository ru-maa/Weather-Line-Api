import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), 'api.env')
load_dotenv(dotenv_path)

# 環境変数の値をAPに代入
AP = os.environ.get("API_KEY") 
TOKEN = os.environ.get("LINE_TOKEN")