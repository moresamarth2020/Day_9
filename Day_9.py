#!/usr/bin/env python
# coding: utf-8

# # if-else Statements
# - Sometimes the programmer needs to check the evaluation of certain expression(s), whether the expression(s) evaluate to True or False. If the expression evaluates to False, then the program execution follows a different path than it would have if the expression had evaluated to True.
# - Based on this, the conditional statements are further classified into following types:
# * if
# * if-else
# * if-else-elif
# * nested if-else-elif.
# ### An if……else statement evaluates like this:
# - if the expression evaluates True:
# - Execute the block of code inside if statement. After execution return to the code out of the if……else block.\
# - if the expression evaluates False:
# - Execute the block of code inside else statement. After execution return to the code out of the if……else block.

# In[13]:


a = int(input("Enter Your Age:"))
if (a>18):
    print('You can drive Car',a)
else:
    print('You can anot drive carr',a)


# In[14]:


# The conditional operators:
# print(a>b)
# print(a<=b)
# print(a==b)
# print(a!=b)


# In[ ]:


applePrice = 210
budget = 200
if (applePrice <= budget):
    print("Alexa, add 1 kg Apples to the cart.")
else:
    print("Alexa, do not add Apples to the cart.")


# In[17]:


apple_price = 220
budget = 150
if (apple_price <= budget):
    print("Alexa, add 1 kg Apple to the Cart.")
else:
    print("Alexa, do not add Apple to the Cart.")


# ### elif Statements
# - Sometimes, the programmer may want to evaluate more than one condition, this can be done using an elif statement.
# * Working of an elif statement:
# - Execute the block of code inside if statement if the initial expression evaluates to True. After execution return to the code out of the if block.
# - Execute the block of code inside the first elif statement if the expression inside it evaluates True. After execution return to the code out of the if block. 
# - Execute the block of code inside the second elif statement if the expression inside it evaluates True. After execution return to the code out of the if block.
# - Execute the block of code inside the nth elif statement if the expression inside it evaluates True. After execution return to the code out of the if block.
# - Execute the block of code inside else statement if none of the expression evaluates to True. After execution return to the code out of the if block.

# In[21]:


num = 0
if (num < 0):
    print("Number is negative.")
elif (num == 0):
    print("Number is Zero.")
else:
    print("Number is positive.")


# In[23]:


num = int(input("Enter a Number:"))
if (num < 0):
    print("Number is Negative.")
elif (num == 0):
    print("Number is Zero.")
elif (num == 24):
    print("Number is special.")
else:
    print("Number is positive")
print("I am Happy Now!")


# ### Nested if statements:
# We can use if, if-else, elif statements inside other if statements as well.

# In[25]:


num = int(input("Enter a Number:"))
if(num<0):
    print("Number is Negative.")
elif(num>0):
    if(num<=10):
        print("Number is Betwen 0-10")
    elif(num>10 and num<=20):
        print("Number is Between 10-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is Negative")


# In[ ]:




