#### El siguiente script lee los datos de la "Encuesta de Hogares de Propositos Multiples (EHPM)" y los procesa.

### Llamamos los paquete a usar
import pandas as pd
import numpy as np
import os #paquete nativo de python
import pyreadstat

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score



#import statsmodels.api as sm



### Nos dirigimos al directorio main para trabajar comodamente
rutaactual = os.path.abspath(__file__)  # Ruta completa del script (incluyendo nombre del scrip)
dirsup2 = os.path.dirname(os.path.dirname(os.path.dirname(rutaactual))) # subimos al directorio /main/
os.chdir(dirsup2)


### Cargamos la base de datos .sav
df = pd.read_stata('Data/Data_raw/Survey_original.dta')
print(df)


### Ajustamos la variable de las personas que conocen la app de Chivo (pregunta 12)
df = df.rename(columns={'p12': 'Are_you_familiar_with_Chivo_Wallet'})
df['Are_you_familiar_with_Chivo_Wallet'] = df['Are_you_familiar_with_Chivo_Wallet'].replace({'Sí': '1', 'No': '0'})


### Ajustamos la variable de las personas que intentaron usar Chivo (pregunta 14)
df = df.rename(columns={'p14': 'Have_you_tried_to_Download_Chivo_Wallet'})
df['Have_you_tried_to_Download_Chivo_Wallet'] = df['Have_you_tried_to_Download_Chivo_Wallet'].replace({'Sí, un amigo o familiar lo hizo por mí': 1, 'Sí, lo intenté yo mismo': 1 ,
                                                                                                         'No': 0, '':0})


### Creamos una variable para las personas que tienen celular con internet (pregunta 9 - opciones v1 a v4)
df['p9A'] = np.where(df['_v1'] == 'Sí, en celular/teléfono móvil propio', 1, 0)
df['p9B'] = np.where(df['_v2'] == 'Sí, en celular/teléfono móvil propio', 1, 0)
df['Cellphone_with_internet'] = np.where( (df['p9A'] == 1) | (df['p9B'] == 1), 1, 0) # 1 significa afirmativo para Cellphone with internet


### Creamos una variable para las personas que están Bancarizadas (pregunta 10 - opciones v5 a v11)
df['Unbanked'] = np.where( (df['_v5'] == 'Ninguno'), 1, 0) # 1 significa unbanked


### Creamos una variable para categorizar la educación (pregunta 5 - llamada educ en los datos originales)
df = df.rename(columns={'educ': 'Years_of_schooling'})
df['Years_of_schooling'] = df['Years_of_schooling'].replace({'Superior': 'High School+',
                                                              'Secundaria': 'Middle School',                                                        
                                                                'Primaria': 'Elementary School'})


### Ajustamos la variable edad (pregunta 4)
df = df.rename(columns={'edad': 'Age'})


### Ajustamos la variable Genero (pregunta 4)
df = df.rename(columns={'Sexo': 'Gender'})
df['Gender'] = df['Gender'].replace({'Masculino': 0, 'Femenino': 1})


### Ajustamos la variable Genero (pregunta 4)
df = df.rename(columns={'p3': 'Marital_Status'})
df['Marital_Status'] = df['Marital_Status'].replace({'Soltera (o)': 1, 'Viuda (o)': 1, 
                                                     'Casada (o)': 0, 'Divorciada (o)': 0, 
                                                     'No indica': 0, 'Unión Libre': 0})

### Ajustamos la variable departamento (pregunta 2)
df = df.rename(columns={'departamento': 'Deparment'})


df= df[['Are_you_familiar_with_Chivo_Wallet', 'Have_you_tried_to_Download_Chivo_Wallet','Cellphone_with_internet', 'Unbanked', 'Years_of_schooling', 'Age', 'Gender', 'Marital_Status', 'Deparment']]

df.to_excel('Data/Data_procesada/Data_Processed.xlsx', index=False)

