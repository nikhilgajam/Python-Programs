import pandas as pd
import numpy as np

# In pandas we have 3 data types
# 1. Series
# 2. DataFrame
# 3. Pandas


arr = [1, 2, 3, 4, 5, 6]
data = {"Name": ["Ram", "Abdul"], "Age": [18, 18]}

# Creating Series using pandas (It is a 1D container)

s = pd.Series(arr)
print(s)

s1 = pd.Series(data)
print(s1)

# Locating elements in Series
print(s[1])
print(s1[0])


# Creating DataFrame using pandas (It is a 2D container)

d = pd.DataFrame(arr)
print(d.loc[1])

d1 = pd.DataFrame(data)
print(d1.loc[0])

# Locating elements in DataFrame
print(s[1])
print(s1[0])


# Creating Panel using pandas (It is a 3D container)
# p = pd.Panel()  Panels are removed from pandas

# Describe in pandas

print(s.describe())
print(d.describe())
print(d1.describe())

# Shape

print(d1.shape)

# Search for statistical operations in pandas

print(s.mean())
print(d.median())
print(d1.mode())
print(s.sum())
print(s.sum(1))  # Only numbers will be summed up by passing 1 as argument
print(s.cumsum())


# To read from a file (ex: data.csv)

# pd.read_csv("data.csv")
# pd.read_html("data.html")
# pd.read_excel("data.xlsx")


# Pandas to_string method to show all data (otherwise it only shows staring and ending five elements only)

print(d1.to_string())
