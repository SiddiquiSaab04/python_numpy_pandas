import pandas as pd
import numpy as np
import urllib.request
import urllib.parse
import json
import socket


base_url = "https://data.cityofnewyork.us/resource/43nn-pn8j.json"
page = 1
limit = 1000
offset = (page - 1) * limit
params = urllib.parse.urlencode({"$limit":limit,"$offset":offset})
url = f"{base_url}?{params}"

try:
    with urllib.request.urlopen(url,timeout = 10) as response:
        raw_data = response.read()
        data = json.loads(raw_data)
except(urllib.error.URLError,TimeoutError,socket.timeout) as e:
    print(f"failed to fetch the API,{e}")
    
df = pd.DataFrame(data)
# print(df)
# drop_location 
df = df.drop(columns=["location"])
# remove @ cols
df = df.drop(columns=[c for c in df.columns if c.startswith(":@")])
# check null
# missing = df.isnull().sum()
# print(missing)
# missing percentage
# missing_percentage = (df.isnull().sum() / len(df) ) * 100
# print(missing_percentage)
# cuisine description 
df["cuisine_description"] = df["cuisine_description"].fillna("Unknown")
missing = df.isnull().sum()
print(missing)
