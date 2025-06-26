import pandas as pd


date_strings_1 = pd.Series(["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04"])
timeseries_1 = pd.to_datetime(date_strings_1)
print("Converted Series 1:\n", timeseries_1)


date_strings_2 = pd.Series(["01/15/2024", "March 10, 2023", "2022-12-25 10:30:00", "2025/06/26"])
timeseries_2 = pd.to_datetime(date_strings_2)
print("\nConverted Series 2:\n", timeseries_2)


date_strings_3 = pd.Series(["2023-01-01", "Not a date", "2023-01-03"])
timeseries_3_coerce = pd.to_datetime(date_strings_3, errors='coerce')
print("\nConverted Series 3 (with NaT for errors):\n", timeseries_3_coerce)


date_strings_4 = pd.Series(["15-01-2023", "20-02-2023", "25-03-2023"])
timeseries_4 = pd.to_datetime(date_strings_4, format="%d-%m-%Y")
print("\nConverted Series 4 (custom format):\n", timeseries_4)