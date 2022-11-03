#!/usr/bin/env python
# coding: utf-8

# In[5]:


pip install opencv-python


# In[6]:



import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[9]:


#reading image
img=cv.imread("begin 2")
cv.imshow('cat',img)
cv.waitKey(60)


# In[ ]:





# In[ ]:




