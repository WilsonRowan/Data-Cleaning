import pandas as pd

df = pd.read_csv("Messy_Employee_dataset.csv")

# drop irrelevant column 
df = df.drop(columns=["First_Name", "Last_Name", "Email", "Phone"])

# handle misssing data
df = df.dropna(subset=["Age", "Salary"])

# remove duplicate values
df = df.drop_duplicates()

# cleaned dataset 
df.to_csv("Final_Employee_dataset.csv", index=False)
