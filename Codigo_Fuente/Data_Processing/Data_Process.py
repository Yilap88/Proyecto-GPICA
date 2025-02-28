#### El siguiente script lee los datos de la "Encuesta de Hogares de Propositos Multiples (EHPM)" y los procesa.

### Llamamos los paquete a usar
import pandas as pd
import numpy as np
import os #paquete nativo de python
import pyreadstat


### Nos dirigimos al directorio main para trabajar comodamente
rutaactual = os.path.abspath(__file__)  # Ruta completa del script (incluyendo nombre del scrip)
dirsup2 = os.path.dirname(os.path.dirname(os.path.dirname(rutaactual))) # subimos al directorio /main/
os.chdir(dirsup2)


### Cargamos la base de datos .sav
df = pd.read_stata('Data/Data_raw/Survey_original.dta')
print(df.head())



  
