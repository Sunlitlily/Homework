#!/usr/bin/env python
# coding: utf-8

# In[25]:


import random
import re
import string

N = int(input())
russian_lower_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
russian_letters = russian_lower_letters + russian_lower_letters.upper()
isGood = False
while isGood != True:
    password = ''.join(random.choices(string.digits + string.ascii_letters + string.punctuation + russian_letters, k = N))
    match = re.search(r'[A-ZА-Я]{2}', password)
    if not match:
        continue
    match = re.search(r'[a-zа-я]{2}', password)
    if not match:
        continue
    match = re.search(r'[0-9]{3}', password)
    if match:
        continue
    match1 = re.search(r'[A-Za-z].*[А-Яа-я]', password)
    match2 = re.search(r'[А-Яа-я].*[A-Za-z]', password)
    if not (match1 or match2):
        continue
    isGood = True
print(password)


# In[ ]:




