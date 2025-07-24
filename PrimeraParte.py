import pygame
import os

pygame.init()

# Configuración de la pantalla
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Juego del Dinosaurio")

# Cargar imágenes del dinosaurio
RUNNING = [pygame.image.load("Assets/Dino/DinoRun1.png"),
           pygame.image.load("Assets/Dino/DinoRun2.png")]
JUMPING = pygame.image.load("Assets/Dino/DinoJump.png")

# Función principal
def main():
    run = True
    clock = pygame.time.Clock()
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        # Llenar la pantalla de blanco
        SCREEN.fill((255, 255, 255))
        
        # Dibujar el dinosaurio en una posición fija
        SCREEN.blit(RUNNING[0], (80, 310))
        
        clock.tick(30)
        pygame.display.update()

main()