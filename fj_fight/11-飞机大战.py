import pygame
import random
import time


# 屏幕的高度, 好比是常量，不对其进行修改
SCREEN_HEIGHT = 768
SCREEN_WIDTH = 512

# 定义敌机类
class EnemyPlane(object):
    def __init__(self):
        # 产生随机数字 1-7
        num = random.randint(1, 7)
        # 加载图片，创建图片对象
        self.enemy_img = pygame.image.load("res/img-plane_%d.png" % num)
        # 获取敌机的矩形对象，以后根据矩形对象的位置绘制敌机显示的位置
        self.enemy_img_rect = self.enemy_img.get_rect()
        # 修改敌机矩形对象的位置
        self.enemy_img_rect[0] = random.randint(0, SCREEN_WIDTH - self.enemy_img_rect[2])
        self.enemy_img_rect[1] = -self.enemy_img_rect[3]

        # 随机产生移动速度
        self.enemy_speed = random.randint(4, 6)
        # self.reset()

    # 敌机绘制重置
    def reset(self):
        self.enemy_img_rect[0] = random.randint(0, SCREEN_WIDTH - self.enemy_img_rect[2])
        self.enemy_img_rect[1] = -self.enemy_img_rect[3]

        # 随机产生移动速度
        self.enemy_speed = random.randint(4, 6)

    # 向下移动
    def move_down(self):
        self.enemy_img_rect.move_ip(0, self.enemy_speed)
        if self.enemy_img_rect[1] > SCREEN_HEIGHT:
            # 重置敌机位置
            self.reset()





# 子弹类
class Bullet(object):
    def __init__(self):
        # 产生随机数字
        num = random.randint(8, 13)
        # 加载图片，创建图片对象
        self.bullet_img = pygame.image.load("res/bullet_%d.png" % num)

        # 获取图片的矩形对象
        # 提示： 子弹矩形对象不做调整，因为飞机的位置我们现在不能确定，等飞机发射子弹的时候获取飞机的位置，然后在设置子弹在飞机头部
        self.bullet_img_rect = self.bullet_img.get_rect()

        # 子弹状态
        self.is_shot = False
        # 子弹的移动速度
        self.bullet_speed = 5

    # 向上移动
    def move_up(self):
        self.bullet_img_rect.move_ip(0, -self.bullet_speed)
        # 判断子弹是否超出屏幕
        if self.bullet_img_rect[1] < -self.bullet_img_rect[3]:
            # 回收这颗子弹，把状态进行修改
            self.is_shot = False



# 英雄飞机类
class HeroPlane(object):
    def __init__(self):
        # 加载图片，创建图片对象
        self.hero_img = pygame.image.load("res/hero2.png")
        # 获取图片矩形对象，以后矩形对象移动到哪里，图片对象就绘制到那个地方
        self.hero_img_rect = self.hero_img.get_rect()
        # 修改矩形对象的位置
        self.hero_img_rect[0] = SCREEN_WIDTH / 2 - self.hero_img_rect[2] / 2
        self.hero_img_rect[1] = SCREEN_HEIGHT - self.hero_img_rect[3] - 20
        # 移动速度
        self.hero_speed = 5
        # 携带子弹列表
        self.bullet_list = [Bullet() for _ in range(5)]


    # 重置飞机位置
    def reset(self):
        # 修改矩形对象的位置
        self.hero_img_rect[0] = SCREEN_WIDTH / 2 - self.hero_img_rect[2] / 2
        self.hero_img_rect[1] = SCREEN_HEIGHT - self.hero_img_rect[3] - 20


    # 发射子弹
    def shot(self):
        # 遍历子弹，判断子弹的状态
        for bullet in self.bullet_list:
            if not bullet.is_shot:
                # 发射子弹
                # 修改子弹的状态
                bullet.is_shot = True
                bullet_x = self.hero_img_rect[0] + self.hero_img_rect[2] / 2 - bullet.bullet_img_rect[2] / 2
                # 修改子弹的位置到飞机头部
                bullet.bullet_img_rect[0] = bullet_x
                bullet.bullet_img_rect[1] = self.hero_img_rect[1] - bullet.bullet_img_rect[3]
                # 只发射一颗子弹，找到一颗未发射的子弹，把子弹状态进行修改然后跳出循环，不再修改后面子弹的状态
                break


    # 上
    def move_up(self):
        # y轴大于屏幕的顶部坐标（0）才能往上移动
        if self.hero_img_rect[1] > 0:
            self.hero_img_rect.move_ip(0, -self.hero_speed)

    # 下
    def move_down(self):
        # y轴小于屏幕的高度减去飞机高度才能往下移动
        if self.hero_img_rect[1] < SCREEN_HEIGHT - self.hero_img_rect[3]:
            self.hero_img_rect.move_ip(0, self.hero_speed)

    # 左
    def move_left(self):
        # x轴大于0表示可以往左边移动
        if self.hero_img_rect[0] > 0:
            self.hero_img_rect.move_ip(-self.hero_speed, 0)

    # 右
    def move_right(self):
        # x轴小于屏幕宽度减去自身的宽度才可以往右移动
        if self.hero_img_rect[0] < SCREEN_WIDTH - self.hero_img_rect[2]:
            self.hero_img_rect.move_ip(self.hero_speed, 0)


# 地图类
class GameMap(object):
    def __init__(self):
        # 加载图片创建两个图片对象
        self.bg_img3 = pygame.image.load("res/111.jpg")
        self.bg_img1 = pygame.image.load("res/img_bg_level_5.jpg")
        self.bg_img2 = pygame.image.load("res/img_bg_level_5.jpg")

        # 获取背景图片矩形对象
        # self.bg_img3_rect = self.bg_img3.get_rect()
        self.bg_img1_rect = self.bg_img1.get_rect()
        self.bg_img2_rect = self.bg_img2.get_rect()

        # 修改矩形对象y坐标
        self.bg_img1_rect[1] = 0 - SCREEN_HEIGHT
        self.bg_img2_rect[1] = 0
        # self.bg_img3_rect[1] = 0


        # 地图滚动速度
        self.map_speed = 3

    # 滚动图片
    def scroll_map(self):
        # 移动矩形对象
        # self.bg_img3_rect.move_ip(0, self.map_speed)
        self.bg_img2_rect.move_ip(0, self.map_speed)
        self.bg_img1_rect.move_ip(0, self.map_speed)
        # 判断矩形对象是否超出屏幕如果某个矩形对象超出屏幕设置到屏幕顶部的外面显示
        # if self.bg_img3_rect[1] >= SCREEN_HEIGHT:
        #     print("第二个图片超出屏幕啦")
        #     # 重置位置到屏幕的外面
        #     del self.bg_img3_rect
        #     # self.bg_img2_rect[1] = -SCREEN_HEIGHT
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
        # 创建飞机
        self.hero_plane = HeroPlane()
        # 敌机列表
        self.enemy_list = [EnemyPlane() for _ in range(5)]
        # 播放背景音乐
        self.play_bg_music()
        # 创建爆炸音效
        self.bz_sound = pygame.mixer.Sound("res/baozha.ogg")
        # 创建游戏结束的音效
        self.over_sound = pygame.mixer.Sound("res/gameover.wav")
        # 当前得分
        self.score = 0

    # 播放背景音乐
    def play_bg_music(self):
        # 加载背景音乐
        pygame.mixer.music.load("res/bg2.ogg")
        # 循环播放背景音乐
        pygame.mixer.music.play(-1)

    # 释放音乐及音效资源
    def release_mixer(self):
        pygame.mixer.music.stop()
        self.bz_sound.stop()


    # 窗口事件处理
    def handle_event(self):
        # 获取窗口操作的事件列表
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                # 表示用户点击关闭按钮的事件
                self.release_mixer()
                exit()
            elif event.type == pygame.KEYDOWN:
                # 表示键盘按下事件类型
                if event.key == pygame.K_ESCAPE:
                    # 表示用户按下了esc按键
                    # 释放音乐及音效资源
                    self.release_mixer()
                    exit()
                elif event.key == pygame.K_SPACE:
                    print("biubiu")
                    # 发射子弹
                    self.hero_plane.shot()

        # 获取键盘上长按的键
        keys = pygame.key.get_pressed()
        # 判断关心长按的键
        if keys[pygame.K_UP]:
            self.hero_plane.move_up()
        elif keys[pygame.K_DOWN]:
            self.hero_plane.move_down()
        elif keys[pygame.K_LEFT]:
            self.hero_plane.move_left()
        elif keys[pygame.K_RIGHT]:
            self.hero_plane.move_right()



    # 移动及绘制图片对象
    def move_draw(self):
        # 滚动地图
        self.map.scroll_map()
        # 绘制地图滚动后的位置
        self.window.blit(self.map.bg_img3, (self.map.bg_img1_rect[0], self.map.bg_img1_rect[1]))
        self.window.blit(self.map.bg_img1, (self.map.bg_img1_rect[0], self.map.bg_img1_rect[1]))
        self.window.blit(self.map.bg_img2, (self.map.bg_img2_rect[0], self.map.bg_img2_rect[1]))

        # 绘制敌机
        for enemy in self.enemy_list:
            # 向下移动
            enemy.move_down()
            # 绘制移动后的位置
            self.window.blit(enemy.enemy_img, (enemy.enemy_img_rect[0], enemy.enemy_img_rect[1]))

        # 绘制飞机
        self.window.blit(self.hero_plane.hero_img, (self.hero_plane.hero_img_rect[0],
                                                   self.hero_plane.hero_img_rect[1]))

        # 遍历子弹列表获取已经发射的状态子弹，让其向上移动
        for bullet in self.hero_plane.bullet_list:
            # 判断子弹是否是发射的状态
            if bullet.is_shot:
                # 发射的子弹向上移动
                bullet.move_up()
                # 绘制移动后的子弹
                self.window.blit(bullet.bullet_img, (bullet.bullet_img_rect[0],bullet.bullet_img_rect[1]))

        # 绘制得分
        self.draw_text("得分:%d" % self.score, 25, 10, 10)


    # 刷新窗口
    def window_update(self):
        pygame.display.update()


    # 检测子弹和敌机的碰撞
    def bullet_hit_enemy(self):
        # 遍历飞机上的子弹列表
        for bullet in self.hero_plane.bullet_list:
            # 判断子弹是否是发射状态
            if bullet.is_shot:
                # 表示发射状态，然后遍历敌机列表于每一架敌机检测是否碰撞
                for enemy in self.enemy_list:
                    # 检测矩形对象是否碰撞
                    if pygame.Rect.colliderect(bullet.bullet_img_rect, enemy.enemy_img_rect):
                        # 碰撞啦
                        # 修改当前分数
                        self.score += 1
                        # 播放爆炸音效
                        self.bz_sound.play()
                        # 子弹回收，修改状态
                        bullet.is_shot = False
                        # 敌机位置重置
                        enemy.reset()
                        # 提示： 一个子弹消灭一架飞机，检测到碰撞不要再和后面的敌机在检测了，需要跳出循环
                        break

    # 检测飞机和敌机是否相撞
    def is_hit_enemy(self):
        # 遍历敌机列表获取敌机
        for enemy in self.enemy_list:
            # 判断是否相撞
            if pygame.Rect.colliderect(enemy.enemy_img_rect, self.hero_plane.hero_img_rect):
                # 碰撞啦
                return True
        else:
            # 如果遍历每一架敌机都没有和我们的飞机进行碰撞可以返回False
            return False

    # 让游戏运行起来
    def run(self):

        while True:

            # 加载图片创建两个图片对象
            self.bg_img3 = pygame.image.load("res/img_bg_level_3.jpg")
            self.window.blit(self.map.bg_img3, (0,0))
            pygame.display.update()
            event_list = pygame.event.get()
            for event in event_list:

                if event.type == pygame.KEYDOWN:
                    # 表示键盘按下事件类型

                    if event.key == pygame.K_SPACE:

                        # 发射子弹
                        self.hero_plane.shot()
                        while True:
                            # 窗口处理事件
                            self.handle_event()
                            # 移动及绘制图片对象
                            self.move_draw()
                            # 刷新窗口
                            self.window_update()
                            # 检测子弹和敌机的碰撞
                            self.bullet_hit_enemy()
                            # 检测飞机和敌机是否相撞
                            if self.is_hit_enemy():
                                break
                        # 游戏结束
                        self.game_over()


    # 游戏结束
    def game_over(self):
        # 停止播放背景音乐
        pygame.mixer.music.stop()
        # 播放游戏结束的音效
        self.over_sound.play()

        # 绘制得分
        self.draw_text("得分:%d" % self.score, 25, 10, 10)

        # 播放游戏结束的音效
        # 绘制得分 shift + tab 往左缩进
        self.draw_text("游戏结束(esc退出) 得分:%d" % self.score, 35, 60, 350)
        # 手动刷新显示文字
        self.window_update()
        # 等待用户输入
        self.wait_input()


    # 等待用户输入操作
    def wait_input(self):
        while True:
            # 获取窗口操作的事件列表
            event_list = pygame.event.get()
            for event in event_list:
                if event.type == pygame.QUIT:
                    # 表示用户点击关闭按钮的事件
                    self.release_mixer()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    # 表示键盘按下事件类型
                    if event.key == pygame.K_ESCAPE:
                        # 表示用户按下了esc按键
                        # 释放音乐及音效资源
                        self.release_mixer()
                        exit()
                    elif event.key == pygame.K_RETURN:
                        # 继续完成
                        # 播放背景音乐
                        pygame.mixer.music.play(-1)
                        # 分数重置
                        self.score = 0
                        # 飞机重置
                        self.hero_plane.reset()
                        # 敌机重置
                        for enemy in self.enemy_list:
                            enemy.reset()
                        # return 代码执行到return关键字表示方法或者函数执行结束
                        return


    # 绘制文字
    def draw_text(self, text, font_size, x, y):
        font = pygame.font.SysFont("simhei", font_size)
        # 根据字体对象创建文字对象
        txt_obj = font.render(text, True, (255, 255, 255))
        # 绘制文字对象
        self.window.blit(txt_obj, (x, y))


# 判断是否是主模块
if __name__ == '__main__':
    # 测试代码
    # 创建游戏窗口对象
    game_window = GameWindow()
    game_window.run()