# %%
import rasterio
import rasterio.plot
import pyproj
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

' Indicador - NDVI '
def calc_ndvi(nir,red):
    '''Calcular NDVI a partir de matrizes inteiras'''
    nir = nir.astype('f4')
    red = red.astype('f4')
    ndvi = (nir - red) / (nir + red)
    return ndvi

# Imagens de 2016
date = '2017-06-16'
url = 'http://landsat-pds.s3.amazonaws.com/c1/L8/042/034/LC08_L1TP_042034_20170616_20170629_01_T1/'
redband = 'LC08_L1TP_042034_20170616_20170629_01_T1_B{}.TIF'.format(4)
nirband = 'LC08_L1TP_042034_20170616_20170629_01_T1_B{}.TIF'.format(5)

# Imagens de 2019
date2 = '2018-06-19'
url2 = 'http://landsat-pds.s3.amazonaws.com/c1/L8/042/034/LC08_L1TP_042034_20180619_20180703_01_T1/'
redband2 = 'LC08_L1TP_042034_20180619_20180703_01_T1_B{}.TIF'.format(4)
nirband2 = 'LC08_L1TP_042034_20180619_20180703_01_T1_B{}.TIF'.format(5)


' BANDA 4 - Vermelha'
# 2016
with rasterio.open(url+redband) as src:
    profile = src.profile
    oviews = src.overviews(1) # lista de visões gerais do maior ao menor
    oview = oviews[1]  # Use a visão geral de segunda maior resolução
    print('Fator de dizimação = {}'.format(oview))
    red = src.read(1, out_shape=(1, int(src.height // oview), int(src.width // oview)))

# 2019
filepath = url2+redband2
with rasterio.open(filepath) as src:
    print('Opening:', filepath)
    oviews = src.overviews(1) # lista de visões gerais do maior ao menor
    oview = oviews[1]  # Use a visão geral de segunda maior resolução
    print('Decimation factor= {}'.format(oview))
    red2 = src.read(1, out_shape=(1, int(src.height // oview), int(src.width // oview)))


' BANDA 5 - Infravermelho próximo'
# 2016
with rasterio.open(url+nirband) as src:
    oviews = src.overviews(1) # lista de visões gerais do maior ao menor
    oview = oviews[1]  # Use a visão geral de segunda maior resolução
    nir = src.read(1, out_shape=(1, int(src.height // oview), int(src.width // oview)))

# 2019
filepath = url2+nirband2
with rasterio.open(filepath) as src:
    print('Opening:', filepath)
    oviews = src.overviews(1) # lista de visões gerais do maior ao menor
    oview = oviews[1]  # Use a visão geral de segunda maior resolução
    print('Decimation factor= {}'.format(oview))
    nir2 = src.read(1, out_shape=(1, int(src.height // oview), int(src.width // oview)))

# Calculo do NDVI
ndvi = calc_ndvi(nir,red)
ndvi2 = calc_ndvi(nir2, red2)

# Plotando os resultados:
fig, axes = plt.subplots(1,3, figsize=(14,6), sharex=True, sharey=True)

plt.sca(axes[0])
plt.imshow(ndvi, cmap='RdYlGn', vmin=-1, vmax=1)
plt.colorbar(shrink=0.5)
plt.title('NDVI {}'.format(date))
plt.xlabel('Coluna #')
plt.ylabel('Linha #')

plt.sca(axes[1])
plt.imshow(ndvi2, cmap='RdYlGn', vmin=-1, vmax=1)
plt.colorbar(shrink=0.5)
plt.title('NDVI {}'.format(date2))

plt.sca(axes[2])
plt.imshow(ndvi2 - ndvi, cmap='bwr', vmin=-1, vmax=1)
plt.colorbar(shrink=0.5)
plt.title('Diferença entre datas:\n ({} - {})'.format(date2, date))
plt.show()










