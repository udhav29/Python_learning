import re

def validate_email(email):
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(email_pattern, email)

def validate_mobile(mobile_no):
    mobile_pattern = r"^[6-9]\d{9}$"
    return re.match(mobile_pattern, mobile_no)

email1 = "test@example.com"
email2 = "invalid-email"
mobile1 = "9876543210"
mobile2 = "12345"

print(f"'{email1}' is a valid email: {bool(validate_email(email1))}")
print(f"'{email2}' is a valid email: {bool(validate_email(email2))}")
print(f"'{mobile1}' is a valid mobile number: {bool(validate_mobile(mobile1))}")
print(f"'{mobile2}' is a valid mobile number: {bool(validate_mobile(mobile2))}")
print("\n\n\n\n\n-------- question2----------")
import pandas as pd

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

print("Summary Statistics:")
print(df.describe())

print("\nSpecies Counts:")
print(df['species'].value_counts())

grouped = df.groupby('species').mean()
print("\nAverage Measurements by Species:")
print(grouped)
