from game import Game
import config as c
from player import Player
import pygame
from static import Static
from pygame.rect import Rect

class Play(Game):
    def __init__(self):
        Game.__init__(self, 'Play', c.screen_width, c.screen_height, c.background_image, c.frame_rate)
        #self.is_game_running = False
        self.create_objects()
        #self.player = None

    def create_objects(self):
        self.create_static()
        self.create_player()
        
        print("objects created")
    
    def create_static(self):
        self.stolb = Static(100, 100, 50, 70, (0, 20, 250))
        self.objects.append(self.stolb)

    def create_player(self):
        player = Player(c.palayer_x, c.palayer_y, c.palayer_width, c.palayer_height, (255, 10, 10), c.palayer_speed)
        
        self.keydown_handlers[pygame.K_LEFT].append(player.handle)
        self.keydown_handlers[pygame.K_RIGHT].append(player.handle)
        self.keydown_handlers[pygame.K_UP].append(player.handle)
        self.keydown_handlers[pygame.K_DOWN].append(player.handle)
        self.keyup_handlers[pygame.K_LEFT].append(player.handle)
        self.keyup_handlers[pygame.K_RIGHT].append(player.handle)
        self.keyup_handlers[pygame.K_UP].append(player.handle)
        self.keyup_handlers[pygame.K_DOWN].append(player.handle)
    
        self.player = player
        self.objects.append(self.player)

    def intersect(self, obj, s_obj):
            edges = dict(left=Rect(obj.left-3, obj.top, 1, obj.height),
                         right=Rect(obj.right+3, obj.top, 1, obj.height),
                         top=Rect(obj.left, obj.top-3, obj.width, 1),
                         bottom=Rect(obj.left, obj.bottom+3, obj.width, 1))
            collisions = set(edge for edge, rect in edges.items() if s_obj.bounds.colliderect(rect))
            ######
            #print(collisions)
            if not collisions:
                return None

            if len(collisions) == 1:
                return list(collisions)[0]

            
            # if 'top' in collisions:
            #     if s_obj.bottom > obj.centerx:
            #         return 'left'
            #     if s_obj.bottom > obj.top:
            #         return 'top'
            #     else:
            #         return 'right'

            # if 'bottom' in collisions:
            #     if s_obj.top <= obj.bottom:
            #         return 'bottom'
            #     if s_obj.left < obj.left:
            #         return 'left'
            #     else:
            #         return 'right'
    

    def stop_run(self, course):
        print(course)
        if course == 'top':
            self.player.move(0, self.player.offset)
        if course == 'bottom':
            self.player.move(0, -self.player.offset)
        if course == 'right':
            self.player.move(-self.player.offset, 0)
        if course == 'left':
            self.player.move(self.player.offset, 0)

    def update(self):
        self.stop_run(self.intersect(self.player, self.stolb))
        super().update()


def main():
    Play().run()
   

if __name__ == '__main__':
    main()