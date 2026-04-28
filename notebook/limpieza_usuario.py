import pandas as pd

def limpiar_usuarios(data_frame_sucio):
    data_frame_limpio = data_frame_sucio.copy()

    # 1. limpiar textos
    data_frame_limpio["nombre"] = data_frame_limpio["nombre"].astype("string").str.strip().str.title()
    data_frame_limpio["correo"] = data_frame_limpio["correo"].astype("string").str.strip().str.lower()
    data_frame_limpio["telefono"] = data_frame_limpio["telefono"].astype("string").str.strip()
    data_frame_limpio["tipo_documento"] = data_frame_limpio["tipo_documento"].astype("string").str.strip().str.upper()
    data_frame_limpio["estado"] = data_frame_limpio["estado"].astype("string").str.strip().str.upper()

    # 2. valores esperados
    valores_tipo_doc = ["CC", "TI", "CE"]
    data_frame_limpio["tipo_documento"] = data_frame_limpio["tipo_documento"].where(
        data_frame_limpio["tipo_documento"].isin(valores_tipo_doc),
        pd.NA
    )

    valores_estado = ["ACTIVO", "INACTIVO", "SUSPENDIDO"]
    data_frame_limpio["estado"] = data_frame_limpio["estado"].where(
        data_frame_limpio["estado"].isin(valores_estado),
        pd.NA
    )

    # 3. limpieza numérica
    data_frame_limpio["id"] = pd.to_numeric(data_frame_limpio["id"], errors="coerce")
    data_frame_limpio["numero_documento"] = pd.to_numeric(data_frame_limpio["numero_documento"], errors="coerce")

    data_frame_limpio = data_frame_limpio[data_frame_limpio["id"] > 0]
    data_frame_limpio = data_frame_limpio[data_frame_limpio["numero_documento"] > 0]

    # 4. validaciones específicas

    # correo válido básico
    data_frame_limpio["correo"] = data_frame_limpio["correo"].where(
        data_frame_limpio["correo"].str.contains("@", na=False),
        pd.NA
    )

    # teléfono válido (10 dígitos)
    data_frame_limpio["telefono"] = data_frame_limpio["telefono"].where(
        data_frame_limpio["telefono"].str.match(r'^\d{10}$', na=False),
        pd.NA
    )

    # 5. eliminar nulos obligatorios
    columnas_obligatorias = ["id", "nombre", "correo", "telefono", "tipo_documento", "numero_documento", "estado"]
    data_frame_limpio = data_frame_limpio.dropna(subset=columnas_obligatorias)

    return data_frame_limpio