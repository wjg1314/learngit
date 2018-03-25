import pygame
SCREEN_HEIGHT =768
SCREEN_WIDTH =512

class GameMap(object):
    def __init__(self):
        self.bg_img1 = pygame.image.load('res/img_bg_level_4.jpg')
        self.bg_img2 = pygame.image.load('res/img_bg_level_4.jpg')
        self.hero_img = pygame.image.load("res/hero2.png")
        self.bg_img1_rect = self.bg_img1.get_rect()
        self.bg_img2_rect = self.bg_img2.get_rect()
        self.bg_img1_rect[1] = 0 - SCREEN_HEIGHT
        self.bg_img2_rect[1] = 0
        self.map_speed =3
    def scroll_map(self):
        self.bg_img2_rect.move_ip(0,self.map_speed)
        self.bg_img1_rect.move_ip(0,self.map_speed)
        if self.bg_img2_rect[1] >= SCREEN_HEIGHT:
            print('2超出屏幕了')
            self.bg_img2_rect[1] = -SCREEN_HEIGHT
        if self.bg_img1_rect[1] >= SCREEN_HEIGHT:
            print('1超出屏幕了')
            self.bg_img1_rect[1] = -SCREEN_HEIGHT
class Plane(object):
    # def __init__(self):
    def plane(self):
        self.hero_img = pygame.image.load("res/hero2.png")
        self.hero_img_rect = self.hero_img.get_rect()
        self.hero_img_rect[0] = SCREEN_WIDTH /2 - self.hero_img_rect[2] / 2
        self.hero_img_rect[1] = SCREEN_HEIGHT - self.hero_img_rect[3] - 20
        self.hero_speed = 5
        # self.bullet_list = [Bullet() for  _ in range(5)]
    def move_up(self):
        if self.hero_img_rect[1] > 0:
            self.hero_img_rect.move_ip(0, -self.hero_speed)
    def move_down(self):
        if self.hero_img_rect[1] < SCREEN_HEIGHT - self.hero_img_rect[3]:
            self.hero_img_rect.move_ip(0, self.hero_speed)
    def move_left(self):
        if self.hero_img_rect[0] > 0:
            self.hero_img_rect.move_ip(-self.hero_speed,0)
    def move_right(self):
        if self.hero_img_rect[0] < SCREEN_WIDTH - self.hero_img_rect[2]:
            self.hero_img_rect.move_ip(-self.hero_speed,0)
    def shot(self):
        pass




class GameWindow(object):
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        pygame.display.set_caption('飞机大战')
        icon_img = pygame.image.load('res/app.ico')
        pygame.display.set_icon(icon_img)
        self.map = GameMap()

    def run(self):
        while True:
            event_list = pygame.event.get()
            for event in event_list:
                if event.type ==pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN:

                    if event.key ==pygame.K_ESCAPE:
                        exit()
                    elif event.key == pygame.K_SPACE:
                        print('biubiub')
                        # exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                print('上')
            elif keys[pygame.K_DOWN]:
                print('下')
            elif keys[pygame.K_LEFT]:
                print('左')
            elif keys[pygame.K_RIGHT]:
                print('右')

            self.map.scroll_map()
            self.window.blit(self.map.bg_img1, (self.map.bg_img1_rect[0],self.map.bg_img1_rect[1]))
            self.window.blit(self.map.bg_img2, (self.map.bg_img2_rect[0],self.map.bg_img2_rect[1]))
            # self.plane()
            pygame.display.update()
            # self.hero()


if __name__ == '__main__':
    game_window = GameWindow()
    game_window.run()