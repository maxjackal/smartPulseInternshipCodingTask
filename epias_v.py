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
#kullanacağım modülleri import ettim


# In[4]:


url1 = 'https://seffaflik.epias.com.tr/transparency/service/market/intra-day-trade-history?endDate=2022-01-26&startDate=2022-01-26'
response = requests.get(url1).json()
conract_grup = {}
def parser_data(data):
   
#url'e get isteği atıp verileri json fromatın dönüştürdüm
#conract_grup adında boş bir sözlük oluşturdum
#parser_data fonksiyonu oluşturup data'nın verilerini döndürmesini sağladım

    for transcation in data['body']['intraDayTradeHistoryList']:
        if not transcation['conract'].startswith('PH'):
#intraDayTradeHistoryList listesindeki transcation sözlüğü için işlem yapılır
#eğer PH ile başlamıyorsa döngü sonraki adıma geçer
            continue
        if transcation['conract'] not in conract_grup:
            conract_grup[transcation['conract']] = {
                'date':f"{transcation['conract'][6:8]}.{transcation['conract'][4:6]}.20{transcation['conract'][2:4]} {transcation['conract'][8:10]}:00",
                'Toplam İşlem Tutar': transcation['price'] * transcation['quantity'] / 10,
                'Toplam İşlem Miktarı': transcation['quantity'] / 10
            }
            conract_grup[transcation['conract']]['Ağırlıklı Ortalama Fiyat'] = conract_grup[transcation['conract']][ 'Toplam İşlem Tutar']/conract_grup[transcation['conract']]['Toplam İşlem Miktarı']
   #conract_grup sözlüğünde ilgili conract yoksa, yeni bir sözlük oluştururuz
   #belirli verileri bu sözlükte tutarız yani sözleşmenin tarihi, toplam işlem tutarı ve toplam işlem
   #miktarı ve ağırlıklı ortalama fiyat hesaplanarak da bu sözlüğe eklenir
        else:
            conract_grup[transcation['conract']][ 'Toplam İşlem Tutar'] += transcation['price'] * transcation['quantity'] / 10
            conract_grup[transcation['conract']]['Toplam İşlem Miktarı']+= transcation['quantity'] / 10
            conract_grup[transcation['conract']]['Ağırlıklı Ortalama Fiyat'] = conract_grup[transcation['conract']][ 'Toplam İşlem Tutar']/conract_grup[transcation['conract']]['Toplam İşlem Miktarı']
   #eğer conract_grup sözlüğünde conract adı mevcut ise
   #sözleşmenin toplam işlem tutarına ve toplam işlem miktarına ilgili işlemin değerini ekler
   #ağırlıklı ortalama fiyat da yeniden hesaplanır
    return conract_grup
#conract_grup sözlüğünü döndürür

# In[14]:



def main():
    url1 = 'https://seffaflik.epias.com.tr/transparency/service/market/intra-day-trade-history?endDate=2022-01-26&startDate=2022-01-26'
    response = requests.get(url1).json()
    data = parser_data(response)
    print(data)
main()


# In[ ]:





# In[ ]:




