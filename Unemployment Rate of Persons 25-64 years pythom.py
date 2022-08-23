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

df.duplicated().sum() # there are not duplicates in the database

df.isnull() # returns a specified value if the expression is NULL

df.isnull().sum() #missing values in the database

df.dropna(axis=0, how="any", inplace=True) #drop all rows with missing values and overwrite dataset


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



av_rate_by_sex = df.groupby("Sex")["VALUE"].mean()
print(av_rate_by_sex)

av_rate_by_sex.plot(kind="bar", title="Mean Unemployment Rate by Sex")
plt.show()

#unemploment rate female lower than men

df.plot(x="Quarter", y="VALUE", kind="line", title="Unemployment Rate through Time")
plt.show() 

#unemployment highest rate 2012 q2, lowest 2020q2


av_rate_by_Education_Level = df.groupby("Education Level")["VALUE"].mean()
print(av_rate_by_Education_Level)

av_rate_by_Education_Level.plot(kind="bar", title="Unemployment Rate Mean by Education Level")
plt.show()

#unemployment highest rate primary

