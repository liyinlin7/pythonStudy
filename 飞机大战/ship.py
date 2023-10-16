import pygame

class Ship:
    """管理飞船的类"""

    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        '''
        使用方法get_rect() 访问屏幕的属性rect ，并将其赋给了self.screen_rect ，这让我们能够将飞船放到屏幕的正确位置。
        '''
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')  # 调用pygame.image.load() 加载图像
        self.rect = self.image.get_rect()  # 使用get_rect() 获取相应surface的属性rect ，以便后面能够使用它来指定飞船的位置

        # 对于每艘新飞船，都将其放在屏幕底部的中央
        '''
        处理rect 对象时，可使用矩形四角和中心的 坐标和 坐标。可通过设置这些值来指定矩形的位置。要让游戏元素居中，可设置相应
        rect 对象的属性center 、centerx 或centery ；要让游戏元素与屏幕边缘对齐，可使用属性top 、bottom 、left 或right 。除此
        之外，还有一些组合属性，如midbottom 、midtop 、midleft 和midright 。要调整游戏元素的水平或垂直位置，可使用属性x 和y
        ，分别是相应矩形左上角的 坐标和 坐标。这些属性让你无须做游戏开发人员原本需要手工完成的计算，因此会经常用到。
        
        注意 在Pygame中，原点(0, 0)位于屏幕左上角，向右下方移动时，坐标值将增大。在1200 × 800的屏幕上，原点位于左上
        角，而右下角的坐标为(1200, 800)。这些坐标对应的是游戏窗口，而不是物理屏幕。我们要将飞船放在屏幕底部的中央。为此，
        将self.rect.midbottom 设置为表示屏幕的矩形的属性midbottom 。Pygame使用这些 rect 属性来放置飞船图
        像，使其与屏幕下边缘对齐并水平居中。

        '''
        self.rect.midbottom = self.screen_rect.midbottom
        # 在飞船的属性X,Y中存储小数值
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船而不是rect对象x值
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0 :
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.top < self.settings.screen_height - self.rect.height:
            self.y += self.settings.ship_speed
        # 根据self.x 更新rect对象
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)  # 方法blitme() ，它将图像绘制到self.rect 指定的位置。

    def center_ship(self):
        """让飞船在屏幕底端居中。"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float( self.rect.x )