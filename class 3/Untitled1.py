#!/usr/bin/env python
# coding: utf-8

# # Text Formating/formation/concatation

# In[4]:


first_name ="Muhammad Bilal"
print(first_name)


# In[5]:


a=len("Bilal")
print(a)


# In[7]:


a= print("Bilal") #print function doesnot return a value
print(a)


# # Concatination
# * **+**
# * variable_name.format(var1,var2,var3)
# * `f'Students name:{var1}'`

# In[10]:


first_name = "Muhammad Bilal "
Last_name ="Hamid"
institute_name="Saylani mass IT Training"
age = str(22)
card = "Institute Name: "+ institute_name + "\nstudents name: "+first_name+Last_name + "\nAge: "+age
print(card)


# In[13]:


card="""
Institute Name: {}
students name: {} {}
Age: {}
""".format(institute_name,firstname,Last_name,age)
print(card)


# In[15]:


card="""
Institute Name: {0}
students name: {1} {2}
Age: {3}
""".format(institute_name,firstname,Last_name,age)
#                0            1         3      4
print(card)


# In[18]:


first_name = "Muhammad Bilal "
Last_name ="Hamid"
institute_name="Saylani mass IT Training"
age = str(22)


card=f"""
Institute Name: {institute_namen}
students name: {first_name} {Last_name}
Age: {age}
""".format(institute_name,firstname,Last_name,age)

print(card)


# In[26]:


first_name = "Muhammad Bilal "
Last_name ="Hamid"
institute_name="Saylani mass IT Training"
age = 22
    
card=f"""Institute Name:%s
students name: %s %s
Age: %d
""" % (institute_name,firstname,Last_name,age)

print(card)


# In[27]:


print(card.capitalize()) #first letter would be capitalized


# In[28]:


print(card.casefold()) #everthing would be lowercase


# In[29]:


print(card.lower()) #everthing would be lowercase


# In[ ]:


print(card.casefold()) #everthing would be small 


# In[33]:


print(card) 
card.casefold().count("a")


# In[ ]:





# In[ ]:





# In[ ]:




