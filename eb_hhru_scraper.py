# -*- coding: utf-8 -*-
"""
Created on Sun May 24 08:42:38 2020

@author: Eduard Babushkin / https://vk.com/id5871581 / https://vk.com/public24508526
        https://edwvb.blogspot.com/2018/02/kak-ya-skachivayu-parsit-vakansii-kompanij-s-hh-ru-na-primere-gazproma.html
"""
#%%
import numpy as np
import requests
from tqdm import tqdm_notebook
import pandas as pd
import re
#%%
r = requests.get ('https://api.hh.ru/vacancies?text=python&only_with_salary=true') .json () 

#%%
vac = []
for i in tqdm_notebook (range (0, 13)):
    vac.append (requests.get ("https://api.hh.ru/vacancies?text=python&only_with_salary=true", params = {'page': i, 'per_page': 100}) .json ())
    
#%%
#%%
vah = []
for i in tqdm_notebook(range(0, 13)):
    for j in tqdm_notebook(range(0, 100)):
        vah.append(requests.get("https://api.hh.ru/vacancies?text=python&only_with_salary=true", params={'page': i, 'per_page': 100}) .json ()['items'] [j] ['alternate_url'])
#%%
lulu = [re.sub(r'[^0-9]', '', e) for e in vah]
vak_url = 'https://api.hh.ru/vacancies/{}'
#%%
var = []
for i in lulu:
    var.append(requests.get(vak_url.format(i)).json())
#%%
df = pd.DataFrame(var)
#%%
df.to_csv('hhru_python_jobs.csv',index=False, header=True)
#%%
#%%
#%%        
#%%        
#%%        
#%%        
#%%        
#%%        
#%%        