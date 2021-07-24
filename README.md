# RasterIO_Satellite_Imagery_Processing
Processamento de imagens de satelito via RasterIO, Numpy e Matplotlib.

Objetivo é acessar as imagens disponibilizadas pelo satelite LandSat-8 que estão armazenadas em um Bucket S3 na cloud da AWS e processar essas imagens.


## Instalando GDAL e RasterIO
Acessar o link abaixo e baixar os arquivos GDAL e rasterio:

Link: https://www.lfd.uci.edu/~gohlke/pythonlibs/#rasterio

Arquivos:
GDAL-3.1.4-cp36-cp36m-win_amd64.whl
rasterio-1.1.8-cp36-cp36m-win_amd64.whl

- Abra o cmd em modo admin, entre na pasta onde os arquivos estão e execute o comando abaixo:

pip install GDAL-3.1.4-cp36-cp36m-win_amd64.whl rasterio-1.1.8-cp36-cp36m-win_amd64.whl

![image](https://user-images.githubusercontent.com/40063504/126878021-1bbcdde6-6e97-4342-b149-101d3a1f6c55.png)


## Resultados

### Script - 0_landsat_aws

![banda_4](https://user-images.githubusercontent.com/40063504/126877898-a64bdc79-1a20-45e3-a683-e0c3dade0f98.png)

### Script - 1_calculo_nvdi

![ndvi](https://user-images.githubusercontent.com/40063504/126877899-01192e7e-4863-4083-99f2-824c9d904f14.png)

### Script - 2_mudanca_NDVI_tempo

![ndvi_dif](https://user-images.githubusercontent.com/40063504/126877904-8183e326-f689-42e6-b6d0-16f090850f8a.png)
