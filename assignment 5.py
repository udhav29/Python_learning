import pandas as pd

print("--- Creating Series from a Dictionary ---")
data_dict = {
    'apple': 10,
    'banana': 5,
    'peach': 8,
    'grape': 12
}
series_from_dict = pd.Series(data_dict)
print("Series created from dictionary:")
print(series_from_dict)
print("\nType of series_from_dict:", type(series_from_dict))
print("-" * 40)

print("\n--- Creating Series from Lists ---")

data_list_1 = [100, 200, 300, 400, 500]
series_from_list_1 = pd.Series(data_list_1)
print("Series created from a single list (default index):")
print(series_from_list_1)
print("\nType of series_from_list_1:", type(series_from_list_1))
print("-" * 40)

data_list_2 = ['Mumbai', 'Delhi', 'Bangalore', 'Chennai']
index_list_2 = ['IND-MH', 'IND-DL', 'IND-KA', 'IND-TN']
series_from_list_2 = pd.Series(data_list_2, index=index_list_2)
print("\nSeries created from two lists (custom index):")
print(series_from_list_2)
print("\nType of series_from_list_2:", type(series_from_list_2))
print("-" * 40)

print("\n--- Accessing Elements of a Series ---")

print("\nAccessing elements from 'series_from_dict':")
print(series_from_dict)

print("\nAccessing 'apple' by label:", series_from_dict['apple'])
print("Accessing 'grape' by label:", series_from_dict['grape'])

print("\nAccessing element at position 0 (first element):", series_from_dict[0])
print("Accessing element at position 2 (third element):", series_from_dict[2])

print("\nAccessing 'apple' and 'peach' by a list of labels:")
print(series_from_dict[['apple', 'peach']])

print("\nAccessing elements at positions 1 and 3 by a list of integer positions:")
print(series_from_dict[[1, 3]])

print("\nSlicing 'banana' to 'grape' by label (inclusive):")
print(series_from_dict['banana':'grape'])

print("\nSlicing from position 1 up to (but not including) position 4:")
print(series_from_dict[1:4])

print("-" * 40)

print("\n" + "="*80 + "\n") # Separator between Series and DataFrame sections

print("--- Make a Pandas DataFrame with a two-dimensional Python list ---")
data_2d_list = [
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'London'],
    ['Charlie', 22, 'Paris']
]
df_from_2d_list = pd.DataFrame(data_2d_list, columns=['Name', 'Age', 'City'])
print("DataFrame from a two-dimensional list:")
print(df_from_2d_list)
print("-" * 60)

print("\n--- Create DataFrame from Python dict ---")
data_dict_df = { # Renamed to avoid clash with series_data_dict
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor'],
    'Price': [1200, 25, 75, 300],
    'Stock': [10, 50, 30, 15]
}
df_from_dict_df = pd.DataFrame(data_dict_df)
print("DataFrame from a Python dictionary:")
print(df_from_dict_df)
print("-" * 60)

print("\n--- Create Pandas DataFrame using List of lists ---")
data_list_of_lists = [
    [1, 'Apples', 100],
    [2, 'Bananas', 150],
    [3, 'Oranges', 120]
]
df_list_of_lists = pd.DataFrame(data_list_of_lists, columns=['ID', 'Fruit', 'Quantity'])
print("DataFrame from a list of lists:")
print(df_list_of_lists)
print("-" * 60)

print("\n--- Create a Pandas DataFrame using List of tuples ---")
data_list_of_tuples = [
    (101, 'Engineer', 75000),
    (102, 'Designer', 60000),
    (103, 'Manager', 90000)
]
df_list_of_tuples = pd.DataFrame(data_list_of_tuples, columns=['Employee ID', 'Role', 'Salary'])
print("DataFrame from a list of tuples:")
print(df_list_of_tuples)
print("-" * 60)

print("\n--- Create a Pandas DataFrame from List of dicts ---")
data_list_of_dicts = [
    {'Name': 'David', 'Age': 35, 'Occupation': 'Doctor'},
    {'Name': 'Emily', 'Age': 28, 'Occupation': 'Artist'},
    {'Name': 'Frank', 'Age': 40, 'Occupation': 'Chef'}
]
df_list_of_dicts = pd.DataFrame(data_list_of_dicts)
print("DataFrame from a list of dictionaries:")
print(df_list_of_dicts)
print("-" * 60)

print("\n" + "="*80 + "\n") # Separator between DataFrame creation and iteration sections

print("--- Sample DataFrame for demonstration ---")
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Age': [25, 30, 22, 35, 28, 40],
    'City': ['New York', 'London', 'Paris', 'New York', 'Berlin', 'London'],
    'Score': [85, 92, 78, 95, 88, 70]
}
df = pd.DataFrame(data)
print(df)
print("-" * 60)

print("\n--- Different ways to iterate over rows in Pandas DataFrame ---")

print("\nUsing df.iterrows():")
for index, row in df.iterrows():
    print(f"Index: {index}, Name: {row['Name']}, Age: {row['Age']}")
print("-" * 60)

print("\nUsing df.itertuples():")
for row_tuple in df.itertuples():
    print(f"Index: {row_tuple.Index}, Name: {row_tuple.Name}, Score: {row_tuple.Score}")
print("-" * 60)

print("\n--- Selecting rows in pandas DataFrame based on conditions ---")

print("\nRows where Age > 28:")
df_age_filtered = df[df['Age'] > 28]
print(df_age_filtered)
print("-" * 60)

print("\nRows where City is 'New York' AND Score > 80:")
df_multi_condition = df[(df['City'] == 'New York') & (df['Score'] > 80)]
print(df_multi_condition)
print("-" * 60)

print("\n--- Select any row from a DataFrame using iloc[] ---")

print("\nSelect the first row (index 0):")
row_0 = df.iloc[0]
print(row_0)
print("-" * 60)

print("\nSelect the third row (index 2):")
row_2 = df.iloc[2]
print(row_2)
print("-" * 60)

print("\nSelect rows from index 1 up to (but not including) index 4:")
rows_slice = df.iloc[1:4]
print(rows_slice)
print("-" * 60)

print("\n--- Limited rows selection with given column ---")

print("\nSelecting Name and City for rows where Age > 25:")
limited_selection = df[df['Age'] > 25][['Name', 'City']]
print(limited_selection)
print("-" * 60)

print("\nAlternatively, using .loc for clearer column selection:")
limited_selection_loc = df.loc[df['Age'] > 25, ['Name', 'City']]
print(limited_selection_loc)
print("-" * 60)


print("\n--- Drop rows from the DataFrame based on certain condition applied on a column ---")

print("\nOriginal DataFrame:")
print(df)

print("\nDropping rows where Score is less than 85 (keep rows where Score >= 85):")
df_dropped_by_condition = df[df['Score'] >= 85].copy()
print(df_dropped_by_condition)
print("-" * 60)

print("\n--- Insert row at given position in Pandas DataFrame ---")

print("\nOriginal DataFrame:")
print(df)

new_row_data = pd.DataFrame([['Grace', 33, 'Tokyo', 90]], columns=df.columns)
insert_position = 2

df_before = df.iloc[:insert_position]
df_after = df.iloc[insert_position:]

df_inserted = pd.concat([df_before, new_row_data, df_after]).reset_index(drop=True)
print(f"\nDataFrame after inserting new row at position {insert_position}:")
print(df_inserted)
print("-" * 60)

print("\n--- Create a list from rows in Pandas DataFrame ---")

print("\nOriginal DataFrame:")
print(df)

list_of_lists_from_df = df.values.tolist()
print("\nList of lists created from DataFrame rows:")
print(list_of_lists_from_df)
print("-" * 60)

print("\nCreate a list of dictionaries from DataFrame rows:")
list_of_dicts_from_df = df.to_dict(orient='records')
print(list_of_dicts_from_df)
print("-" * 60)