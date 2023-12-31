import pandas as pd
import numpy as np
import seaborn as sns                       #visualisation
import matplotlib.pyplot as plt             #visualisation
sns.set(color_codes=True)
df = pd.read_csv("C:/Users/1/ANALIZ/data.csv")
# To display the top 5 rows 
print(df.head(5))
print("________________")
print(df.tail(5))  
print("________________")
print(df.dtypes)
print("________________")
df = df.drop(['Engine Fuel Type', 'Market Category', 'Vehicle Style', 'Popularity', 'Number of Doors', 'Vehicle Size'], axis=1)
print(df.head(5))
print("________________")
df = df.rename(columns={"Engine HP": "HP", "Engine Cylinders": "Cylinders", "Transmission Type": "Transmission", "Driven_Wheels": "Drive Mode","highway MPG": "MPG-H", "city mpg": "MPG-C", "MSRP": "Price" })
print(df.head(5))
print("________________")
print(df.shape)
print("________________")
duplicate_rows_df = df[df.duplicated()]
print("number of duplicate rows: ", duplicate_rows_df.shape)
print("________________")
print(df.count() )
print("________________")
df = df.drop_duplicates()
print(df.head(5))
print("________________")
print(df.count())
print("________________")
print(df.isnull().sum())
print("________________")
df = df.dropna()    # Dropping the missing values.
print(df.count())
print("________________")
print(df.isnull().sum())
print("________________")
plt.figure(figsize=(8, 6))  # Установите желаемый размер графика
sns.boxplot(x=df['Price'])
plt.show()
print("________________")
plt.figure(figsize=(8, 6))
sns.boxplot(x=df['HP'])
plt.show()
plt.figure(figsize=(8, 6))
sns.boxplot(x=df['Cylinders'])
plt.show()
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
print(IQR)
df = df[~((df < (Q1 - 1.5 * IQR)) |(df > (Q3 + 1.5 * IQR))).any(axis=1)]
print(df.shape)
df.Make.value_counts().nlargest(40).plot(kind='bar', figsize=(10,5))
plt.title("Number of cars by make")
plt.ylabel('Number of cars')
plt.xlabel('Make');
plt.figure(figsize=(10,5))
c= df.corr()
sns.heatmap(c,cmap="BrBG",annot=True)
print(c)
fig, ax = plt.subplots(figsize=(10,6))
ax.scatter(df['HP'], df['Price'])
ax.set_xlabel('HP')
ax.set_ylabel('Price')
plt.show()