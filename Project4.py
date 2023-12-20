#!/usr/bin/env python
# coding: utf-8

# # VEHICLES PROJECT
# 
The following dataframe describes car sales advertisements. Providing information about each car:
-price
-year produced
-model
-condition
-cylinders
-fuel
-odometer
-transmission
-type
-paint color
-4 wheel Drive (yes or no)
-date was posted
-Total days since listed
# In[1]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import plotly.express as px


# In[2]:


#df= pd.read_csv('vehicles_us.csv')
#df.head()


# In[3]:


df= pd.read_csv(r'Data science/project 4/vehicles_us.csv')
df.head()


# ### New column indicating just the car manufacturer

# In[4]:


df['manufacturer_name'] = df['model'].apply(lambda x: x.split(' ')[0] if pd.notnull(x) else None)


# In[5]:


df.head()


# In[6]:


df.info()


# ### Cleaning data by removing duplicates and missing values

# In[7]:


df = df.drop_duplicates()


# In[8]:


print(df.isna().sum())


# In[9]:


df= df.dropna()


# In[10]:


print(df.isna().sum())


# #### No more missing values found

# ### Replacing true missing values for the following columns with the word "null"

# In[11]:


columns_to_replace = 'model_year','cylinders', 'odometer', 'paint_color','is_4wd'
for column in columns_to_replace:
    df[column] = df[column].fillna('null')


# In[12]:


years = df["model_year"].unique()


# In[13]:


years


# In[14]:


#df['model_year'] = pd.to_numeric(df['model_year'], errors='coerce')  


# In[15]:


#default_year = 0


# In[16]:


#df['model_year'] = df['model_year'].fillna(default_year).astype(int)


# ### Converting floating values to integer

# In[17]:


df['model_year']= df['model_year'].astype('int')


# In[18]:


df.head()


# In[19]:


df['model_year'].unique()


# In[20]:


manufacturers_choice= df['manufacturer_name'].unique()


# In[21]:


manufacturers_choice


# ### Items to select from on "manufacturer" select box 

# In[22]:


min_year= df['model_year'].min()


# In[23]:


max_year = df['model_year'].max()


# ### Looking for the min and max number to filter by range year

# In[24]:


min_year


# In[25]:


max_year


# In[26]:


(min_year,max_year) = ( df['model_year'].min(), df['model_year'].max())


# In[27]:


min_year


# ### Function to categorize price range according the age of the car

# In[28]:


def age_category(x):
    if x<5: return '<5'
    elif x>=5 and x<10: return '5-10'
    elif x>=10 and x<20: return '10-20'
    else: return '>20'  


# In[29]:


df['age']=2023-df['model_year']


# In[30]:


df['age_category']= df['age'].apply(age_category)


# In[ ]:




