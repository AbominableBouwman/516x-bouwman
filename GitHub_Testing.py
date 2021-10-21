#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd

url = "https://raw.githubusercontent.com/isu-abe/516x/master/data/surveys1977.csv"
df = pd.read_csv(url, sep = ",", index_col=0)
print(df.head())
print(df.describe())


# In[ ]:




