from app_store_scraper import AppStore
import pandas as pd
import numpy as np

import json

tiktok = AppStore(country='us', app_name='tiktok', app_id='835599320')

tiktok.review(how_many=1500)

print(tiktok.reviews)