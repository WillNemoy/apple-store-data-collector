
from pprint import pprint
import json
import datetime

import requests
import pandas as pd
import numpy as np

from openpyxl import Workbook, load_workbook

def appleAPI(appId):

    page = 1
    apple_request = ("https://itunes.apple.com/us/rss/customerreviews/page="
                     + str(page)
                     + "/id="
                     + appId
                     + "/sortBy=mostHelpful/json")

    apple_Json = requests.get(apple_request).json()
    
    return apple_Json


#run the function

pprint(appleAPI("324684580"))