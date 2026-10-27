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
# print(df)
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
# values = {
#     "User_ID":102.0,
#     "Name":"Ben",
#     "Score":56.5,
#     "Passed":True,
#     "city":"Baku"
# }
# filled = df.fillna(value=values , inplace=True)
# print(filled)
print(df)

emp_data = {
    "Employee_ID": [101, 102, 103, 104, np.nan, 106],
    "Name": ["Zeeshan", "Ayesha", "Ali", np.nan, "Sana", "Usman"],
    "Department": ["IT", "HR", "Sales", "Marketing", "IT", np.nan],
    "Join_Date": ["2022-01-15", "2023-05-11", np.nan, "2021-09-01", "2024-02-10", "2023-11-20"]
}

salary_data = {
    "Employee_ID": [101, 102, np.nan, 104, 105, 106],
    "Base_Salary": [85000.0, np.nan, 45000.0, 60000.0, 95000.0, 72000.0],
    "Bonus": [5000.0, 3000.0, np.nan, 4000.0, 8000.0, np.nan],
    "Allowances": [12000.0, 10000.0, 5000.0, np.nan, 15000.0, 9000.0]
}
emp_df = pd.DataFrame(emp_data)
sal_df = pd.DataFrame(salary_data)

print(pd.merge(emp_df,sal_df,on="Employee_ID",how="left"))