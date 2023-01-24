#!/usr/bin/env python
# coding: utf-8

# ### Assignment Set 01 

# ## Q1.	Look at the data given below. Plot the data, find the outliers and find out  μ,σ,σ^2

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


x=pd.Series([24.23,25.53,25.41,24.14,29.62,28.25,25.81,24.39,40.26,32.95,91.36,25.99,39.42,26.71,35.00])
name=['Allied Signal','Bankers Trust','General Mills','ITT Industries','J.P.Morgan & Co.','Lehman Brothers',
      'Marriott','MCI','Merrill Lynch','Microsoft','Morgan Stanley','Sun Microsystems','Travelers','US Airways',
      'Warner-Lambert']


# In[4]:


#to plot the data 
#pie plot
plt.figure(figsize=(6,9))
plt.pie(x,labels=name,autopct='%1.0f%%')
plt.show()


# In[5]:


#to find outliers
#boxplot
sns.boxplot(x)


# In[6]:


#Mean
x.mean()


# In[7]:


#standard deviation
x.std()


# In[8]:


#variance
x.var()


# ## Q5.	Returns on a certain business venture, to the nearest $1,000, are known to follow the following probability distribution

# In[16]:


import numpy

y=[-2000,-1000,0,1000,2000,3000]


# In[17]:


#standard deviation
x=numpy.std(y)
print(x)


# In[19]:


#variance
x=numpy.var(y)
print(x)


# In[ ]:




