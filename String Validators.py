
# coding: utf-8

# In[ ]:


string_in = input()
string_list = list(string_in)
a,b,c,d,e = False,False,False,False,False
for i in range (len(string_list)):
    if string_list[i].isalnum() :
        a = 'True'
    if string_list[i].isalpha() :
        b = 'True'
    if string_list[i].isdigit():
        c = 'True'
    if string_list[i].islower() :
        d = 'True'
    if string_list[i].isupper():
        e = 'True'
print(str(a)+'\n'+str(b)+'\n'+str(c)+'\n'+str(d)+'\n'+str(e))

