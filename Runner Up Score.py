
# coding: utf-8

# In[12]:


n = int(input())
arr = map(int, input().split())
list_numbe = list(arr)
list_number = []
new = []
a = sorted(list_numbe,reverse=True )
high = int(max(a))
for high in a:
    if high not in new:
        new.append(high)
new.remove(max(new))
print(max(new))

