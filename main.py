''' IMPORTS '''
import pygame
import cam_buttons

#buttons - temp just cause i wanna get the positioning out of the way
#currently positioned in reference to the sprite for the cam system, hence some being off screen
button1A = cam_buttons.camButton(106, 21, "1A")
button1B = cam_buttons.camButton(86, 76, "1B")
button1C = cam_buttons.camButton(54, 154, "1C")
button2A = cam_buttons.camButton(106, 270, "2A")
button2B = cam_buttons.camButton(106, 310, "2B", True)
button3 = cam_buttons.camButton(22, 252, "3")
button4A = cam_buttons.camButton(212, 271, "4A")
button4B = cam_buttons.camButton(212, 311, "4B")
button5 = cam_buttons.camButton(-20, 103, "5")
button6 = cam_buttons.camButton(309, 235, "6")
button7 = cam_buttons.camButton(318, 104, "7")

#map also temp until further camera development
map_sprite = pygame.image.load("map.png")

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
    
    #intial screen wipe
    screen.fill((0, 0, 0))

    #map drawing (temp for testing positioning of buttons)
    screen.blit(map_sprite, (0, 0))

    #button drawing (temp for testing positioning)
    button1A.draw_self(screen)
    button1B.draw_self(screen)
    button1C.draw_self(screen)
    button2A.draw_self(screen)
    button2B.draw_self(screen)
    button3.draw_self(screen)
    button4A.draw_self(screen)
    button4B.draw_self(screen)
    button5.draw_self(screen)
    button6.draw_self(screen)
    button7.draw_self(screen)

    #update the display
    pygame.display.update()
    
    #tick the clock
    clock.tick(60)

''' ENDING IT ALL :D '''
#quit the window
pygame.quit()
#end the program
quit()