"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""
import pandas as pd
import os

def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
    
    input_file = "files/input/solicitudes_de_credito.csv"
    output_dir = "files/output"

    df = load_data(input_file)
    df = clean_data(df)
    save_data(df, output_dir)
    print(df)
    
def clean_data(df):
    df_clean= df.copy()
    df_clean.dropna(inplace=True)

    cols_texto = ["sexo", "tipo_de_emprendimiento", "idea_negocio", "barrio", "línea_credito"]

    # Limpiar columnas de texto
    for col in cols_texto:  

        df_clean[col] = (df_clean[col]
            .str.lower()
            .str.replace("-", " ", regex=False)
            .str.replace("_", " ", regex=False)
        )

    # Organizar columna "fecha_de_beneficio"
    df_clean["fecha_de_beneficio"] = df_clean["fecha_de_beneficio"].apply(
        lambda f: f"{f.split('/')[2]}/{f.split('/')[1]}/{f.split('/')[0]}" if len(f.split('/')[0]) == 4 else f
    )

    # Limpiar caracteres de "monto_del_credito" 
    df_clean["monto_del_credito"] = (
        pd.to_numeric(df_clean["monto_del_credito"]
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False))
    )
   
    # eliminar duplicados y filas con campos vacios
    df_clean.drop_duplicates(inplace=True)
   
    return df_clean

#Lea el archivo usando pandas y devuelva un DataFrame
def load_data(ruta_archivo):
    df = pd.read_csv(ruta_archivo,sep=";",index_col=0)
    df.dropna(inplace=True)
    return df

#Guarda el DataFrame en un archivo
def save_data(df, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "solicitudes_de_credito.csv")
    df.to_csv(output_path, index=False, sep=";")

if __name__ == "__main__":
    pregunta_01()