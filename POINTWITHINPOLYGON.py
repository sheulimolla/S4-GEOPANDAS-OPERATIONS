
# coding: utf-8

# In[5]:


import geopandas as gp


# In[22]:


tbl= gp.read_file("C:\\Users\SheuliMolla\Desktop\DEV LEAGUE\GEOSPATIAL DATA\spatial_OAHU\soilmu_a_hi990.shp")


# In[23]:


type (tbl)


# In[25]:


tbl.columns


# In[31]:


tbl.geometry.name


# In[32]:


tbl= tbl.rename(columns={'geometry': 'polygon'}).set_geometry('polygon')


# In[33]:


tbl.geometry.name


# In[34]:


tbl['centroid_column'] = tbl.centroid


# In[35]:


tbl = tbl.set_geometry('centroid_column')


# In[40]:


tbl.head ()


# In[54]:


poly0=tbl.polygon[0]


# In[56]:


p1=tbl.centroid_column[0]


# In[57]:


p1.within(poly0)

