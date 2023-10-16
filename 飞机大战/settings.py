class Settings:
    """存储游戏  中所有的设置类 """

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 1200  #  宽
        self.screen_height = 800  # 高
        self.bg_color = (230, 230, 230)  # 背景色

        # 飞船设置
        '''
        将ship_speed 的初始值设置为1.5 。现在需要移动飞船时，每次循环将移动1.5像素而不是1像素。
        '''
        # 飞船设置
        self.ship_speed = 1.5
        self.ship_limit = 3
        # 子弹设置
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        # 外星人设置
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # feleet_direction 为1表示向右移，为-1表示向左移
        self.fleet_direction = 1