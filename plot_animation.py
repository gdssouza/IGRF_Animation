# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 18:47:53 2020

@author: Anon
"""

# importando bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import cartopy.crs as ccrs

anos = np.arange(1960, 2021, 1)
projection = ccrs.Orthographic(central_latitude=90.0)

# lendo dados
data = pd.read_csv('igrfgridData1960-2020.csv')

fig = plt.figure(figsize=(18,9))
ax = plt.axes( projection = projection )
ax.coastlines()
ax.gridlines()

def animation_frame(ano):
    df = data[data.Date == ano]
    ax.set_title(ano)
    scat = ax.scatter(df.Lon, df.Lat, c=df.Bt,\
                  transform = ccrs.PlateCarree(),\
                  cmap = plt.cm.RdBu_r)
    #print("Plotando IGRF de",ano)
    return scat

fig.colorbar(animation_frame(anos[0]),
             label='Totalintensity in nanoTesla (nT)')

# gerando animação
animation = FuncAnimation(fig, func=animation_frame, frames=anos)
        
print("Salvando ...")
animation.save('animation.gif', writer=PillowWriter(fps=5))