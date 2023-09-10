#!/usr/bin/env python
# coding: utf-8

# In[17]:


def revstr(str1):
    news=""
    l=str1.split(" ")
    for i in l:
        m=i
        str=""
        for k in m:
            str=k+str
        news=news+" "+str
        
        
    return news
str1="technovert solutions"
print(revstr(str1))


# In[ ]:




