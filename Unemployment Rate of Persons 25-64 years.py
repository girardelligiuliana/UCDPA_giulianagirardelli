import pandas as pd #read CSV files, data processing
import numpy as np #recomendation system
import matplotlib.pyplot as plt #data visualisation
import seaborn as sns #data visualisation

df = pd.read_csv(r"C:\Users\girar\OneDrive\Escritorio\Unemployment Rate of Persons 25-64 years.csv")
#import csv file

df.info()

df.shape

df.head()

df.tail()

df.describe() 

df.columns

df.duplicated().sum() 

df.isnull() 

df.isnull().sum()

df.dropna(axis=0, how="any", inplace=True)

df.sort_values("Education Level")

df[["Sex", "Education Level", "VALUE"]]

df[["VALUE", "Education Level", "Quarter"]]

df[df["Sex"] == "Female"]

df[df["Sex"] == "Male"]

df.groupby("Sex")["VALUE"].mean()

df.groupby("Sex")["VALUE"].agg([min, max, sum])

#Unemployment rates Female vs Male
df[df["Sex"] == "Female"]["VALUE"].hist(alpha=0.7)
df[df["Sex"] == "Male"]["VALUE"].hist(alpha=0.7)

plt.legend(["Female", "Male"])
plt.title("Unemployment Rate Female VS Male")
plt.show()

df[df["Sex"] == "Female"].hist(alpha=0.7)

plt.title("Female Unemployment Rate ")
plt.show()


df[df["Sex"] == "Male"].hist()
plt.title("Male Unemployment Rate ")
plt.show()

df.plot(x="Quarter", y="VALUE", kind="line", title="Unemployment Rate through Time")
plt.show() 

#unemployment highest rate 2012 q2, lowest 2020q2


av_rate_by_Education_Level = df.groupby("Education Level")["VALUE"].mean()
print(av_rate_by_Education_Level)

av_rate_by_Education_Level.plot(kind="bar", title="Unemployment Rate Mean by Education Level")
plt.show()

#unemployment highest rate primary
