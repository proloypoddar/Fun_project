# import
import pygame, sys, random

pygame.init()  # initializing
screen = pygame.display.set_mode((800, 600))  # display surface

clock = pygame.time.Clock()  # determine speed / frame rate of the game
bg = pygame.image.load('wood_bg.png')  # same folder
land_bg = pygame.image.load('land_bg.png')  # land image
water = pygame.image.load('water_bg.png')  # water image
cloud_1 = pygame.image.load('cloud1.png')  # cloud img 1
cloud_2 = pygame.image.load('cloud2.png')  # cloud img 2


while True:  # game loop
    for event in pygame.event.get():  # when the while loop starts
        # pygame starts looking for all the events
        if event.type == pygame.QUIT:  # closing
            pygame.quit()  # close pygame
            sys.exit()  # close all the program

    screen.blit(bg, (0, 0))


    screen.blit(land_bg, (0, 500))
    screen.blit(water, (0, 550))
    screen.blit(cloud_1, (30, 30))
    screen.blit(cloud_2, (150, 70))
    screen.blit(cloud_1, (350, 40))
    screen.blit(cloud_2, (550, 65))
    screen.blit(cloud_1, (700, 50))

    pygame.display.update()
    clock.tick(60)  # frame rate
