#Funcion para generar N usuarios
#En spring boot el modelo de un usuario es:

#id(Integer)
#nombre(String)
#correo(String)
#telefono(String)
#tipo_documento(String)
#numero_documento(String)
#estado(String)

import random
from datetime import datetime, timedelta

def simular_usuarios(numeroUsuarios):

    #Defino atributos base
    nombres=["Juan Perez","Maria Lopez","Carlos Gomez","Ana Martinez","Luis Rojas","Sofia Torres"]
    correos=["gmail.com","hotmail.com","yahoo.com"]
    telefonos_base=["300","301","302","310","311"]
    tipos_documento=["CC","TI","CE"]
    estados=["ACTIVO","INACTIVO","SUSPENDIDO"]

    #Ciclo para generar N registros de la tabla usuarios
    usuarios=[]
    for _ in range (numeroUsuarios):
        usuario={
            "id":random.randint(1,1000),
            "nombre":random.choice(nombres),
            "correo":random.choice(correos),
            "telefono":random.choice(telefonos_base),
            "tipo_documento":random.choice(tipos_documento),
            "numero_documento":str(random.randint(10000000,99999999)),
            "estado":random.choice(estados)
        }
        usuarios.append(usuario)
    return usuarios