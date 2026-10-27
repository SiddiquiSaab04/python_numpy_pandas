import pandas as pd

data = {
    "User_ID": [101, 102, 103, 104],
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Score": [85.5, 91.2, 78.0, 95.4],
    "Passed": [True, True, False, True],
    "city":["Izmir","Dublin","Warsaw","Baku"]
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