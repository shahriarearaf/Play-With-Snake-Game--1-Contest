
# coding: utf-8

# In[ ]:


string_in = input()
string_in = list(string_in)
sub_string = input()
count = 0
for i in range(len(string_in)):
    if string_in[i].startswith(sub_string[1]):
        count += 1
print(str(count))

