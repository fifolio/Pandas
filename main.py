import pandas as pd

mydataset = {"cars": ["BMW", "Volvo", "Ford"], "passings": [3, 7, 2]}

myvar = pd.DataFrame(mydataset)

# print(myvar)

# print(pd.__version__)

# Create a simple Pandas Series from a list:
a = [1, 7, 2]

myvar = pd.Series(a)

# print(myvar)

# Return the first value of the Series:
# print(myvar[0])

# Create your own labels:
a = [1, 7, 2]

myvar = pd.Series(a, index=["x", "y", "z"])

# print(myvar)

# Return the value of "y":
# print(myvar["y"])

# Create a simple Pandas Series from a dictionary:
calories = {"day1": 4.20, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

# print(myvar)

# Create a Series using only data from "day1" and "day2":
calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index=["day1", "day2"])

# print(myvar)

# Create a DataFrame from two Series:
data = {"calories": [420, 380, 390], "duration": [50, 40, 45]}

myvar = pd.DataFrame(data)

# print(myvar)

# Create a simple Pandas DataFrame:
data = {"calories": [420, 380, 390], "duration": [50, 40, 45]}

# load data into a DataFrame object:
df = pd.DataFrame(data)

# print(df)

# Return row 0:
# refer to the row index:
# print(df.loc[0]) # Note: This example returns a Pandas Series.

# Return row 0 and 1:
# use a list of indexes:
# print(df.loc[[0, 1]]) # When using [], the result is a Pandas DataFrame.

# Add a list of names to give each row a name:
data = {"calories": [420, 380, 390], "duration": [50, 40, 45]}

df = pd.DataFrame(data, index=["day1", "day2", "day3"])

# print(df.loc["day1"])

# Load the CSV into a DataFrame:
df = pd.read_csv("data.csv")

# print(df.to_string()) # Tip: use to_string() to print the entire DataFrame.

# Print the DataFrame without the to_string() method:
df = pd.read_csv("data.csv")

# print(df)

# Check the number of maximum returned rows:
# print(pd.options.display.max_rows)

# Increase the maximum number of rows to display the entire DataFrame:
pd.options.display.max_rows = 9999

df = pd.read_csv("data.csv")

# print(df)

# Load the JSON file into a DataFrame:
df = pd.read_json("data.json")

# print(df.to_string())

# Load a Python Dictionary into a DataFrame:
data = {
    "Duration": {"0": 60, "1": 60, "2": 60, "3": 45, "4": 45, "5": 60},
    "Pulse": {"0": 110, "1": 117, "2": 103, "3": 109, "4": 117, "5": 102},
    "Maxpulse": {"0": 130, "1": 145, "2": 135, "3": 175, "4": 148, "5": 127},
    "Calories": {"0": 409, "1": 479, "2": 340, "3": 282, "4": 406, "5": 300},
}

df = pd.DataFrame(data)

# print(df)

# Get a quick overview by printing the first 10 rows of the DataFrame:
df = pd.read_csv("data.csv")

# print(df.head(10))

# Print the first 5 rows of the DataFrame:
df = pd.read_csv("data.csv")

# print(df.head())

# Print the last 5 rows of the DataFrame:
# print(df.tail())

# Print information about the data:
# print(df.info())

# Return a new Data Frame with no empty cells:
df = pd.read_csv("data.csv")

new_df = df.dropna()

# print(new_df.to_string())

# Remove all rows with NULL values:
df = pd.read_csv("data.csv")

df.dropna(inplace=True)

# print(df.to_string())

# Replace NULL values with the number 130:
df = pd.read_csv("data.csv")

df.fillna(130, inplace=True)
# print(df)

# Replace NULL values in the "Calories" columns with the number 130:
df = pd.read_csv("data.csv")

df.fillna({"Calories": 130}, inplace=True)

# Calculate the MEAN, and replace any empty values with it:
df = pd.read_csv("data.csv")

x = df["Calories"].mean()

df.fillna({"Calories": x}, inplace=True)

# Calculate the MEDIAN, and replace any empty values with it:
df = pd.read_csv("data.csv")

x = df["Calories"].median()

df.fillna({"Calories": x}, inplace=True)

# Calculate the MODE, and replace any empty values with it:
df = pd.read_csv("data.csv")

x = df["Calories"].mode()[0]

df.fillna({"Calories": x}, inplace=True)

# Convert to date:
df = pd.read_csv("data.csv")

# df["Date"] = pd.to_datetime(df["Date"], format="mixed")

# print(df.to_string())

# Remove rows with a NULL value in the "Date" column:
# df.dropna(subset=["Date"], inplace=True)

# Set "Duration" = 45 in row 7:
df.loc[7, "Duration"] = 45


# Loop through all values in the "Duration" column. If the value is higher than 120, set it to 120:
for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.loc[x, "Duration"] = 120


# Delete rows where "Duration" is higher than 120:
for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.drop(x, inplace=True)

# Returns True for every row that is a duplicate, otherwise False:
print(df.duplicated())

# Remove all duplicates:
df.drop_duplicates(inplace = True)