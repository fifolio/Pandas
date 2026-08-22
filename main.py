import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

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

myvar = pd.Series(a, index = ["x", "y", "z"])

# print(myvar)

# Return the value of "y":
# print(myvar["y"])

# Create a simple Pandas Series from a dictionary:
calories = {"day1": 4.20, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

# print(myvar)

# Create a Series using only data from "day1" and "day2":
calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"])

# print(myvar)

# Create a DataFrame from two Series:
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)