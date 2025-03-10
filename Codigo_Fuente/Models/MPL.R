#INSTALAMOS PAQUETES NECESARIOS
#install.packages("readxl")
#install.packages("plm")
#install.packages("dplyr")
#install.packages("fixest")
#install.packages("stargazer")
#install.packages("modelsummary")
#install.packages("officer")
#install.packages("rstudioapi")

#Cargamos librerías
library(readxl)
library(plm)
library(dplyr)
library(fixest)
library(stargazer)
library(modelsummary)
library(officer)
library(rstudioapi)

# Configuramos directorio dinámico
ruta_script <- rstudioapi::getActiveDocumentContext()$path
setwd(dirname(ruta_script))
setwd("..")
setwd("..")
current_dir <- getwd()

# Cargamos los datos procesados
ruta_archivo <- "Data/Data_procesada/Data_Processed.xlsx"
dataframe <- read_excel(ruta_archivo)

# Muestra los primeros registros del DataFrame y los nombres de las variables
head(dataframe)
glimpse(dataframe)

# Configuramos las variables categóricas por factores
dataframe$Years_of_schooling <- factor(dataframe$Years_of_schooling)
dataframe$Deparment <- factor(dataframe$Deparment)

### Creamos un dataframe que solo tenga a las personas que conocen Chivo (requisito de los resultados de la tabla1)
data_filtrado <- subset(dataframe, Are_you_familiar_with_Chivo_Wallet == 1)
data_filtrado <- na.omit(data_filtrado)


####################################################################################################
########################  MODELOS DE REGRESIÓN DE LA TABLA 1 #######################################
####################################################################################################

# Ajustar el modelo 1 (regresión simple)
#modelo_simple1 <- lm(Have_you_tried_to_Download_Chivo_Wallet ~ Cellphone_with_internet + Deparment, data = data_filtrado)
# Resumen de los resultados
#summary(modelo_simple1)

# Ajustar el modelo 1 (errores clusterizados por deparment)
modelo_fixest1 <- feols(Have_you_tried_to_Download_Chivo_Wallet ~ Cellphone_with_internet, data = data_filtrado, cluster = ~Deparment)
# Resumen de los resultados
summary(modelo_fixest1)



# Ajustar el modelo 2 (regresión simple)
#modelo_simple2 <- lm(Have_you_tried_to_Download_Chivo_Wallet ~ Unbanked + Deparment, data = data_filtrado)
# Resumen de los resultados
#summary(modelo_simple2)

# Ajustar el modelo 2 (errores clusterizados por deparment)
modelo_fixest2 <- feols(Have_you_tried_to_Download_Chivo_Wallet ~ Unbanked, data = data_filtrado, cluster = ~Deparment)
# Resumen de los resultados
summary(modelo_simple2)



# Ajustar el modelo 3 (regresión simple)
#modelo_simple3 <- lm(Have_you_tried_to_Download_Chivo_Wallet ~ Years_of_schooling + Age + Gender + Marital_Status + Deparment, data = data_filtrado)
# Resumen de los resultados
#summary(modelo_simple3)

# Ajustar el modelo 3 (errores clusterizados por deparment)
modelo_fixest3 <- feols(Have_you_tried_to_Download_Chivo_Wallet ~ Years_of_schooling + Age + Gender + Marital_Status, data = data_filtrado, cluster = ~Deparment)
# Resumen de los resultados
summary(modelo_fixest3)



# Ajustar el modelo 4 (regresión simple)
#modelo_simple4 <- lm(Have_you_tried_to_Download_Chivo_Wallet ~ Cellphone_with_internet + Unbanked + Years_of_schooling + Age + Gender + Marital_Status + Deparment, data = data_filtrado)
# Resumen de los resultados
#summary(modelo_simple4)

# Ajustar el modelo 4 (errores clusterizados por deparment)
modelo_fixest4 <- feols(Have_you_tried_to_Download_Chivo_Wallet ~ Cellphone_with_internet + Unbanked + Years_of_schooling + Age + Gender + Marital_Status, data = data_filtrado, cluster = ~Deparment)
# Resumen de los resultados
summary(modelo_fixest4)


### Hacemos tabla con los resultados de las regresiones simples
#stargazer(modelo_simple1, modelo_simple2, modelo_simple3, modelo_simple4, type = "text",
#          title = "Resultados de Modelos de Regresión",
#          align = TRUE, no.space = TRUE)
#modelos <- list(modelo_fixest1, modelo_fixest2, modelo_fixest3, modelo_fixest4)
#modelsummary(modelos, output = "markdown")


### Hacemos tabla con los resultados de las regresiones simples con errores clusterizados por deparment
resultados <- etable(modelo_fixest1, modelo_fixest2, modelo_fixest3, modelo_fixest4)
print(resultados)


### Exportamos la tabla a un documento de word

# Crea un documento de Word
doc <- read_docx()
doc <- body_add_table(doc, value = resultados, style = "table_template")
print(doc, target = "Resultados/resultados_modelo_Tabla1.docx")


