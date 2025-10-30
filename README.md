# 📊 Demanda Insatisfecha Salud - Conversor CSV a Excel

Herramienta para procesar reportes de demanda insatisfecha del sistema de salud, convirtiendo archivos CSV a Excel con desglose automático de datos estructurados.

## 🎯 Funcionalidad

Este script Python automatiza el procesamiento de reportes de contactos, realizando:

- ✅ Conversión de CSV a formato Excel (.xlsx)
- ✅ Desglose automático del campo "Cuestionario respondido" en 5 columnas separadas
- ✅ Detección automática de codificación del archivo (UTF-8, Latin-1, Windows-1252, etc.)
- ✅ Preservación de caracteres especiales y acentos
- ✅ Manejo de archivos con miles de filas

## 📥 Formato de Entrada

**Archivo CSV esperado:** `Reporte_Contactos_2025_10_30_1215.csv`

**Estructura del CSV (2 columnas):**
```
Cuestionario respondido,Fecha de inicio
1 - Id_plataforma_contacto - 5491138839970 | 2 - Id_paciente - 1584559 | 3 - Nombre_profesional -   | 4 - Id_profesional - 46050 | 5 - Link_chat - https://go.botmaker.com/#/chats/XXX,29/10/2025 09:58:28
```

## 📤 Formato de Salida

**Archivo Excel generado:** `Reporte_Contactos_2025_10_30_desglosado.xlsx`

**Estructura del Excel (7 columnas):**

| # | Columna | Descripción |
|---|---------|-------------|
| 1 | Cuestionario respondido | Campo original con todos los datos |
| 2 | Fecha de inicio | Fecha y hora del contacto |
| 3 | Id_plataforma_contacto | Número de teléfono/plataforma (ej: 5491138839970) |
| 4 | Id_paciente | Identificador único del paciente |
| 5 | Nombre_profesional | Nombre del profesional (puede estar vacío) |
| 6 | Id_profesional | Identificador del profesional |
| 7 | Link_chat | URL del chat en Botmaker |

## 🚀 Instalación

### Requisitos Previos
- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Instalar Dependencias

```bash
pip install pandas openpyxl
```

O usando el archivo de requisitos:

```bash
pip install -r requirements.txt
```

## 📖 Uso

### Opción 1: Uso Básico (Nombres por Defecto)

1. Coloca tu archivo CSV en la misma carpeta que el script
2. Asegúrate de que se llame: `Reporte_Contactos_2025_10_30_1215.csv`
3. Ejecuta:

```bash
python csv_to_excel.py
```

4. Se generará: `Reporte_Contactos_2025_10_30_desglosado.xlsx`

### Opción 2: Personalizar Nombres de Archivos

Edita el script `csv_to_excel.py` en las líneas 108-111:

```python
archivo_csv = "tu_archivo.csv"
archivo_excel = "nombre_salida.xlsx"
```

### Ejemplo de Ejecución

```bash
$ python csv_to_excel.py
============================================================
CONVERSOR DE CSV A EXCEL
============================================================
Leyendo archivo CSV: Reporte_Contactos_2025_10_30_1215.csv
✓ Encoding detectado: latin-1
✓ CSV leído correctamente: 5247 filas, 2 columnas
Columnas encontradas: ['Cuestionario respondido', 'Fecha de inicio']

Desglosando campo 'Cuestionario respondido'...
✓ Campo desglosado en 5 columnas:
  - Id_plataforma_contacto
  - Id_paciente
  - Nombre_profesional
  - Id_profesional
  - Link_chat

Convirtiendo a Excel: Reporte_Contactos_2025_10_30_desglosado.xlsx
✓ Conversión completada exitosamente!
✓ Archivo guardado: Reporte_Contactos_2025_10_30_desglosado.xlsx
✓ Total de filas procesadas: 5247
✓ Total de columnas en Excel: 7

============================================================
PROCESO FINALIZADO
============================================================
```

## 🔧 Características Técnicas

### Extracción de Datos
El script utiliza expresiones regulares para extraer datos del campo "Cuestionario respondido" con el formato:
```
N - nombre_campo - valor | N - nombre_campo - valor | ...
```

### Manejo de Codificaciones
El script intenta automáticamente las siguientes codificaciones:
- UTF-8
- Latin-1 (ISO-8859-1)
- CP1252 (Windows-1252)

### Gestión de Errores
- ❌ Archivo no encontrado
- ❌ CSV vacío
- ❌ Errores de codificación
- ❌ Formato inválido

## 🛠️ Solución de Problemas

### Error: "No se encontró el archivo"
**Solución:** Verifica que el archivo CSV esté en la misma carpeta que el script y que el nombre sea correcto.

### Error: "codec can't decode byte"
**Solución:** El script actualizado maneja esto automáticamente. Si persiste, verifica que el archivo no esté corrupto.

### Excel generado vacío o con datos incorrectos
**Solución:** Verifica que el separador del CSV sea una coma (,) y que el formato del campo "Cuestionario respondido" sea el esperado.

## 📁 Estructura del Proyecto

```
Demanda_Insatisfecha_Salud/
├── csv_to_excel.py              # Script principal
├── requirements.txt              # Dependencias del proyecto
├── README.md                     # Este archivo
└── ejemplos/
    ├── ejemplo_input.csv        # Ejemplo de entrada
    └── ejemplo_output.xlsx      # Ejemplo de salida
```

## 💡 Consejos de Uso en Excel

### Inmovilizar Primera Columna
Para mantener visible la primera columna al hacer scroll:
1. Abre el Excel generado
2. Haz clic en la celda **B1**
3. Ve a **Vista > Inmovilizar > Inmovilizar paneles**

### Filtros Automáticos
Para activar filtros en los encabezados:
1. Selecciona cualquier celda de la tabla
2. Ve a **Datos > Filtro** (o presiona Ctrl+Shift+L)

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Haz un Fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👤 Autor

**EdVeralli**
- GitHub: [@EdVeralli](https://github.com/EdVeralli)
- Repositorio: [Demanda_Insatisfecha_Salud](https://github.com/EdVeralli/Demanda_Insatisfecha_Salud)

## 📧 Contacto

Si tienes preguntas, sugerencias o encuentras algún problema, por favor abre un [Issue](https://github.com/EdVeralli/Demanda_Insatisfecha_Salud/issues) en GitHub.

---

⭐ Si este proyecto te resultó útil, considera darle una estrella en GitHub!
