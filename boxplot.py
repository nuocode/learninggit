#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



# ## 画出boxplot，最后一行20是额外添加的大数，看如何置于box之外。

# In[67]:


group_A = np.random.randint(low=39, high=158, size=20)
group_A.sort()
group_A


# In[68]:


group_B = np.random.randint(low=60, high=180, size=20)
group_B.sort()
group_B


# In[69]:


group_C = np.random.randint(low=38, high=190, size=20)
group_C.sort()
group_C


# In[70]:


group_D = np.random.randint(low=28, high=138, size=20)
group_D.sort()
group_D


# In[71]:


data = pd.DataFrame({"group_A": group_A,"group_B": group_B,"group_C": group_C,"group_D": group_D })
data.median()


# In[72]:


data


# In[73]:


data.loc[20] = [260, 199, 189, 290]
data


# In[74]:


data.boxplot()
plt.ylabel("Price($)")
plt.xlabel("Group")
plt.show()


# In[ ]:




