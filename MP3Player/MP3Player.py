import pygame

pygame.init()
pygame.mixer.music.load('/home/pi/python-tutorial/MP3Player/music/music.mp3')
pygame.mixer.music.play()
pygame.event.wait()