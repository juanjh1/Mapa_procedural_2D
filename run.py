import pygame 
import biomas 
import random 
import player
from perlin_noise import PerlinNoise

pygame.init()
WIDTH = 700
HEIGTH = 600
RUIDO = random.uniform(0, 1000)
OCTAVAS = 1
pixel_dimension = 4

noise = PerlinNoise(octaves=OCTAVAS, seed=RUIDO) 

def bioma_selector(ruido) -> tuple:
    normalized_noise_value = (ruido + .60) / 2   
    def select_bioma() -> biomas.Bioma:
        if normalized_noise_value < 0.2:
            return biomas.Bioma.AGUA 
        elif  normalized_noise_value < 0.4:      
           return biomas.Bioma.BOSQUE
        elif  normalized_noise_value < 0.6:
            return biomas.Bioma.TIERRA  
             
             
        return biomas.Bioma.MONTANA
      
        
    
    def select_pixel_bioma(bioma) -> tuple:
      
        texturas = biomas.bioma_data[bioma]['texturas']
        if bioma == biomas.Bioma.AGUA :
          if normalized_noise_value < 0.1:
                index = 0
          elif  normalized_noise_value < 0.15:
                index = 1
          else:
                index = 2  
        elif bioma == biomas.Bioma.BOSQUE:
            if normalized_noise_value < 0.25:
                index = 0
            elif  normalized_noise_value < 0.3:
                index = 1
            elif  normalized_noise_value < 0.35:
                index = 2
            else:
                index = 3 
        elif bioma == biomas.Bioma.TIERRA:
            if normalized_noise_value < 0.42:
                index = 3 
    
            elif  normalized_noise_value < 0.45:
                index = 2
  
            elif  normalized_noise_value < 0.5:
                 index = 1
            else:
                index = 0
                      
        elif bioma == biomas.Bioma.MONTANA:
             index = 1
        eleccion = texturas[index] 
        
        return eleccion.value  

    
    return select_pixel_bioma(select_bioma())



def initialize_map (widt, heigth, dimension) -> list :    
     return [[bioma_selector(noise([row/ (HEIGTH* 0.18), col / (WIDTH* 0.18)])) for col in range(0, widt, dimension)] for row in  range(0, heigth, dimension)]

 



screen = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("Generador de Mapas Procedurales")
matrix = initialize_map(WIDTH, HEIGTH, pixel_dimension)

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
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_UP:
                matrix = player.arriba( matrix)
          elif event.key == pygame.K_DOWN:
                matrix = player.abajo( matrix)
          elif event.key == pygame.K_LEFT:
                matrix = player.izquierda(matrix)
          elif event.key == pygame.K_RIGHT:
                matrix = player.derecha( matrix)


pygame.quit()