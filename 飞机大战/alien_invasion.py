import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import  Button
from time import sleep

class AlienInvasion:
    '''
        管理游戏资源和行为的类
    '''

    def __init__(self):
        '''
            初始化游戏并创建游戏资源
        '''
        pygame.init()
        '''
        调用pygame.display.set_mode() 来创建一个显示窗口，游戏的所有图形元素都将在其中绘制。实参(1200,800) 是一个元组，
        指定了游戏窗口的尺寸——宽1200像素、高800像素（你可以根据自己的显示器尺寸调整这些值）。
        将这个显示窗口赋给属性self.screen ，让这个类中的所有方法都能够使用它。
        '''
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        """全屏模式"""
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")   # 设置窗口的名称
        # 创建一个用于存储游戏统计信息的实例
        self.stats = GameStats(self)

        '''
        导入Ship 类，并在创建屏幕后创建一个Ship 实例。调用Ship() 时，必须ᨀ供一个参数：一个AlienInvasion 实例。在
        这里，self 指向的是当前AlienInvasion 实例。这个参数让Ship能够访问游戏资源，如对象screen 。我们将这个Ship 实例赋给了self.ship 。
        '''
        self.ship = Ship(self)
        '''
        pygame.sprite.Group 类似于列表，但ᨀ供了有助于开发游戏的额外功能。
        在主循环中，将使用这个编组在屏幕上绘制子弹以及更新每颗子弹的位置。
        '''
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
        # 创建Play按钮
        self.play_button = Button(self, "Play")


    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events() # 监控键盘和鼠标
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets() # 更新子弹位置并删除子弹
                self._update_aliens()  # 移动外星人
            self._update_screen() # 每次循环时都会重绘屏幕

    def _check_events(self):
        """响应按键和鼠标事件"""
        ''' 
        为访问Pygame检测到的事件，我们使用了函 数pygame.event.get() 。这个函数返回一个列表，其中包含它在
        上一次被调用后发生的所有事件。所有键盘和鼠标事件都将导致这个for 循环运行。在这个循环中，我们将编写一系列if 语句来检
        测并响应特定的事件。例如，当玩家单击游戏窗口的关闭按钮时，将检测到pygame.QUIT 事件，进而调用sys.exit() 来退出游戏
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button( mouse_pos )

    def _check_keydown_events(self, event):
        """响应按键 按下"""
        if event.key == pygame.K_RIGHT:
            # 向右移动飞船
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # 向左移动飞船
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            # 向上移动飞船
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            # 向下移动飞船
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """响应按钮 松开"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            # 向左移动飞船
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            # 向上移动飞船
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            # 向下移动飞船
            self.ship.moving_down = False

    def _fire_bullet(self):
        """创建一颗子弹，并将其加入编组bullets中"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        """更新子弹的位置并删除消失的子弹"""
        # 更新子弹的位置
        self.bullets.update()
        # 删除消失的子弹
        '''
        使用for 循环遍历列表（或Pygame编组）时，Python要求该列表的长度在整个循环中保持不变。因为不能从for 循环遍历的列表或编
        组中删除元素，所以必须遍历编组的副本。我们使用方法copy()来设置for 循环，从而能够在循环中修改bullets 。我们
        检查每颗子弹，看看它是否从屏幕顶端消失。如果是，就将其从bullets 中删除。
        '''
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove( bullet )
        # print(len(self.bullets))  # 查看子弹的数量
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """响应子弹和外星人碰撞。"""

        # 删除发生碰撞的子弹和外星人。
        collisions = pygame.sprite.groupcollide( self.bullets, self.aliens, True, True )
        if not self.aliens:
            # 删除现有的所有子弹，并创建一群新的外星人。
            self.bullets.empty()
            self._create_fleet()

    def _create_fleet(self):
        """创建外星人群"""
        # 创建一个外星人并计算一行可容纳多少个外星人
        # 外星人的间距为外星人宽度
        alien = Alien(self)
        '''
        从外星人的rect 属性中获取外星人宽度和高度，并将这个值存储到alien_width ，alien_height中，以免反复访问属性rect 。
        '''
        alien_width, alien_height = alien.rect.size
        '''
        计算可用于放置外星人的水平空间以及其中可容纳多少个外星人
        '''
        available_space_x = self.settings.screen_width - ( 2 * alien_width )
        number_aliens_x = available_space_x // ( 2 * alien_width )
        # 计算屏幕可容纳多少行外星人
        ship_height = self.ship.rect.height
        available_space_y = ( self.settings.screen_height - ( 3 * alien_height ) - ship_height )
        number_rows = available_space_y // ( 2 * alien_height )
        # 创建第一行外星人
        for row_number in range(number_rows):
            for alien_number in range( number_aliens_x ):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        # 创建一个外星人并将其加入当前行
        '''
       在这个循环中，创建一个新的外星人，并通过设置 坐标将其加入当前行。将每个外星人都往右推一个外星人宽度。接下来，
       将外星人宽度乘以2，得到每个外星人占据的空间（其中包括右边的空白区域），再据此计算当前外星人在当前行的位置。我们使用
       外星人的属性x 来设置其rect 的位置。
       '''
        alien = Alien( self )
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add( alien )

    def _check_fleet_edges(self):
        """外星人到达边缘时采取相应的措施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """将整群外星人下移，并改变他们的方向"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_aliens_bottom(self):
        """检查是否有外星人到达了屏幕底端。"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # 像飞船被撞到一样处理。
                self._ship_hit()
                break

    def _check_play_button(self, mouse_pos):
        """在玩家单击Play按钮时开始新游戏。"""
        button_clicked = self.play_button.rect.collidepoint( mouse_pos )
        if button_clicked and not self.stats.game_active:
            # 重置游戏统计信息。
            self.stats.reset_stats()
            self.stats.game_active = True
            # 清空余下的外星人和子弹。
            self.aliens.empty()
            self.bullets.empty()
            # 创建一群新的外星人并让飞船居中。
            self._create_fleet()
            self.ship.center_ship()

    def _ship_hit(self):
        """ 响应飞船被外星人撞倒"""
        if self.stats.ships_left > 0:
            # 将ships_left 减1
            self.stats.ships_left -= 1
            # 清空余下的外星人和子弹
            self.aliens.empty()
            self.bullets.empty()
            # 创建一群新的外星人，并将飞船放到屏幕底端的中央
            self._create_fleet()
            self.ship.center_ship()
            # 暂停
            sleep(0.5)
        else:
            self.stats.game_active = False

    def _update_aliens(self):
        """
        检查是否有外星人位于屏幕边缘，并更新整群外星人的位置
        """
        self._check_fleet_edges()
        self.aliens.update()
        # 检查是否有外星人撞倒飞船
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        # 检查是否有外星人到达了屏幕底端
        self._check_aliens_bottom()

    def _update_screen(self):
        """更新屏幕上的图片，并切换到新屏幕"""
        '''
        设置背景色:  调用方法fill() 用这种背景色填充屏幕。方法fill() 用于处理surface，只接受一个实参：一种颜色。
        '''
        self.screen.fill( self.settings.bg_color )
        '''
        调用ship.blitme() 将飞船绘制到屏幕上，确保它出现在背景前面
        '''
        self.ship.blitme()
        # 让最近绘制的屏幕可见
        '''
        方法bullets.sprites() 返回一个列表，其中包含编组bullets中的所有精灵。
        为在屏幕上绘制发射的所有子弹，遍历编组bullets 中的精灵，并对每个精灵调用draw_bullet()
        '''
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # 如果游戏处于非活动状态，就绘制Play按钮。
        if not self.stats.game_active:
            self.play_button.draw_button()

        '''
        调用了pygame.display.flip() ，命令Pygame让最近绘制的屏幕可见。在这里，它在每次执行while 循环时都绘制一个空屏
        幕，并擦去旧屏幕，使得只有新屏幕可见。我们移动游戏元素时，pygame.display.flip() 将不断更新屏幕，以显示元素的新
        位置，并且在原来的位置隐藏元素，从而营造平滑移动的效果
        '''
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
