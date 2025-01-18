
import pygame 

class Player():
    widt = None
    heigt = None
    pixel_size = None
    last_value = None

    def __init__(self, widt, heigt, pixel) -> None:
      
        self.widt = widt
        self.heigt = heigt
        self.pixel_size = pixel
        self.usewidt = self.widt // self.pixel_size
        self.useheigt = self.heigt // self.pixel_size 
        self.x = self.usewidt // 2 
        self.y = self.useheigt // 2 
        

    def set_player_matrix(self,  matrix) -> list :
        self.last_value = matrix[self.y][self.x]
        matrix[self.y][self.x] =  (0,0,0)
        return  matrix
    

    def arriba(self, matrix):

        matrix[self.y][self.x] = self.last_value 
        self.y -= 1  
        self.last_value = matrix[self.y][self.x]
        matrix[self.y][self.x] = (0, 0, 0)  
        return matrix

    def abajo(self, matrix):
        matrix[self.y][self.x] = self.last_value 
        self.y += 1
        self.last_value = matrix[self.y][self.x]
        matrix[self.y][self.x] = (0, 0, 0)  
        return matrix

    def izquierda(self, matrix):
        matrix[self.y][self.x] = self.last_value
        self.x -= 1 
        self.last_value = matrix[self.y][self.x]
        matrix[self.y][self.x] = (0, 0, 0)  
        return matrix

    def derecha(self, matrix):
        matrix[self.y][self.x] = self.last_value 
        self.x += 1
        self.last_value = matrix[self.y][self.x]
        matrix[self.y][self.x] = (0, 0, 0)  
        return matrix




    
        

        
        