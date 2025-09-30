''' IMPORTS '''
import pygame
import cam_manager as cm

cam_man = cm.Manager()

''' PYGAME SETUP '''
#initialize the pygame module
pygame.init()

#define width and height for the screen
screen_width = 1280
screen_height = 720
#create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
#set caption for the window
pygame.display.set_caption("FNAF")

''' PRE LOOP STUFF '''
#clock for controlling frame rate
clock = pygame.time.Clock()
#variable to control the game loop
keep_playing = True
#varible for knowing if in cams or not
in_cams = True

''' LOOP '''
while keep_playing:
    #iterate over all pygame events
    for event in pygame.event.get():
        #check for a quit
        if event.type == pygame.QUIT:
            #end the loop
            keep_playing = False
        #check for click
        if event.type == pygame.MOUSEBUTTONDOWN:
            #check it is the lmb
            if event.button == 1:
                mouse_pos = event.pos
                if in_cams:
                    cam_man.check_for_button_click(mouse_pos[0], mouse_pos[1])

    ''' THINGS HAPPENING REGARDLESS OF IF IN CAMS OR NOT '''
    #do the flash thing
    cam_man.cam_map.button_flash()
    
    #intial screen wipe
    screen.fill((0, 0, 0))

    ''' IF IN CAMS '''
    if in_cams:
        #draws the state of cams
        cam_man.draw_self(screen)

    #update the display
    pygame.display.update()
    
    #tick the clock
    clock.tick(60)

''' ENDING IT ALL :D '''
#quit the window
pygame.quit()
#end the program
quit()