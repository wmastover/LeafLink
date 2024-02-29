import pygame
from PlayAudio import play_audio
import threading

def happy():
    # Initialize Pygame
    pygame.init()

    # Set the display to windowed mode and title
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Happy State Display')

    # Set the background color
    background_color = (109, 71, 7)  # RGB for dark brown
    screen.fill(background_color)

    # Load and display the happy image
    happy_image_path = "Visuals/Happy.png"
    image = pygame.image.load(happy_image_path)
    image = pygame.transform.scale(image, (image.get_width() // 4, image.get_height() // 4))
    image_rect = image.get_rect(center=(400, 300))
    screen.blit(image, image_rect)

    # Update the display
    pygame.display.update()

    # Play the audio
    audio_path = "./Audio/thankYou.mp3"
    threading.Thread(target=play_audio, args=(audio_path,)).start()

    # Main loop to keep the window open
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update the display
        pygame.display.update()
        # Limit the frame rate to 30 FPS
        pygame.time.Clock().tick(30)

    # Quit Pygame
    pygame.quit()

display_happy_state_and_play_audio()
