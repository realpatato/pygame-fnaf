''' IMPORTS '''
import pygame

#initialize the audio module
pygame.mixer.init()

class camButton:
    def __init__(self, x, y, name, selected = False):
        #used only for drawing the button
        self.draw_rect = pygame.Rect(x, y, 60, 40)
        #used for click detection since the buttons are drawn, then moved
        self.click_box = pygame.Rect(x + 860, y + 320, 60, 40)
        self.selected = selected
        #used for making the button flash when selected
        self.flash = False
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
        return self.sprites[int(self.selected) - int(self.flash)]

    def draw_self(self, surface):
        ''' Draws the sprite to the surface '''
        surface.blit(self.get_cur_sprite(), (self.draw_rect.x, self.draw_rect.y))

class CamMap:
    def __init__(self):
        ''' Handles the cam map and holds the buttons '''
        self.buttons = self.gen_buttons()
        self.map_sprite = self.gen_cur_sprite()
        self.button_flash_timer = 0
    
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
                #stores whatever button is currently true, which will always default to 1A
                self.cur_true_button = buttons[info[2]]
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
        for button in self.buttons.values():
            button.draw_self(sprite)
        #return the condition of the cam system sprite
        return sprite

    def button_flash(self):
        ''' Handles the button flashing '''
        #add to the timer
        self.button_flash_timer += 1
        #if it has been one second, do the thing
        if self.button_flash_timer == 40:
            #swap the flash
            self.cur_true_button.flash = not self.cur_true_button.flash
            #update the image
            self.map_sprite = self.gen_cur_sprite()
            #reset the timer
            self.button_flash_timer = 0

    def draw_self(self, surface, x, y):
        ''' Draws the map object at given x and y '''
        surface.blit(self.map_sprite, (x, y))

class Manager:
    def __init__(self):
        ''' Simply manages cam functions, connecting the pieces, and handles drawing the current camera frame '''
        self.cam_map = CamMap()
        self.audios = self.get_audios()

    def get_audios(self):
        ''' Returns all audios and stores them in a dictionary '''
        return {
            "cam_switch" : pygame.mixer.Sound("sfx/switch.wav")
        }
    
    def check_for_button_click(self, mx, my):
        ''' Checks for a button click based on given x and y coordinates'''
        #iterate over the buttons
        for button in self.cam_map.buttons.values():
            #check if the mouse is within the button area
            if (mx > button.click_box.x) and (mx < button.click_box.right) and (my > button.click_box.y) and (my < button.click_box.bottom):
                #play the cam switch sound effect (happens anytime you click the camera)
                pygame.mixer.Sound.play(self.audios["cam_switch"])
                #check if already selected
                if (not button.selected):
                    #set it to be selected
                    button.selected = True
                    #set the currently selected button to false
                    self.cam_map.cur_true_button.selected = False
                    #reset the flash on the old cam button
                    self.cam_map.cur_true_button.flash = False
                    #reset the flash timer
                    self.cam_map.button_flash_timer = 0
                    #update the map sprite
                    self.cam_map.map_sprite = self.cam_map.gen_cur_sprite()
                    #set it to be the current true button
                    self.cam_map.cur_true_button = button
    
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