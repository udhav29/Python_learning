import pandas as pd

data1 = {'ID': [1, 2, 3, 4, 5],
         'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
         'Age': [25, 30, 35, 28, 22]}
df1 = pd.DataFrame(data1)
print("--- df1 ---")
print(df1, "\n")

data2 = {'ID': [1, 2, 4, 6, 7],
         'City': ['New York', 'London', 'Paris', 'Tokyo', 'Sydney'],
         'Salary': [70000, 60000, 80000, 75000, 90000]}
df2 = pd.DataFrame(data2)
print("--- df2 ---")
print(df2, "\n")

print("--- Inner Merge (ID) ---")
inner_merged_df = pd.merge(df1, df2, on='ID', how='inner')
print(inner_merged_df, "\n")

print("--- Left Join (df1 and df2 on ID) ---")
left_joined_df = pd.merge(df1, df2, on='ID', how='left')
print(left_joined_df, "\n")

print("--- Right Join (df1 and df2 on ID) ---")
right_joined_df = pd.merge(df1, df2, on='ID', how='right')
print(right_joined_df, "\n")

df1_indexed = df1.set_index('ID')
df2_indexed = df2.set_index('ID')

print("--- df1 with 'ID' as index ---")
print(df1_indexed, "\n")
print("--- df2 with 'ID' as index ---")
print(df2_indexed, "\n")

print("--- Index-Based Join (df1_indexed.join(df2_indexed)) ---")
index_joined_df = df1_indexed.join(df2_indexed, how='left')
print(index_joined_df, "\n")

data3 = {'ID': [1, 2, 3, 4, 5, 8],
         'Department': ['HR', 'IT', 'Finance', 'HR', 'IT', 'Sales'],
         'ManagerID': [101, 102, 103, 101, 102, 104]}
df3 = pd.DataFrame(data3)
print("--- df3 (for multiple keys) ---")
print(df3, "\n")

data4 = {'ID': [1, 2, 4, 8, 9],
         'Department': ['HR', 'IT', 'HR', 'Sales', 'Marketing'],
         'Project': ['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon'],
         'Budget': [50000, 75000, 60000, 90000, 40000]}
df4 = pd.DataFrame(data4)
print("--- df4 (for multiple keys) ---")
print(df4, "\n")

print("--- Merging with Multiple Keys (ID and Department) ---")
multi_key_merged_df = pd.merge(df3, df4, on=['ID', 'Department'], how='inner')
print(multi_key_merged_df, "\n")
