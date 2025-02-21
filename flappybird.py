import pygame
import random

pygame.init()

WIDTH, HEIGHT  = 400, 600
BIRD_X, BIRD_Y = 50, 300
GRAVITY = 0.5
JUMP_STRENGTH = -10
PIPE_WIDTH, PIPE_GAP, PIPE_SPEED = 70, 200, 3

WHITE, GREEN, BLUE = (255,255,255), (0,255,0), (0,0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

bird = pygame.Rect(BIRD_X, BIRD_Y,30,30)
pipes = []

running = True
bird_velocity = 0

def createPipe():
    height = random.randint(100, 400)
    top = pygame.Rect(WIDTH, 0, PIPE_WIDTH, height)
    bottom = pygame.Rect(WIDTH, height+PIPE_GAP, PIPE_WIDTH, HEIGHT-height-PIPE_GAP)
    return top, bottom

pipes.append(createPipe())

while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocirty = JUMP_STRENGTH
                
    bird_velocity += GRAVITY
    bird.y += bird_velocity
    
    for pipe in pipes:
        pipe[0].x -= PIPE_SPEED
        pipe[1].x -= PIPE_SPEED
        
    if pipes[0][0].x < -PIPE_WIDTH:
        pipes.pop(0)
        pipes.append(createPipe())
        
    pygame.draw.rect(screen, BLUE, bird)
    
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, pipe[0])
        pygame.draw.rect(screen, BLUE, pipe[1])
        
    
    for pipe in pipes:
        if bird.colliderect(pipe[0]) or bird.colliderect(pipe[1]) or bird.y>=HEIGHT:
            running = False
            
    pygame.display.update()
    clock.tick(30)
    
pygame.quit()
            
        