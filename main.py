''' IMPORTS '''
import pygame
import cam_manager

man = cam_manager.Manager()

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
            mouse_pos = event.pos
            man.check_for_button_click(mouse_pos[0], mouse_pos[1])
    
    #intial screen wipe
    screen.fill((0, 0, 0))

    man.draw_self(screen)

    #update the display
    pygame.display.update()
    
    #tick the clock
    clock.tick(60)

''' ENDING IT ALL :D '''
#quit the window
pygame.quit()
#end the program
quit()