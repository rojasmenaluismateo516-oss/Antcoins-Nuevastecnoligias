import pandas as pd 

# zona para importar simulaciones
from utils.simulacion_usuario import simular_usuarios

# zona para importar limpiezas
from notebook.limpieza_usuario import limpiar_usuarios 

# creando las simulaciones
simulaciones = simular_usuarios(10)

# ordenando las simulaciones 
simulaciones_ordenadas = pd.DataFrame(simulaciones)

# limpiando el set de datos 
simulaciones_limpias = limpiar_usuarios(simulaciones_ordenadas)

print(simulaciones_limpias)