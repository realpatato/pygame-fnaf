''' IMPORTS '''
import pygame
from random import randint

class Static:
    def __init__(self, transparency):
        self.sprites = self.get_sprites(transparency)
        self.sprite_index = 0

    def get_sprites(self, transparency):
        ''' Creates a list of static sprites '''
        #create empty list to store the sprites
        sprites = []
        #runs 8 times, since there is 8 files
        for i in range(8):
            #loads one of the images
            sprite = pygame.image.load("static/static" + str(i + 1) + ".png")
            #sets the alpha to make the image slightly transparent
            sprite.set_alpha(round(transparency / 100 * 255))
            #adds the sprite to the list
            sprites.append(sprite)
        #returns the list of sprites
        return sprites
    
    def get_cur_sprite(self):
        #random number that will be the amount to advance in the sprite list
        frame_advance = randint(1, 3)
        #loop so that we don't go out of range
        for i in range(frame_advance):
            #add to the index
            self.sprite_index += 1
            #if we're out of range
            if self.sprite_index == 8:
                #set it to 0
                self.sprite_index = 0
        #return the random sprite
        return self.sprites[self.sprite_index]

    def draw_self(self, surface):
        ''' Draws the static to the surface '''
        surface.blit(self.get_cur_sprite(), (0, 0))