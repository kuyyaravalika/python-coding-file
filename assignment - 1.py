#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. write a python program to convert a string to lower case


# In[2]:


x="RAVALIKA"
x.lower()


# In[3]:


#2. write a python program to convert only odd indexed characters to lower case


# In[8]:


var="python"
var[0].upper()+var[1].lower()+var[2].upper()+var[3].lower()+var[4].upper()+var[5].lower()


# In[9]:


#3. write a python program to convert only even index characters to lower case


# In[10]:


var="python"
var[0].upper()+var[1].upper()+var[2].lower()+var[3].upper()+var[4].lower()+var[5].upper()


# In[11]:


#4. write a python program to convert only odd indexed characters to upper case


# In[13]:


var="python"
var[0].lower()+var[1].upper()+var[2].lower()+var[3].upper()+var[4].lower()+var[5].upper()


# In[ ]:


#5.write a python progaram to convert only even indexed characters to upper case


# In[14]:


var="python"
var[0].upper()+var[1].lower()+var[2].upper()+var[3].lower()+var[4].upper()+var[5].lower()


# In[24]:


#6. write a python program where you have different variable which contains your name,sex,age,phone no,father name and mother name.and by using this variable create a
name=input("enter your name")
sex=input("enter your gender")
age=int(input("enter your age"))
phone_no=int(input("enter your phone_number"))
fathersname=input("enter your father name")
mothername=input("enter your mother name")
bio_data="my name is {} my gender {} my age is {} my phone_no is {} my fathersname is {} my mothersname is {}"
print("bio_data".format)



# In[20]:


#7. write a python program to count how many times "@" occured


# In[23]:


y="2@@@@@@@ytefcf@"
y.count("@")


# In[49]:


#8.write a python program to get only name from the string "name1.@gmail.com'name2.@gmail.com,name3.@gmail.com"
z="name1.@gmail.com'name2.@gmail.com,name3.@gmail.com"
name1="name1.@gmail.com"
name2="name2.@gmail.com"
name3="name3.@gmail.com"
print(z.replace("name1.@gmail.com","name1")[0:5])
print(z.replace("name2.@gmail.com","name2")[17:22])
print(z.replace("name3.@gmail.com","name3")[34:40])       


# In[48]:


#9.give a string of odd length greater that 9,return a new string made of the middle three characters of a given string


# In[33]:


var1="mynameissan"
var1[4:7]


# In[26]:


#10.write a python program to insert a 2 string in the middle of 1 string


# In[28]:


str1="myn"
str2="sa"
str1[0:1]+str2+str1[1:3]


# In[29]:


#11. write a program to remove vowel from the entire alphbets ex:"abcdefghijklmnopqrstuvwxy"


# In[30]:


a="abcdefghijklmnopqrstuvwxyz"
a[1:4]+a[5:8]+a[9:14]+a[15:20]+a[21:26]


# In[ ]:




