
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

    """
    for review in apple_Json["feed"]["entry"]:
        print(str(review).encode("utf-8"))
        print()
    """

    df = pd.DataFrame(apple_Json["feed"]["entry"])
    df.to_csv("apple store reviews.csv")
    
    return df


#run the function
appleAPI("324684580")
##print(appleAPI("324684580"))
##print(str(appleAPI("324684580")).encode("utf-8"))



##!check up on this later to ensure all info is saved!
    #apple_Json_string = json.dumps(apple_Json, ensure_ascii=False).encode('utf8').decode()
"""
 def clean_text(x):
    
        new_text = ""

        for character in x:
            if (character.isalnum() == True 
                or character == " "
                or character == "'"
                or character == "#"
                or character == "-"
                or character == "("
                or character == ")"
                or character == "&"
                or character == "%"
                or character == "$"
                or character == "@"
                or character == "*"
                or character == ":"
                or character == ";"
                or character == "."
                or character == "?"
                or character == "/"
                or character == "["
                or character == "]"
                or character == "{"
                or character == "}"
                or character == "="
                or character == "!"
                or character == "<"
                or character == ">"
                or character == ","
                or character == ""
                or character == "_"
                or character == "+"
                or character == "|"):

                new_text += character

        return new_text
"""