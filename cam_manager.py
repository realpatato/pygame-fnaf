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
        directory = "cam_assets/button_assets/"
        #get the foreground of the button
        button_fg = pygame.image.load(directory + "button_fgs/" + name + ".png")
        #remove yucky background from the image
        button_fg.set_colorkey((90, 90, 90))
        #do this twice
        for i in range(2):
            #get the background of the button
            button_bg = pygame.image.load(directory + "button_bgs/selected" + str(bool(i)) + ".png")
            #create an empty surface fdor drawing the sprite
            sprite = pygame.Surface((60, 40))
            #draw the background
            sprite.blit(button_bg, (0, 0))
            #draw the foreground
            sprite.blit(button_fg, (8, 7))
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

class CamMap:
    def __init__(self):
        ''' Handles the cam map and holds the buttons '''
        self.buttons = self.gen_buttons()
        self.map_sprite = self.gen_cur_sprite()
    
    def gen_buttons(self):
        ''' Creates all buttons when game starts '''
        #stores the info for the buttons
        button_info = [
            [126, 21, "1A"],
            [106, 76, "1B"],
            [74, 154, "1C"],
            [126, 270, "2A"],
            [126, 310, "2B"],
            [42, 252, "3"],
            [232, 271, "4A"],
            [232, 311, "4B"],
            [0, 103, "5"],
            [329, 235, "6"],
            [338, 104, "7"]
        ]
        #empty dictionary to store buttons
        buttons = {}
        #iterate over the button info
        for info in button_info:
            #store a button with certain values
            buttons[info[2]] = camButton(info[0], info[1], info[2])
            #set 1A to selected, its the default
            if info[2] == "1A":
                buttons[info[2]].selected = True
        #return the dictionary
        return buttons

    def gen_cur_sprite(self):
        ''' Generates the sprite at the current moment '''
        #start with an empty surface, takes up the whole screen since the actual cam is drawn here too
        sprite = pygame.Surface((420, 400))
        #get the map image
        map_sprite = pygame.image.load("cam_assets/map.png")
        #draw the map on the surface
        sprite.blit(map_sprite, (20, 0))
        #draw the buttons
        for button_key in self.buttons:
            self.buttons[button_key].draw_self(sprite)
        #return the condition of the cam system sprite
        return sprite

    def draw_self(self, surface, x, y):
        ''' Draws the map object at given x and y '''
        surface.blit(self.map_sprite, (x, y))

class Manager:
    def __init__(self):
        ''' Simply manages cam functions, connecting the pieces, and handles drawing the current camera frame '''
        self.cam_map = CamMap()
    
    def gen_cur_sprite(self):
        ''' Generates the current sprite '''
        #takes up the whole screen, so we make a surface that size
        sprite = pygame.Surface((1280, 720))
        #draw the map to the surface
        self.cam_map.draw_self(sprite, 860, 320)
        #return the sprite
        return sprite

    def draw_self(self, surface):
        ''' Draws the sprite to the surface '''
        surface.blit(self.gen_cur_sprite(), (0, 0))