import pandas as pd
import numpy as np
import urllib.request
import urllib.parse
import json
import socket


base_url = "https://data.cityofnewyork.us/resource/43nn-pn8j.json"
page = 1
limit = 10
offset = (page - 1) * limit
params = urllib.parse.urlencode({"$limit":limit,"$offset":offset})
url = f"{base_url}?{params}"

try:
    with urllib.request.urlopen(url,timeout = 10) as response:
        raw_data = response.read()
        data = json.loads(raw_data)
        df = pd.DataFrame(data)
        # print(df)
        print("printing rows...")
        print(df.shape)
        print("info of columns...")
        print(df.info())
        print("missing values in column...")
        print(df.isnull().sum())
        print("column data type...")
        print(df.dtypes)
        print("duplicates....")
        print(df.duplicated().sum())
except(urllib.error.URLError,TimeoutError,socket.timeout) as e:
    print(f"failed to fetch the API,{e}")
