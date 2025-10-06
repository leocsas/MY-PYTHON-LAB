# Faça um programa em python que abra e reproduza o áudio de um arquivo MP3.

import pygame

pygame.mixer.init()
pygame.mixer.music.load('C:/Users/leona/Documents/CursoEmVideo/testes/aula08/Dreaming.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy(): # O get_busy() retorna True enquanto a música ainda está tocando
    continue