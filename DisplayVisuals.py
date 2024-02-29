import pygame
import os
from PlayAudio import play_audio

# Initialize Pygame
pygame.init()

# Global variables for UI state
screen = None
background_color = (109, 71, 7)  # RGB for dark brown, converted from #6D4707
happy_image_path = "Visuals/Happy.png"
sad_image_path = "Visuals/Sad.png"
mid_image_path = "Visuals/Mid.png"  # Path for the mid state image
current_image_path = happy_image_path
background_colors = {
    "happy": (109, 71, 7),  # Dark brown
    "mid": (178, 123, 32),  # Mid state color, converted from #B27B20
    "sad": (255, 222, 89)   # Sandy yellow
}
state_order = ["happy", "mid", "sad"]
current_state_index = 0

def init_ui():
    global screen, background_color, current_image_path

    # Set the display to windowed mode and title
    screen = pygame.display.set_mode((800, 600))  # Set to desired window size
    pygame.display.set_caption('Mood Display')

    # Set the initial background color and image
    screen.fill(background_color)
    display_image(current_image_path)

    # Update the display
    pygame.display.update()

def display_image(image_path):
    global screen
    image = pygame.image.load(image_path)
    # Scale the image to 1/4 the size
    image = pygame.transform.scale(image, (image.get_width() // 4, image.get_height() // 4))
    image_rect = image.get_rect(center=(400, 300))  # Center the image
    screen.blit(image, image_rect)

def toggle_background_and_image():
    global screen, background_color, current_image_path, happy_image_path, sad_image_path, mid_image_path, current_state_index, state_order, background_colors

    # Move to the next state
    current_state_index = (current_state_index + 1) % len(state_order)
    current_state = state_order[current_state_index]

    # Set the background color and image based on the current state
    background_color = background_colors[current_state]
    if current_state == "happy":
        current_image_path = happy_image_path
        audio_path = "./Audio/thankYou.mp3"
    elif current_state == "mid":
        current_image_path = mid_image_path
        audio_path = "./Audio/thirsty.mp3"  # Placeholder for mid state audio
    else:
        current_image_path = sad_image_path
        audio_path = "./Audio/CouldIGetSomeWaterPlease.mp3"

    # Update the display and play the corresponding audio
    screen.fill(background_color)
    display_image(current_image_path)
    pygame.display.update()
    import threading
    threading.Thread(target=play_audio, args=(audio_path,)).start()

def main():
    init_ui()
    running = True
    sensor_check_event = pygame.USEREVENT + 1
    pygame.time.set_timer(sensor_check_event, 15000)  # Check sensor every 15,000 milliseconds (15 seconds)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    toggle_background_and_image()
            elif event.type == sensor_check_event:
                # Custom event for checking the sensor
                # Placeholder for sensor checking logic
                pass

        pygame.time.Clock().tick(30)  # Limit the frame rate to 30 FPS

    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()
