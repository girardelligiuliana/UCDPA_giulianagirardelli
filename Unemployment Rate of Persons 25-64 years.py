#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd #read CSV files, data processing
import numpy as np #recomendation system
import matplotlib.pyplot as plt #data visualisation
import seaborn as sns #data visualisation


# In[2]:


df = pd.read_csv(r"C:\Users\girar\OneDrive\Escritorio\Unemployment Rate of Persons 25-64 years.csv")
#import csv file


# In[3]:


df.info()


# In[4]:


df.shape


# In[5]:


df.head()


# In[6]:


df.tail()


# In[7]:


df.describe() 


# In[ ]:





# In[8]:


df.columns


# In[9]:


df.duplicated().sum() # there are not duplicates in the database


# In[10]:


df.isnull() # returns a specified value if the expression is NULL


# In[11]:


df.isnull().sum() #missing values in the database


# In[12]:


df.dropna(axis=0, how="any", inplace=True) #drop all rows with missing values and overwrite dataset


# In[ ]:





# In[13]:


df.sort_values("Education Level")


# In[14]:


df[["Sex", "Education Level", "VALUE"]]


# In[15]:


df[["VALUE", "Education Level", "Quarter"]]


# In[16]:


df[df["Sex"] == "Female"]


# In[ ]:





# In[17]:


df[df["Sex"] == "Male"]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[18]:


df.groupby("Sex")["VALUE"].mean()


# In[19]:


df.groupby("Sex")["VALUE"].agg([min, max, sum])


# In[ ]:





# In[ ]:





# In[ ]:





# In[45]:


#Unemployment rates Female vs Male
df[df["Sex"] == "Female"]["VALUE"].hist(alpha=0.7)
df[df["Sex"] == "Male"]["VALUE"].hist(alpha=0.7)

plt.legend(["Female", "Male"])
plt.title("Unemployment Rate Female VS Male")
plt.show()


# In[ ]:





# In[21]:


av_rate_by_sex = df.groupby("Sex")["VALUE"].mean()
print(av_rate_by_sex)

av_rate_by_sex.plot(kind="bar", title="Mean Unemployment Rate by Sex")
plt.show()

#unemploment rate female lower than men


# In[ ]:





# In[23]:


# grafico de torta con education level solo de female, y solo de male

# grafico lineal primario a traves del tiempo, secundario etc


# In[36]:


df.plot(x="Quarter", y="VALUE", kind="line", title="Unemployment Rate through Time")
plt.show() 

#unemployment highest rate 2012 q2, lowest 2020q2


# In[27]:



av_rate_by_Education_Level = df.groupby("Education Level")["VALUE"].mean()
print(av_rate_by_Education_Level)

av_rate_by_Education_Level.plot(kind="bar", title="Unemployment Rate Mean by Education Level")
plt.show()

#unemployment highest rate primary


# In[ ]:




