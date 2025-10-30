#!/usr/bin/env python3
"""
Script para convertir CSV de reporte de demanda insatisfecha a Excel
Desglosa el campo "Cuestionario respondido" en 5 columnas separadas
"""
import pandas as pd
import sys
import re
from pathlib import Path

def extraer_valor(texto, patron):
    """
    Extrae el valor de un campo específico del texto
    
    Args:
        texto: Texto completo del campo
        patron: Nombre del campo a extraer
    
    Returns:
        Valor extraído o cadena vacía si no se encuentra
    """
    if pd.isna(texto):
        return ''
    
    # Buscar el patrón: "N - nombre_campo - valor"
    match = re.search(rf'\d+\s*-\s*{patron}\s*-\s*([^|]*)', str(texto))
    if match:
        return match.group(1).strip()
    return ''

def desglosar_cuestionario(df):
    """
    Desglosa la columna "Cuestionario respondido" en 5 columnas separadas
    
    Args:
        df: DataFrame con los datos
    
    Returns:
        DataFrame con las nuevas columnas agregadas
    """
    print("\nDesglosando campo 'Cuestionario respondido'...")
    
    if 'Cuestionario respondido' not in df.columns:
        print("⚠️  Advertencia: No se encontró la columna 'Cuestionario respondido'")
        return df
    
    # Extraer cada campo en una nueva columna
    df['Id_plataforma_contacto'] = df['Cuestionario respondido'].apply(
        lambda x: extraer_valor(x, 'Id_plataforma_contacto')
    )
    df['Id_paciente'] = df['Cuestionario respondido'].apply(
        lambda x: extraer_valor(x, 'Id_paciente')
    )
    df['Nombre_profesional'] = df['Cuestionario respondido'].apply(
        lambda x: extraer_valor(x, 'Nombre_profesional')
    )
    df['Id_profesional'] = df['Cuestionario respondido'].apply(
        lambda x: extraer_valor(x, 'Id_profesional')
    )
    df['Link_chat'] = df['Cuestionario respondido'].apply(
        lambda x: extraer_valor(x, 'Link_chat')
    )
    
    print("✓ Campo desglosado en 5 columnas:")
    print("  - Id_plataforma_contacto")
    print("  - Id_paciente")
    print("  - Nombre_profesional")
    print("  - Id_profesional")
    print("  - Link_chat")
    
    return df

def convertir_csv_a_excel(archivo_csv, archivo_excel=None):
    """
    Convierte un archivo CSV a formato Excel (.xlsx)
    
    Args:
        archivo_csv: Ruta del archivo CSV de entrada
        archivo_excel: Ruta del archivo Excel de salida (opcional)
    """
    try:
        print(f"Leyendo archivo CSV: {archivo_csv}")
        
        # Intentar leer con diferentes encodings
        encodings = ['utf-8', 'latin-1', 'iso-8859-1', 'cp1252', 'windows-1252']
        df = None
        encoding_usado = None
        
        for encoding in encodings:
            try:
                df = pd.read_csv(archivo_csv, sep=',', encoding=encoding)
                encoding_usado = encoding
                print(f"✓ Encoding detectado: {encoding}")
                break
            except UnicodeDecodeError:
                continue
            except Exception:
                continue
        
        if df is None:
            print("❌ Error: No se pudo leer el archivo con ninguna codificación conocida")
            sys.exit(1)
        
        print(f"✓ CSV leído correctamente: {len(df)} filas, {len(df.columns)} columnas")
        print(f"Columnas encontradas: {list(df.columns)}")
        
        # Desglosar el campo "Cuestionario respondido"
        df = desglosar_cuestionario(df)
        
        # Si no se especifica nombre de salida, usar el mismo nombre pero con extensión .xlsx
        if archivo_excel is None:
            archivo_excel = Path(archivo_csv).stem + '.xlsx'
        
        # Guardar como Excel
        print(f"\nConvirtiendo a Excel: {archivo_excel}")
        df.to_excel(archivo_excel, index=False, engine='openpyxl')
        
        print(f"✓ Conversión completada exitosamente!")
        print(f"✓ Archivo guardado: {archivo_excel}")
        print(f"✓ Total de filas procesadas: {len(df)}")
        print(f"✓ Total de columnas en Excel: {len(df.columns)}")
        
        return archivo_excel
        
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo '{archivo_csv}'")
        sys.exit(1)
    except pd.errors.EmptyDataError:
        print(f"❌ Error: El archivo CSV está vacío")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error al procesar el archivo: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    # Nombre del archivo CSV
    archivo_csv = "Reporte_Contactos_2025_10_30_1215.csv"
    
    # Puedes cambiar el nombre del archivo de salida si lo deseas
    archivo_excel = "Reporte_Contactos_2025_10_30_desglosado.xlsx"
    
    print("=" * 60)
    print("CONVERSOR DE CSV A EXCEL")
    print("=" * 60)
    
    convertir_csv_a_excel(archivo_csv, archivo_excel)
    
    print("\n" + "=" * 60)
    print("PROCESO FINALIZADO")
    print("=" * 60)
