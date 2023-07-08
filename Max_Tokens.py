#!/usr/bin/env python
# coding: utf-8

# In[4]:


import openai


# In[1]:


from dotenv import dotenv_values


# In[2]:


config = dotenv_values(".env")


# In[5]:


openai.api_key=config["OPENAI_API_KEY"]


# In[19]:


response = openai.Completion.create(
                          model="text-davinci-003",
                          max_tokens = 200,
                          stop = "10.",
                          prompt = "Best movies of all times :  ")


# In[20]:


print(response["choices"][0]["text"])


# In[ ]:




