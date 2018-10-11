
# coding: utf-8

# In[1]:


from sklearn import tree


# In[2]:


#height, weight, shoesize
x = [[170, 75, 41], [175, 77, 43], [165, 80, 43], [160, 71, 38],[180, 90, 47], [185, 80, 42], [155, 58, 36], [157, 78, 40], [167, 67, 40],[177, 83, 44]]


# In[3]:


y = ['male', 'male', 'female','female', 'female', 'male', 'female', 'male', 'male', 'female']


# In[4]:


clf = tree.DecisionTreeClassifier()


# In[5]:


clf = clf.fit(x,y)


# In[13]:


prediction = clf.predict([[175,75,40]])


# In[14]:


print (prediction)

