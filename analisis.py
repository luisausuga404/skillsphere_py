import pandas as pd
from src.preprocesamiento import cargar_datos, manejar_nulos, estandarizar_texto

df_estudiantes = cargar_datos("data/raw/estudiantes.csv")
df_certificados = cargar_datos("data/raw/certificados.csv")

df_estudiantes = manejar_nulos(df_estudiantes, ["nombre", "id_estudiante"])
df_estudiantes = estandarizar_texto(df_estudiantes, ["nombre", "programa", "ciudad"])

df_certificados = manejar_nulos(df_certificados, ["id_estudiante", "nombre_curso"])
df_certificados = estandarizar_texto(df_certificados, ["nombre_curso", "institucion", "estado"])

df_estudiantes.to_csv("data/processed/estudiantes_limpios.csv", index=False)
df_certificados.to_csv("data/processed/certificados_limpios.csv", index=False)

print("Datos limpios guardados en data/processed/")