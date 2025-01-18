# Mapa_procedural_2D

Este proyecto es un generador de mapas procedurales en 2D utilizando ruido Perlin para crear biomas diversos como tierra, bosque, montaña y agua. Está desarrollado en Python utilizando la biblioteca Pygame para la visualización gráfica y la interacción con el usuario.


## Características
- Generación de mapas de biomas variados usando ruido Perlin.
- Visualización interactiva con Pygame.
- Control del jugador con teclas direccionales para moverlo en el mapa.
- La posibilidad de modificar el tamaño del mapa y la resolución de los píxeles.
- Código modular y fácil de entender

## Requisitos
Asegúrate de tener las siguientes bibliotecas instaladas:

- Python 3.x
- Pygame
- Perlin Noise

Puedes instalar las dependencias usando pip:


```sh
pip install pygame perlin-noise
```

## Instalación
Clona este repositorio a tu máquina local:

```sh
https://github.com/juanjh1/Mapa_procedural_2D.git
```
Instala las dependencias requeridas

Ejecuta el archivo principal para iniciar el generador de mapas:

```sh
python run.py
```

## Uso
- Al ejecutar el programa, se abrirá una ventana de Pygame mostrando un mapa generado procedimentalmente.
- El jugador puede moverse por el mapa utilizando las teclas ↑, ↓, ←, →.
- El mapa está compuesto por biomas representados por diferentes texturas.
# Estructura del Proyecto

| Archivo                       | funcionalidad                                                     |    
| ------                        | ------                                                            |
| run.py                        |  El archivo principal donde se ejecuta el generador de mapas.     |
| biomas.py                     | Contiene las clases y datos relacionados con los biomas.          |
| player.py                     | Gestiona la lógica y el control del jugador.                      |
| perlin_noise.py               | Biblioteca utilizada para generar el ruido Perlin.                |


