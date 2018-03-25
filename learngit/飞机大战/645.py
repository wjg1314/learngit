import pygame

# 屏幕的高度, 好比是常量，不对其进行修改
SCREEN_HEIGHT = 768
SCREEN_WIDTH = 512


# 地图类
class GameMap(object):
    def __init__(self):
        # 加载图片创建两个图片对象
        self.bg_img1 = pygame.image.load("res/img_bg_level_5.jpg")
        self.bg_img2 = pygame.image.load("res/img_bg_level_5.jpg")

        # 获取背景图片矩形对象
        self.bg_img1_rect = self.bg_img1.get_rect()
        self.bg_img2_rect = self.bg_img2.get_rect()

        # 修改矩形对象y坐标
        self.bg_img1_rect[1] = 0 - SCREEN_HEIGHT
        self.bg_img2_rect[1] = 0

        # 地图滚动速度
        self.map_speed = 3

    # 滚动图片
    def scroll_map(self):
        # 移动矩形对象
        self.bg_img2_rect.move_ip(0, self.map_speed)
        self.bg_img1_rect.move_ip(0, self.map_speed)
        # 判断矩形对象是否超出屏幕如果某个矩形对象超出屏幕设置到屏幕顶部的外面显示
        if self.bg_img2_rect[1] >= SCREEN_HEIGHT:
            print("第二个图片超出屏幕啦")
            # 重置位置到屏幕的外面
            self.bg_img2_rect[1] = -SCREEN_HEIGHT

        if self.bg_img1_rect[1] >= SCREEN_HEIGHT:
            print("第一个图片超出屏幕啦")
            # 重置位置到屏幕的外面
            self.bg_img1_rect[1] = -SCREEN_HEIGHT


# 定义游戏窗口类
class GameWindow(object):
    def __init__(self):
        # 初始化pygame
        pygame.init()
        # 创建游戏窗口
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        # 设置标题
        pygame.display.set_caption("飞机大战")
        # 加载图片，创建图片对象
        icon_img = pygame.image.load("res/app.ico")
        # 设置icon
        pygame.display.set_icon(icon_img)
        # 创建地图对象
        self.map = GameMap()


    # 让游戏运行起来
    def run(self):
        while True:
            # 获取窗口操作的事件列表
            event_list = pygame.event.get()
            for event in event_list:
                if event.type == pygame.QUIT:
                    # 表示用户点击关闭按钮的事件
                    exit()
                elif event.type == pygame.KEYDOWN:
                    # 表示键盘按下事件类型
                    if event.key == pygame.K_ESCAPE:
                        # 表示用户按下了esc按键
                        exit()
                    elif event.key == pygame.K_SPACE:
                        print("biubiu")


            # 获取键盘上长按的键
            keys = pygame.key.get_pressed()
            # 判断关心长按的键
            if keys[pygame.K_UP]:
                print("上")
            elif keys[pygame.K_DOWN]:
                print("下")
            elif keys[pygame.K_LEFT]:
                print("左")
            elif keys[pygame.K_RIGHT]:
                print("右")

            # 滚动地图
            self.map.scroll_map()
            # 绘制地图滚动后的位置
            self.window.blit(self.map.bg_img1, (self.map.bg_img1_rect[0], self.map.bg_img1_rect[1]))
            self.window.blit(self.map.bg_img2, (self.map.bg_img2_rect[0], self.map.bg_img2_rect[1]))
            # 刷新窗口
            pygame.display.update()

# 判断是否是主模块
if __name__ == '__main__':
    # 测试代码
    # 创建游戏窗口对象
    game_window = GameWindow()
    game_window.run()