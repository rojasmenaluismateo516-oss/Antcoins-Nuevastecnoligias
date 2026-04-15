import pandas as pd

#Rutina para crear un archivo json desde python
def crear_json(data_frame,nombre_archivo="archivo.json"):
    data_frame.to_json(nombre_archivo,orient="records", indent=4)
    


#Rutina para crear un archivo csv desde python
def crear_csv(data_frame,nombre_archivo="archivo.csv"):
    data_frame.to_csv(nombre_archivo, index=False)
    
