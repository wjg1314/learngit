import pygame
import time
pygame.init()
window = pygame.display.set_mode((512,768))
pygame.display.set_caption('飞机大战')
ico_img = pygame.image.load('res/app.ico')
pygame.display.set_icon(ico_img)
bg_img = pygame.image.load('res/img_bg_level_4.jpg')
window.blit(bg_img,(0,0))
enemy_img = pygame.image.load('res/img-plane_4.png')
enemy_img_rect = enemy_img.get_rect()
enemy_img_rect[0] = 100
enemy_img_rect[1] = 300
for i in range(10):
    window.blit(bg_img,(0,0))
    window.blit(enemy_img,(enemy_img_rect[0],enemy_img_rect[1]))
    enemy_img_rect.move_ip(0,10)
    # print(enemy_img_rect)

    pygame.display.update()
    time.sleep(0.3)
input()