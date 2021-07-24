# %%
import rasterio
import rasterio.plot
import pyproj
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Arquivos de satélite na nuvem
filepath = 'http://landsat-pds.s3.amazonaws.com/c1/L8/042/034/LC08_L1TP_042034_20170616_20170629_01_T1/LC08_L1TP_042034_20170616_20170629_01_T1_B4.TIF'

print('Landsat na AWS:')
with rasterio.open(filepath) as src:
    print(src.profile)

'Traçar uma visão geral de baixa resolução'
# A grade de valores raster pode ser acessada como uma matriz numpy e plotada:
with rasterio.open(filepath) as src:
   oviews = src.overviews(1) # lista de visões gerais do maior ao menor
   oview = oviews[-1] # vamos olhar para a menor miniatura
   print('\nFator de dizimação = {}'.format(oview))

   thumbnail = src.read(1, out_shape=(1, int(src.height // oview), int(src.width // oview)))

print('\nTipo array: ',type(thumbnail))
print(thumbnail)

plt.imshow(thumbnail)
plt.colorbar()
plt.title('Overview - Banda 4 {}'.format(thumbnail.shape))
plt.xlabel('Coluna #')
plt.ylabel('Linha #')
plt.show()
