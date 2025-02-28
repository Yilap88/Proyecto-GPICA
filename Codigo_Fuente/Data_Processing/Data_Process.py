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
df, meta = pyreadstat.read_sav('Data/Data_raw/EHPM_2020.sav')
print(df.head())
  