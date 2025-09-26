''' IMPORTS '''
import pygame

class camButton:
    def __init__(self, x, y, name, selected = False):
        self.rect = pygame.Rect(x, y, 60, 40)
        self.selected = selected
        self.sprites = self.gen_sprites(name)
        
    def gen_sprites(self, name):
        ''' Generates the selected and non-selected variations of the button '''
        #create an empty list to store sprites
        sprites = []
        #each button part will pull from this directory
        directory = "cams_assets/button_assets/"
        #do this twice
        for i in range(2):
            #get the background of the button
            button_bg = pygame.image.load(directory + "button_bgs/selected" + str(bool(i)) + ".png")
            #create an empty surface fdor drawing the sprite
            sprite = pygame.Surface((60, 40))
            #draw the background
            sprite.blit(button_bg, (0, 0))
            #add the sprite to the list
            sprites.append(sprite)
        #return that list
        return sprites
    
    def get_cur_sprite(self):
        ''' Returns the current sprite '''
        #gets the sprite by converting the bool into an int, (False = 0 True = 1)
        return self.sprites[int(self.selected)]

    def draw_self(self, surface):
        ''' Draws the sprite to the surface '''
        surface.blit(self.get_cur_sprite(), (self.rect.x, self.rect.y))