import os
from dotenv import load_dotenv
from exif import Image

load_dotenv()

API_KEY = os.getenv('TOKEN')
