import pygame
pygame.init()
window = pygame.display.set_mode((512,768))
pygame.display.set_caption('飞机大战')
ico_img = pygame.image.load('res/app.ico')
pygame.display.set_icon(ico_img)
input()