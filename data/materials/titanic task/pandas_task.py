#!/usr/bin/env python
# coding: utf-8

# In[32]:


import pandas as pd


# ### Titanic data

# In[33]:


df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')


# In[34]:


df


# In[35]:


df.Name = df.Name.apply(lambda x : x.split(' ')[0])


# In[36]:


df.Name = df.Name.str.replace(',','').str.strip()


# In[37]:


df.astype({'Survived': 'category'})


# In[38]:


df.Survived = df.Survived.astype('category')


# In[39]:


df


# In[43]:


df.to_csv('titanic.csv', index= False)


# In[44]:


df1 = pd.read_csv('titanic.csv')


# In[45]:


df1


# In[46]:


df1.dtypes


# In[47]:


#1 . Find out how many male and female passenger was onboarded .
df.Sex.value_counts()


# In[52]:


#2. how many survived we have.
df['Survived'][df.Survived == 1].count()


# In[54]:


#3. how many casuality we have
df['Survived'][df.Survived == 0].count()


# In[57]:


#. what is name of a person who is the eldest one . 
df[['Name', 'Age']][df.Age == max(df.Age)]


# In[61]:


#5 . how many passenger do we have in first , second and third class 
df.Pclass.value_counts(sort = True)


# In[68]:


#6. how many person we have whose name starts with "s"
df['Name'][df['Name'].str.lower().str.startswith('s')].count()


# In[69]:


#7. try to create a new column which is a summation  of "SibSp" and "parch"

df['N_col'] = df.Parch + df.SibSp


# In[70]:


df


# In[73]:


#8 . how many person do we have below age of 25 .
df['Name'][df.Age < 25].count()


# In[74]:


#9 . how many person died whose age was less then 40 
df['Name'][(df.Age < 40) & (df.Survived == 0)].count()


# In[139]:


#10 . from a  cabin column seperate text and numeric value . 
def spliter(s):
    
    digit = ''
    text = ''
    if type(s) == str:

        for i in s:
            if i in ('0123456789'):
                digit += i
            else:
                text += i
                    
    return digit, text
df.Cabin.apply(lambda x : [x if type(x) != str else spliter(x)][0])


# ### Bank Data

# In[140]:


df2 = pd.read_csv(r'C:\Users\gopip\Downloads\bank.csv', sep = ';')


# In[141]:


df2.columns = df2.columns.str.title()


# In[142]:


df2


# In[144]:


#1 . how many campaign available in this dataset . 
df2['Campaign'].nunique()


# In[155]:


#2 . how many users do we have with housing and personal loan . 

len(df2[(df2.Housing == 'yes') & (df2.Loan == 'yes')])


# In[157]:


#3. how many person do we have whose age is 60+ . 
len(df2[df2.Age > 60])


# In[166]:


#4 . in which month we have trageted most of the customer .
df2['Month'].value_counts(sort = True, ascending= False)[0:1]


# In[169]:


#5 . which mode of call is giving you more result
df2['Contact'][df2.Poutcome == 'success'].value_counts(sort = True, ascending= False)[0:1]


# In[178]:


#6 . how many enterpeures do we have in this list 
df2['Job'][df2.Job == 'entrepreneur'].value_counts()


# In[180]:


#7 . how many customers do we have with negative balance 
len(df2[(df2.Balance < 0)])


# In[198]:


#8. prepare a group of data based on education level .
df2.groupby('Education').describe().T


# In[201]:


df2.groupby('Education').describe(include = 'object')


# In[ ]:




