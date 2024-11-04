import pygame
import sys
import random

def render_alarm():
    click_surf = font.render("Click!", True, (20, 20, 25)).convert_alpha()
    click_rect = click_surf.get_rect(center=(500, 300))
    screen.blit(click_surf, click_rect)

def render_instructions():
    wait_surf = font.render("Wait for green", True, (200, 200, 200)).convert_alpha()
    wait_rect = wait_surf.get_rect(center = (500, 300))
    screen.blit(wait_surf, wait_rect)

def render_start():
    title_surf_list = [title_font.render("Reaction Speed Test", True, (20, 20, 20)), 
                       title_font.render("Clicked Too Soon!", True, (20, 20, 20)),
                       title_font.render(f"Reaction Time: {reaction_speed} ms", True, (255, 255, 255)).convert_alpha()]
    title_rect = title_surf_list[start_index].get_rect(center = (500, 200))
    instructions_surf_list = [font.render("Click to begin", True, (20, 20, 20)), 
                              font.render("Click to restart", True, (20, 20, 20)),
                              font.render("Click to try again", True, (20, 20, 20))]
    instructions_rect = instructions_surf_list[start_index].get_rect(center = (500, 400))
    screen.blit(title_surf_list[start_index], title_rect)
    screen.blit(instructions_surf_list[start_index], instructions_rect)

pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Reaction Speed Test")
red = (255, 88, 51)
blue = (59, 142, 165)
green = (152, 255, 143)
game_running = True
background_color = blue
screen.fill(background_color)
reaction_speed = 0
font = pygame.font.SysFont("Antipasto.ttf", 100)
title_font = pygame.font.SysFont("Antipasto.ttf", 125)
start_time = pygame.time.get_ticks()
start_index = 0
wait_time = 1000
clock = pygame.time.Clock()
state = "Start"
pygame.display.update()


while game_running:
    current_time = pygame.time.get_ticks()
    screen.fill(background_color)
    if state == "Start":
        background_color = blue
        render_start()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                state = "Running"
                random_time = random.randint(1000, 6000)
                start_time = pygame.time.get_ticks()
                background_color = red
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    elif state == "Running":
        if background_color == red:
            render_instructions()

        if (current_time - start_time) > (wait_time + random_time):
            background_color = green
            render_alarm()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if background_color == green:
                    reaction_speed = current_time - start_time - wait_time - random_time
                    state = "Start"
                    start_index = 2
                elif background_color == red:
                    state = "Start"
                    start_index = 1
    
    pygame.display.update()
    clock.tick(60)
