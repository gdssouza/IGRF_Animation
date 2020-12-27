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
    return ax.scatter(df.Lon, df.Lat, c=df.Bt,\
                          transform = ccrs.PlateCarree(),\
                          cmap = plt.cm.RdBu_r)

# gerando animação
anos = np.arange(1960, 2021, 1)
animation = FuncAnimation(fig, func=animation_frame, frames=anos, interval=10)

print("Salvando ...")
animation.save('animation.gif', writer=PillowWriter(fps=40))