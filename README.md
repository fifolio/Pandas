Pandas Introduction

What is Pandas?
* Pandas is a Python library used for working with data sets.
* It has functions for analyzing, cleaning, exploring, and manipulating data.
* The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis" and was created by Wes McKinney in 2008.

Why Use Pandas?
* Pandas allows us to analyze big data and make conclusions based * on statistical theories.
* Pandas can clean messy data sets, and make them readable and relevant.
* Relevant data is very important in data science.

What Can Pandas Do?
* Pandas gives you answers about the data. Like:
* Is there a correlation between two or more columns?
* What is average value?
* Max value?
* Min value?
* Pandas are also able to delete rows that are not relevant, or contains wrong values, like empty or NULL values. This is called cleaning the data.

---

What is a Series?
* A Pandas Series is like a column in a table.
* It is a one-dimensional array holding data of any type.

Labels
* If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.
* This label can be used to access a specified value.

Create Labels
* With the index argument, you can name your own labels.
* When you have created labels, you can access an item by referring to the label.

Key/Value Objects as Series
* You can also use a key/value object, like a dictionary, when creating a Series.
* Note: The keys of the dictionary become the labels.

* To select only some of the items in the dictionary, use the index argument and specify only the items you want to include in the Series.

DataFrames
* Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
* Series is like a column, a DataFrame is the whole table.

---

Pandas DataFrames

What is a DataFrame?

* A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.

Locate Row
* Pandas use the loc attribute to return one or more specified row(s)

Named Indexes
* With the index argument, you can name your own indexes.

---

Read CSV Files

* A simple way to store big data sets is to use CSV files (comma separated files).
* CSV files contains plain text and is a well know format that can be read by everyone including Pandas. 
* In our examples we will be using a CSV file called 'data.csv'.
* If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows.

max_rows
* The number of rows returned is defined in Pandas option settings. 
* You can check your system's maximum rows with the pd.options.display.max_rows statement.
* In my system the number is 60, which means that if the DataFrame contains more than 60 rows, the print(df) statement will return only the headers and the first and last 5 rows.

---

Pandas Read JSON

* Big data sets are often stored, or extracted as JSON.
* JSON is plain text, but has the format of an object, and is well known in the world of programming, including Pandas.
* If your JSON code is not in a file, but in a Python Dictionary, you can load it into a DataFrame directly

---

Pandas - Analyzing DataFrames

Viewing the Data
* One of the most used method for getting a quick overview of the DataFrame, is the head() method.
* The head() method returns the headers and a specified number of rows, starting from the top.
* Note: if the number of rows is not specified, the head() method will return the top 5 rows.
* There is also a tail() method for viewing the last rows of the DataFrame.
* The tail() method returns the headers and a specified number of rows, starting from the bottom.

Info About the Data
* The DataFrames object has a method called info(), that gives you more information about the data set.

---

Data Cleaning
Data cleaning means fixing bad data in your data set.

Bad data could be:

* Empty cells
* Data in wrong format
* Wrong data
* Duplicates
* In this tutorial you will learn how to deal with all of them.

---

Empty Cells
* Empty cells can potentially give you a wrong result when you analyze data.

Remove Rows
* One way to deal with empty cells is to remove rows that contain empty cells.
This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result.
* Note: By default, the dropna() method returns a new DataFrame, and will not change the original.
* dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containing NULL values from the original DataFrame.
* inplace = True: The argument to make sure that the changes are done for the original DataFrame instead of returning a new one.



Replace Empty Values
* Another way of dealing with empty cells is to insert a new value instead.
* This way you do not have to delete entire rows just because of some empty cells.
* The fillna() method allows us to replace empty cells with a value:

Replace Only For Specified Columns
* The example above replaces all empty cells in the whole Data Frame.
* To only replace empty values for one column, specify the column name for the DataFrame:

Replace Using Mean, Median, or Mode
* A common way to replace empty cells, is to calculate the mean, median or mode value of the column.
* Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column.
* Mean = the average value (the sum of all values divided by number of values).
* Median = the value in the middle, after you have sorted all values ascending.
* Mode = the value that appears most frequently.

