import pygame
import time

pygame.mixer.init()

def play_audio(file_path):
    """
    Play an MP3 file over the default speakers on a Raspberry Pi.
    :param file_path: The path to the MP3 file to be played.
    """
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    
    # Wait for the music to play without using event loop
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

# This function call should be outside the selection and managed by the main program logic
# play_audio("./CouldIGetSomeWaterPlease.mp3")
