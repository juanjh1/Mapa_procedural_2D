
import pygame 

class Player():
    widt = None
    heigt = None
    pixel_size = None
    last_value = None
    THRESHOLD = 10

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
        self.generate_new_section( self.check_player_edge(self.x,self.y, matrix))
        matrix[self.y][self.x] = (0, 0, 0)  
        return matrix

    def abajo(self, matrix):
        matrix[self.y][self.x] = self.last_value 
        self.y += 1
        self.last_value = matrix[self.y][self.x]
        self.generate_new_section( self.check_player_edge(self.x,self.y, matrix))
        matrix[self.y][self.x] = (0, 0, 0)  
        return matrix

    def izquierda(self, matrix):
        matrix[self.y][self.x] = self.last_value
        self.x -= 1 
        self.last_value = matrix[self.y][self.x]
        self.generate_new_section( self.check_player_edge(self.x,self.y, matrix))
        matrix[self.y][self.x] = (0, 0, 0)  
        return matrix

    def derecha(self, matrix):
        matrix[self.y][self.x] = self.last_value 
        self.x += 1
        self.last_value = matrix[self.y][self.x]
       
        self.generate_new_section( self.check_player_edge(self.x,self.y, matrix))
        matrix[self.y][self.x] = (0, 0, 0)  
        return matrix

    def check_player_edge(self, x, y, matrix):
        print('l',x , self.THRESHOLD)

        print('r', x ,  len(matrix[y]) - self.THRESHOLD)

        print('t', y, self.THRESHOLD)

        print('b', y , len(matrix)- self.THRESHOLD)


        if x < self.THRESHOLD:
            return 'left'
        elif x >= len(matrix[y]) - self.THRESHOLD:  
            return 'right'
        elif y <= self.THRESHOLD:  
            return 'top'
        elif y >= len(matrix)- self.THRESHOLD:  
            return 'bottom'

    def generate_new_section(self, position):
       
        if position == 'left':
        
            pass
        elif position == 'right':
     
            pass
        elif position == 'top':
        
            pass
        elif position == 'bottom':
       
            pass
        
            

        
        