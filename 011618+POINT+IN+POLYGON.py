
# coding: utf-8

# # TITLE_POINTWITHINPOLYGON

# In[5]:


import geopandas as gp


# In[130]:


tbl= gp.read_file("C:\\Users\SheuliMolla\Desktop\DEV LEAGUE\GEOSPATIAL DATA\spatial_OAHU\soilmu_a_hi990.shp")


# In[131]:


type (tbl)


# In[132]:


tbl.columns


# In[133]:


tbl.geometry.name


# In[134]:


tbl= tbl.rename(columns={'geometry': 'polygon'}).set_geometry('polygon')


# In[135]:


tbl.geometry.name


# # Table header

# In[136]:


tbl.head ()


# ## Representative Points are guarunteed to be within polygons

# In[142]:


tbl.representative_point()[0]


# In[143]:


print (tbl.representative_point()[0])


# # Designating polygons and points from table

# In[144]:


poly0=tbl.polygon[0]


# In[147]:


p0=tbl.representative_point()[0]


# In[146]:


print (tbl.representative_point()[0])


# In[149]:


poly1=tbl.polygon[1]


# In[150]:


p1=tbl.representative_point()[1]


# # Test if point is within polygon (from representative point)

# In[148]:


p0.within(poly0)


# In[151]:


p1.within(poly1)


# In[152]:


p0.within(poly1)


# In[153]:


p1.within(poly0)


# ## Joining http://geopandas.org/mergingdata.html

# # Test if polygons are valid shapes

# In[74]:


tbl.is_valid

