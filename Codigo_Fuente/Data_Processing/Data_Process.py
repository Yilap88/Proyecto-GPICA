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
print(df)

### Filtramos las personas que conocen la app de Chivo (p12)
df = df[df['p12'] == "Sí"]
print(df['p12'])
df = df.rename(columns={'p12': 'Are you familiar with Chivo Wallet?'})


### Creamos una variable para las personas que tienen celular con internet
df['p9A'] = np.where(df['_v1'] == 'Sí, en celular/teléfono móvil propio', 1, 0)
df['p9B'] = np.where(df['_v2'] == 'Sí, en celular/teléfono móvil propio', 1, 0)
df['Cellphone with internet'] = np.where( (df['p9A'] == 1) | (df['p9B'] == 1), 'Sí', 'No')

### Creamos una variable para las personas que están Bancarizadas
df['Unbanked'] = np.where( (df['_v5'] == 'Ninguno'), 'No', 'Sí')

### Creamos una variable para categorizar la educación
df['Years of schooling'] = np.where( (df['educ'] == 'Superior'), 'High School+', 'Middle School')

### Creamos una variable para categorizar la edad
df['Age'] = np.where( (df['educ'] == 'Superior'), 'High School+', 'Middle School')



df.to_excel('Data/Data_procesada/Data_Processed.xlsx', index=False)

  
