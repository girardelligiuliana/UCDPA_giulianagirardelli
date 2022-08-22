#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd #read CSV files, data processing
import numpy as np #recomendation system
import matplotlib.pyplot as plt #data visualisation
import seaborn as sns #data visualisation


# In[8]:


df = pd.read_csv(r"C:\Users\girar\OneDrive\Escritorio\Unemployment Rate of Persons 25-64 years.csv")
#import csv file


# In[9]:


df.info()


# In[10]:


df.shape


# In[12]:


df.head()


# In[14]:


df.tail()


# In[121]:


df.describe() 


# In[ ]:





# In[16]:


df.columns


# In[17]:


df.duplicated().sum() # there are not duplicates in the database


# In[18]:


df.isnull() # returns a specified value if the expression is NULL


# In[19]:


df.isnull().sum() #missing values in the database


# In[20]:


df.dropna(axis=0, how="any", inplace=True) #drop all rows with missing values and overwrite dataset


# In[ ]:





# In[143]:


df.sort_values("Education Level")


# In[141]:


df[["Sex", "Education Level", "VALUE"]]


# In[144]:


df[["VALUE", "Education Level", "Quarter"]]


# In[42]:


df[df["Sex"] == "Female"]


# In[ ]:





# In[43]:


df[df["Sex"] == "Male"]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[63]:


df.groupby("Sex")["VALUE"].mean()


# In[64]:


df.groupby("Sex")["VALUE"].agg([min, max, sum])


# In[161]:


import tkinter
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

plt.show()
df["Sex"].hist()
plt.hist(x)
plt.show()


# In[ ]:





# In[164]:


x = np.array(["Primary"])
y = np.array([0, 5, 10, 15, 20, 25, 30])

plt.bar(x,y)
plt.show()


# In[84]:



df[df["Sex"] == "Female"]["VALUE"].hist(alpha=0.7)
df[df["Sex"] == "Male"]["VALUE"].hist(alpha=0.7)

plt.legend(["Female", "Male"])
plt.show()


# In[113]:


fig, ax= plt.subplots()
ax.plot(df["Sex"] == "Male", 
       df["Quarter"], 
        marker="o")
plt.show()


# In[109]:


fig, ax= plt.subplots()
ax.plot(df["Education Level"], 
       df["Quarter"], 
        marker="o")
plt.show()


# In[114]:


# Which sex has the highest unemployment rates?

#Graph number 1
sns.set(style="darkgrid")
plt.title("education level & unemployment")
ax= sns.countplot(x="Education Level", data=df, palette= ("purple", "red","yellow", "blue", "green", "black", "white", "cyan"))


# In[93]:


# grafico de torta con education level solo de female, y solo de male
# grafico de barra de education level a traves de los anios
# grafico lineal primario a traves del tiempo, secundario etc

