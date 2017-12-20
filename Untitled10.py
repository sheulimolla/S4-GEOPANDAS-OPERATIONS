
# coding: utf-8

# In[1]:


import geopandas as gp


# In[3]:


tbl=gp.read_file("C:\\Users\SheuliMolla\Desktop\DEV LEAGUE\GEOSPATIAL DATA\spatial_OAHU\soilmu_a_hi990.shp")


# In[6]:


type (tbl)


# In[17]:


tbl.columns


# In[21]:


tbl.head()


# In[30]:


tbl.geometry[0]


# In[31]:


tbl.geometry [2]


# In[32]:


tbl.geometry [4]


# In[34]:


tbl.loc.[1]


# In[35]:


tbl.loc["geometry"]


# In[36]:


tbl.index


# In[37]:


tbl.columns


# In[38]:


tbl.columns.loc["geometry"]


# In[29]:


tbl.head().geometry[2]

