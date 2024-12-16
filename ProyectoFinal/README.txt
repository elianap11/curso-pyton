# Proyecto de Gestión de Inventario
Este proyecto es una aplicación de gestión de inventario desarrollada en Python, que utiliza SQLite como base de datos para almacenar información sobre los productos.

## Requisitos
- Python 3.x
- SQLite (incluido en la instalación de Python)

## Ejecución de la Aplicación
Para ejecutar la aplicación, sigue los siguientes pasos:
- Tener Python instalado en tu sistema.
- Descargar el archivo .py del proyecto.
- Abrir una terminal o línea de comandos.
-  Navegar al directorio donde se encuentra el archivo de la aplicación (por ejemplo, inventario.py).
- Ejecuta el siguiente comando: python inventario.py
- La aplicación se iniciará y verás un menú interactivo en la consola.

## Funcionalidades Implementadas
- Inicialización de Base de Datos: Cuando se ejecuta la aplicación, se crea un archivo de base de datos inventario.db y se establece una tabla Productos si no existe.
- Registrar Producto: Permite al usuario ingresar los detalles de un nuevo producto (nombre, descripción, cantidad, precio y categoría) y lo guarda en la base de datos. Incluye validaciones para asegurar que:
- El nombre y la categoría no estén vacíos.
- La cantidad sea un número entero positivo.
- El precio sea un número válido y no negativo.

## Mostrar Productos:
- Muestra todos los productos registrados en la base de datos, junto con su ID, nombre, descripción, cantidad, precio y categoría.

## Buscar Producto por ID:
- Permite buscar un producto específico en la base de datos utilizando su ID.
- Si el producto existe, muestra todos los detalles; de lo contrario, informa al usuario que no se encontró el producto.

## Actualizar Cantidad de un Producto:
- Permite actualizar la cantidad disponible de un producto ya registrado en la base de datos utilizando su ID.
- Incluye validaciones para asegurar que la nueva cantidad sea un número entero positivo.

## Eliminar Producto:
- Elimina un producto específico de la base de datos utilizando su ID.
- Confirma al usuario si la operación fue exitosa o si no se encontró el producto.

## Reporte de Bajo Stock:
- Genera un informe de los productos cuyo stock es inferior a un límite definido por el usuario.
- Muestra el ID, nombre y cantidad de cada producto.

## Menú Interactivo:
- La aplicación presenta un menú interactivo donde el usuario puede seleccionar la opción deseada para gestionar el inventario.
- Ahora incluye manejo de errores para entradas inválidas, asegurando una experiencia más robusta.

## Notas Adicionales
- Asegurate de ingresar datos válidos cuando se te soliciten para evitar errores.
- Los cambios en la base de datos se guardan de forma permanente.
- Si deseas cerrar la aplicación, simplemente selecciona la opción "7. Salir" en el menú.