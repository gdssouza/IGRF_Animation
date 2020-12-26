# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 18:04:12 2020

@author: Anon
"""

# importando pandas
import pandas as pd

# informações dos arquivos
caminho = 'dados_NOAA/igrfgridData'
cab = ['Date','Lat','Lon','Elevation','Bt','Bt_sv']
anos = ["1960-1980","1980-2000","2000-2020"]

# concatenando
df = pd.DataFrame({})
for intervalo in anos:
    df2 = pd.read_csv(caminho+intervalo+'.csv',skiprows=13,sep=',',names=cab)
    df = pd.concat([df, df2])

# definindo data como index
df3 = df.set_index('Date')

# visualizando
print(df3.head())

# salvando
df3.to_csv(caminho+"1960-2020.csv")