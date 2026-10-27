import pandas as pd
import numpy as np
data = {
    "User_ID": [101, np.nan, 103, 104],
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Score": [85.5, 91.2,np.nan, 95.4],
    "Passed": [np.nan, True, False, True],
    "city":["Izmir","Dublin","Warsaw",np.nan]
}

df = pd.DataFrame(data)
print(df)
# select_row = df.loc[[0,1,2]]
# print(select_row)

# select_row = df.loc[[2,3]][["Name","Score"]]
# print(select_row)

# conditions

# high_score = df[df["Score"] > 90]
# print(high_score)

# city_conditon = df[df["city"] == "Izmir"]
# print(city_conditon)


# nulls
# sum_of_values = df.isna().sum()
# print(sum_of_values)

# sum_of_values = df.isna()
# print(sum_of_values)

# sum_of_values = df.isna().sum().any()
# print(sum_of_values)

# dropna # thresh 

# print(df.dropna(thresh = 5))

# fillna
