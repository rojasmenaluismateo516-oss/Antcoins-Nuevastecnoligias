import random

def simular_usuarios(numeroUsuarios):

    nombres = ["Juan Perez","Maria Lopez","Carlos Gomez","Ana Martinez","Luis Rojas","Sofia Torres"]
    correos = ["gmail.com","hotmail.com","yahoo.com"]
    telefonos_base = ["300","301","302","310","311"]
    tipos_documento = ["CC","TI","CE"]
    estados = ["ACTIVO","INACTIVO","SUSPENDIDO"]

    usuarios = []

    for _ in range(numeroUsuarios):

        usuario = {
            "id": random.randint(1, 200),
            "nombre": random.choice(nombres),
            "correo": f"{random.choice(nombres).replace(' ','').lower()}@{random.choice(correos)}",
            "telefono": random.choice(telefonos_base) + str(random.randint(1000000, 9999999)),
            "tipo_documento": random.choice(tipos_documento),
            "numero_documento": str(random.randint(10000000,99999999)),
            "estado": random.choice(estados)
        }

       
        probabilidadError = random.random()

        if probabilidadError < 0.2:
            usuario["id"] = -1  
        elif probabilidadError < 0.4:
            usuario["correo"] = " " + usuario["correo"].upper()  
        elif probabilidadError < 0.5:
            usuario["telefono"] = "123"  
        elif probabilidadError < 0.7:
            usuario["tipo_documento"] = "XX"  
        elif probabilidadError < 0.9:
            usuario["estado"] = "desconocido" 

        usuarios.append(usuario)

    return usuarios