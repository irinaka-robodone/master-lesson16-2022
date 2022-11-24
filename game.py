# import object
import pygame


SCREEN_SIZE = (900,425)  #全部大文字のやつは定数  

def init():
    pygame.init()
    pygame.display.set_caption("なんかよくわからないもの")
    window = pygame.display.set_mode(SCREEN_SIZE)
    
    # player = object.player(100,10,10)　←エラー？
    teki = object.teki(100,100)
    
    
    while True:
        pygame
    
def main():
    ckock = pygame.time.Clock()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        ckock.tick(40)  
init()

main()