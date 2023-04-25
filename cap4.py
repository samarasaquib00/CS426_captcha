import pygame
import pygame.mixer

pygame.init()

# Set up the window and the buttons
window = pygame.display.set_mode((600, 600))
play_button_img = pygame.image.load('play.png')
new_size = (50,50)
play_button_img = pygame.transform.scale(play_button_img, new_size)
play_button_rect = play_button_img.get_rect()
play_button_rect.center = (200, 150)
play_button_rect.size = new_size

quit_button_font = pygame.font.SysFont('arial', 40)
quit_button_text = quit_button_font.render('Quit', True, (0, 0, 0))
quit_button_rect = quit_button_text.get_rect()
quit_button_rect.center = (200, 75)

color = (255,255,255) 
# Changing surface color
window.fill(color)
pygame.display.flip()

# Load the audio files
pygame.mixer.init()
audio_left = pygame.mixer.Sound('voicefiles/left.mp3')
audio_right = pygame.mixer.Sound('voicefiles/right.mp3')
audio_up = pygame.mixer.Sound('voicefiles/up.mp3')
audio_down = pygame.mixer.Sound('voicefiles/down.mp3')

audio_list = [audio_left, audio_right, audio_up]

button_clicked = False
played1 = False
played2 = False
played3 = False
counter = 0
check_img = pygame.image.load('check.png')
x_img = pygame.image.load('x.png')
gamedone = False

# Draw the buttons on the screen
window.blit(play_button_img, play_button_rect)
window.blit(quit_button_text, quit_button_rect)
while gamedone == False:
    for event in pygame.event.get():
        audio_list[0].stop()
        audio_list[1].stop()
        audio_list[2].stop()

        # Check if the mouse button is pressed and if it is over the play button
        if event.type == pygame.MOUSEBUTTONDOWN and play_button_rect.collidepoint(event.pos):
            button_clicked = True

        if button_clicked and played1 == False:
            audio_list[0].play()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    counter = counter + 1
                    played1 = True

        if played1 == True and played2 == False:
            audio_list[0].stop()
            audio_list[1].play()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    counter = counter + 1
                    played2 = True

        if played2 == True and played3 == False:
            audio_list[1].stop()
            audio_list[2].play()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    counter = counter + 1
                    played3 = True

        # Check if the mouse button is pressed and if it is over the quit button
        if event.type == pygame.MOUSEBUTTONDOWN and quit_button_rect.collidepoint(event.pos):
            pygame.quit()
            quit()

        if played3 == True:
            audio_list[2].stop()
            if counter == 3:
                window.blit(check_img, (350, 200))
                
            else:
                window.blit(x_img, (350, 200))
            
            gamedone = True

    pygame.display.update()


