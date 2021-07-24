# %%
import rasterio
import rasterio.plot
import pyproj
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

'''
O Índice de Vegetação por Diferença Normalizada é um indicador simples que pode ser usado para avaliar 
se o alvo inclui vegetação saudável. Este cálculo usa duas bandas de um conjunto de dados de imagem multiespectral, 
as bandas do vermelho e do infravermelho próximo (NIR):

Para este tutorial, usaremos as bandas NIR e Red de uma cena Landsat-8 acima de parte do vale central e da 
Sierra Nevada na Califórnia. Estaremos usando conjuntos de dados Nível 1TP , imagens ortorretificadas projetadas 
em mapas contendo dados calibrados radiometricamente.

## Bandas
- Vermelho: Banda 4
- Infravermelho próximo: banda 5

Por causa da longevidade da missão de aterrissagem e porque diferentes sensores no satélite registram dados 
em diferentes resoluções, essas bandas são armazenadas individualmente como arquivos raster de banda única. 
Alguns outros rasters podem armazenar várias bandas no mesmo arquivo.
'''


# Use a mesma imagem de exemplo:
date = '2017-06-16'
url = 'http://landsat-pds.s3.amazonaws.com/c1/L8/042/034/LC08_L1TP_042034_20170616_20170629_01_T1/'
redband = 'LC08_L1TP_042034_20170616_20170629_01_T1_B{}.TIF'.format(4)
nirband = 'LC08_L1TP_042034_20170616_20170629_01_T1_B{}.TIF'.format(5)

' BANDA 4 - Vermelha'
with rasterio.open(url+redband) as src:
    profile = src.profile
    oviews = src.overviews(1) # lista de visões gerais do maior ao menor
    oview = oviews[1]  # Use a visão geral de segunda maior resolução
    print('Fator de dizimação = {}'.format(oview))
    red = src.read(1, out_shape=(1, int(src.height // oview), int(src.width // oview)))

#plt.imshow(red)
#plt.colorbar()
#plt.title('{}\nRed {}'.format(redband, red.shape))
#plt.xlabel('Coluna #')
#plt.ylabel('Linha #')
#plt.show()


' BANDA 5 - Infravermelho próximo'
with rasterio.open(url+nirband) as src:
    oviews = src.overviews(1) # lista de visões gerais do maior ao menor
    oview = oviews[1]  # Use a visão geral de segunda maior resolução
    nir = src.read(1, out_shape=(1, int(src.height // oview), int(src.width // oview)))

#plt.imshow(nir)
#plt.colorbar()
#plt.title('{}\nNIR {}'.format(nirband, nir.shape))
#plt.xlabel('Coluna #')
#plt.ylabel('Linha #')
#plt.show()

' Indicador - NDVI '
def calc_ndvi(nir,red):
    '''Calcular NDVI a partir de matrizes inteiras'''
    nir = nir.astype('f4')
    red = red.astype('f4')
    ndvi = (nir - red) / (nir + red)
    return ndvi

ndvi = calc_ndvi(nir,red)
plt.imshow(ndvi, cmap='RdYlGn')
plt.colorbar()
plt.title('NDVI {}'.format(date))
plt.xlabel('Coluna #')
plt.ylabel('Linha #')
plt.show()