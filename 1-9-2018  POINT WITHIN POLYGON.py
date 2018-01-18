
# coding: utf-8

# In[1]:


from shapely.geometry import Point, Polygon
# Create Point objects
p1 = Point(24.952242, 60.1696017)
p2 = Point(24.976567, 60.1612500)


# Create a Polygon
coords = [(24.950899, 60.169158), (24.953492, 60.169158), (24.953510, 60.170104), (24.950958, 60.169990)]
poly = Polygon(coords)


# In[2]:


print (p1)


# In[3]:


print (p2)


# In[4]:


print (poly)


# In[5]:


p1.within(poly)


# In[6]:


p2.within (poly)


# In[7]:


p1.contains(poly)


# In[8]:


p2.contains(poly)

