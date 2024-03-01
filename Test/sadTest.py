import pygame
from PlayAudio import play_audio
import threading

def sad():
    # Initialize Pygame
    pygame.init()

    # Set the display to windowed mode and title
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Sad State Display')  # Corrected the title to match the sad state

    # Set the background color
    background_color = (255, 222, 89)  # RGB for a light brown color
    screen.fill(background_color)

    # Load and display the sad image
    sad_image_path = "Visuals/Sad.png"
    image = pygame.image.load(sad_image_path)
    image = pygame.transform.scale(image, (image.get_width() // 4, image.get_height() // 4))
    image_rect = image.get_rect(center=(400, 300))
    screen.blit(image, image_rect)

    # Update the display
    pygame.display.flip()

    # Play the audio
    audio_path = "./Audio/thirsty.mp3"
    threading.Thread(target=play_audio, args=(audio_path,)).start()
    # Main loop to keep the window open for 5 seconds
    start_time = pygame.time.get_ticks()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if pygame.time.get_ticks() - start_time > 5000:  # 5000 milliseconds = 5 seconds
            running = False
        pygame.time.Clock().tick(30)  # Limit the frame rate to 30 FPS
    
    # Quit Pygame
    pygame.quit()