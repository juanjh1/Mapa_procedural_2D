import pygame 
import biomas 
import random 
import player
from perlin_noise import PerlinNoise

pygame.init()
WIDTH = 700
HEIGTH = 600
RUIDO = random.uniform(0, 100)
OCTAVAS = 8
pixel_dimension = 10

noise = PerlinNoise(octaves=OCTAVAS, seed=RUIDO) 

def selector_bioma(ruido) -> tuple:
    
    def select_bioma() -> biomas.Bioma:
        if ruido < 0.2:
            return biomas.Bioma.TIERRA
          
        elif ruido < 0.4:
            return biomas.Bioma.BOSQUE
        elif ruido < 0.6:
            return biomas.Bioma.MONTANA
             
           
        return biomas.Bioma.AGUA 
        
    
    def select_pixel_bioma(noise_value, bioma) -> tuple:
      
        texturas = biomas.bioma_data[bioma]['texturas']
        normalized_noise_value = (noise_value + 1) / 2         
        index = int(normalized_noise_value * (len(texturas) - 1)) 
        eleccion = texturas[index] 
        
        return eleccion.value  

    
    return select_pixel_bioma(ruido ,select_bioma())



def map_intit (widt, heigth, dimension) -> list :    
     return [[selector_bioma(noise([row/ HEIGTH, col / WIDTH])) for col in range(0, widt, dimension)] for row in  range(0, heigth, dimension)]

 



screen = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("Generador de Mapas Procedurales")
matrix = map_intit(WIDTH, HEIGTH, pixel_dimension)

player  = player.Player(WIDTH, HEIGTH, pixel_dimension)

matrix = player.set_player_matrix(matrix)



def draw_grid() -> None:
   
    for y in range(0, HEIGTH,pixel_dimension ):
           pygame.draw.line(screen, (0,0, 0), (0, y), ( WIDTH, y))
    for x in range(0, WIDTH,pixel_dimension ):
           pygame.draw.line(screen, (0, 0, 0), (x, 0), (x, HEIGTH))



def draw_rects() -> None:
        for y in range(0, HEIGTH ,pixel_dimension ):
            for x in range(0, WIDTH ,pixel_dimension ):
                pygame.draw.rect(screen,matrix[y//pixel_dimension][x//pixel_dimension],(x,y, pixel_dimension, pixel_dimension),  )



running = True
while running:
    screen.fill((0, 0, 0))
   
    draw_grid()         
    draw_rects()
    
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN  :
          if event.key == pygame.K_UP:
                matrix = player.arriba( matrix)
          elif event.key == pygame.K_DOWN:
                matrix = player.abajo( matrix)
          elif event.key == pygame.K_LEFT:
                matrix = player.izquierda(matrix)
          elif event.key == pygame.K_RIGHT:
                matrix = player.derecha( matrix)


pygame.quit()