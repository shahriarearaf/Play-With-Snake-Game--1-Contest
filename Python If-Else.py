
# coding: utf-8

# In[12]:


n = int(input())

if 1 <= n <= 100:
    if n % 2 != 0:
        print('Weird')
    elif n % 2 == 0:
        if 2 <= n <= 5:
            print("Not Weird")
        elif 6 <= n <= 20:
            print("Weird")
        elif n >=20:
            print('Not Weird')
    

