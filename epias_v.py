#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install requests


# In[2]:


pip  install pandas


# In[3]:


import requests
import openpyxl
from openpyxl.styles import Alignment
from openpyxl import Workbook
import pandas as pd


# In[4]:


url1 = 'https://seffaflik.epias.com.tr/transparency/service/market/intra-day-trade-history?endDate=2022-01-26&startDate=2022-01-26'
response = requests.get(url1).json()
conract_grup = {}
def parser_data(data):
   
    for transcation in data['body']['intraDayTradeHistoryList']:
        if not transcation['conract'].startswith('PH'):
            continue
        if transcation['conract'] not in conract_grup:
            conract_grup[transcation['conract']] = {
                'date':f"{transcation['conract'][6:8]}.{transcation['conract'][4:6]}.20{transcation['conract'][2:4]} {transcation['conract'][8:10]}:00",
                'Toplam İşlem Tutar': transcation['price'] * transcation['quantity'] / 10,
                'Toplam İşlem Miktarı': transcation['quantity'] / 10
            }
            conract_grup[transcation['conract']]['Ağırlıklı Ortalama Fiyat'] = conract_grup[transcation['conract']][ 'Toplam İşlem Tutar']/conract_grup[transcation['conract']]['Toplam İşlem Miktarı']
        else:
            conract_grup[transcation['conract']][ 'Toplam İşlem Tutar'] += transcation['price'] * transcation['quantity'] / 10
            conract_grup[transcation['conract']]['Toplam İşlem Miktarı']+= transcation['quantity'] / 10
            conract_grup[transcation['conract']]['Ağırlıklı Ortalama Fiyat'] = conract_grup[transcation['conract']][ 'Toplam İşlem Tutar']/conract_grup[transcation['conract']]['Toplam İşlem Miktarı']
    return conract_grup


# In[14]:



def main():
    url1 = 'https://seffaflik.epias.com.tr/transparency/service/market/intra-day-trade-history?endDate=2022-01-26&startDate=2022-01-26'
    response = requests.get(url1).json()
    data = parser_data(response)
    print(data)
main()


# In[ ]:





# In[ ]:




