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

# lendo dados
data = pd.read_csv('igrfgridData1960-2020.csv')

fig, ax = plt.subplots()

def animation_frame(ano):
    df = data[data.Date == ano]
    ax.set_title(ano)
    return ax.scatter(df.Lon,df.Lat,c=df.Bt)

# gerando animação
anos = np.arange(1960,2021,1)
animation = FuncAnimation(fig, func=animation_frame, frames=anos, interval=1000)

print("Salvando ...")
animation.save('animation.mp4', writer=PillowWriter(fps=1))
#plt.show()