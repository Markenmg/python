import pygame
import time
import random

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

Bg = pygame.transform.scale(pygame.image.load("bg.jpg"), (WIDTH, HEIGHT))

player_Height = 40
player_width = 60

def draw(player):
    WIN.blit(Bg, (0,0))
    pygame.draw.rect(WIN, (255, 0, 0), player)#Red
    
    
    
    pygame.display.update()
    
def main():
    run = True
     
    player = pygame.Rect(200, HEIGHT - player_Height , player_width, player_Height) 


    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  
                break
    
        draw(player)

     
    pygame.quit()

if __name__ == "__main__":
    main()