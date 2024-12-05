Proyecto de Gestión de Inventario

Este proyecto es una aplicación de gestión de inventario desarrollada en Python, que utiliza SQLite como base de datos para almacenar información sobre los productos.

## Requisitos

- Python 3.x
- SQLite (incluido en la instalación de Python)

## Ejecución de la Aplicación

Para ejecutar la aplicación, sigue los siguientes pasos:

1. Asegúrate de tener Python y SQLite instalados en tu sistema.
2. Descarga o clona el repositorio donde se encuentra el archivo .py del proyecto.
3. Abre una terminal o línea de comandos.
4. Navega al directorio donde se encuentra el archivo de la aplicación (por ejemplo, `inventario.py`).
5. Ejecuta el siguiente comando: python inventario.py
6. La aplicación se iniciará y verás un menú interactivo en la consola.

## Funcionalidades Implementadas

1. **Inicialización de Base de Datos**:
- Cuando se ejecuta la aplicación, se crea un archivo de base de datos `inventario.db` y se establece una tabla `Productos` si no existe.

2. **Registrar Producto**:
- Permite al usuario ingresar los detalles de un nuevo producto (nombre, descripción, cantidad, precio y categoría) y lo guarda en la base de datos.

3. **Mostrar Productos**:
- Muestra todos los productos registrados en la base de datos, junto con su ID, nombre, descripción, cantidad, precio y categoría.

4. **Actualizar Cantidad de un Producto**:
- Permite actualizar la cantidad disponible de un producto ya registrado en la base de datos utilizando su ID.

5. **Eliminar Producto**:
- Elimina un producto específico de la base de datos utilizando su ID.

6. **Reporte de Bajo Stock**:
- Permite generar un informe de los productos cuyo stock es inferior a un límite definido por el usuario.

7. **Menú Interactivo**:
- La aplicación presenta un menú interactivo donde el usuario puede seleccionar la opción deseada para gestionar el inventario.

## Notas Adicionales

- Asegúrate de ingresar datos válidos cuando se te soliciten.
- Los cambios en la base de datos se guardan de forma permanente.
- Si deseas cerrar la aplicación, simplemente selecciona la opción "6. Salir" en el menú.