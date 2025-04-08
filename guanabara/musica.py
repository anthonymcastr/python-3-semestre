import pygame

pygame.init()
pygame.mixer.music.load('musica123.mp3')
pygame.mixer.music.play()
pygame.event.wait()

print("A música está tocando. Pressione Enter para finalizar.")
input()
pygame.mixer.music.stop()