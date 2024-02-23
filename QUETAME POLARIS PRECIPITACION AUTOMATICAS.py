#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import psycopg2
import matplotlib.pyplot as plt
import datetime
from datetime import date, timedelta
import locale


# In[2]:


locale.setlocale(locale.LC_ALL, 'es-ES')


# In[3]:


dia_actual = date.today()
ayer = dia_actual - timedelta(days = 1)
ayer_str = ayer.strftime("%A %d de %B de %Y")
ayer_str

hoy_str = dia_actual.strftime("%A %d de %B de %Y")


# In[11]:


from datetime import datetime


# In[13]:


dia_actual = datetime.now()
dia_actual


# In[14]:


dia_6 = dia_actual - timedelta(hours = 12)


# In[24]:


dia_6_str = dia_6.strftime('%Y-%m-%d %H:%M:%S.%f')


# In[16]:


dia_hoy = dia_actual.strftime('%Y-%m-%d %H:%M:%S.%f')


# In[17]:


dia_hoy


# In[22]:


manana = dia_actual + timedelta(days=1)


# In[18]:


con = psycopg2.connect(database= "ideam", user="fda_ideam", password= "Fd4_1d34m201902",
    host = "172.16.1.193")


# In[19]:


# Crea un objeto cursor utilizando la conexión
cur = con.cursor()


# In[20]:


fecha_anterior = ayer.strftime("%Y-%m-%d")
fecha_anterior

fecha_actual = dia_actual.strftime("%Y-%m-%d")


# In[23]:


# Formateamos la fecha para que sea una cadena en el formato que deseamos
fecha_manana = manana.strftime("%Y-%m-%d")
fecha_manana


# In[25]:


sql = f''' SELECT st.station_name, ad.date_record, st.municipality, st.province, ad.id_stz, ad.raw_data AS nivel
            FROM data_radio.archive_data AS ad INNER JOIN configuration.stations AS st
                ON ad.id_stz = st.id_stz
            WHERE id_measure = 1
            AND ad.date_record BETWEEN '{dia_6_str}'::timestamp AND  '{dia_actual}'::timestamp
            ORDER BY nivel DESC NULLS LAST; '''


# In[23]:


# sql = f''' SELECT st.station_name, ad.date_record, st.municipality, st.province, ad.id_stz, ad.raw_data AS nivel
#             FROM data_radio.archive_data AS ad INNER JOIN configuration.stations AS st
#                 ON ad.id_stz = st.id_stz
#             WHERE id_measure = 7 AND ad.id_stz IN ('1145', '2132')
#             AND ad.date_record BETWEEN '2023-07-17 07:0:00.000'::timestamp AND  '{fecha_manana} 07:0:00.000'::timestamp
#             ORDER BY nivel DESC NULLS LAST; '''


# In[26]:


cur.execute(sql)


# In[27]:


# Obtiene los resultados de la consulta
rows = cur.fetchall()



# Obtiene los nombres de las columnas de la consulta
col_names = [desc[0] for desc in cur.description]

# Crea un dataframe con los resultados
df = pd.DataFrame(rows, columns=col_names)


# In[28]:


# cur.close()
# con.close()


# In[29]:


df['nivel'] = df['nivel'].replace(8, np.nan)


# In[30]:


df


# In[31]:


df.dtypes


# In[32]:


df['id_stz'].unique()


# In[33]:


estaciones_id = df['id_stz'].unique().tolist()


# In[39]:

#df.to_excel(r"O:\My Drive\OSPA\01. Tematicas\02. Hidrologia\01. Productos\Visor_hidrologia\insumos\Registros\niveles.xlsx")
df.to_excel(r"G:\Mi unidad\OSPA\01. Tematicas\02. Hidrologia\01. Productos\Visor_hidrologia\insumos\Registros\precipitacion.xlsx")



# In[ ]:




