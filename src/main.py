import pygame

FPS = 60
pygame.init()
clock = pygame.time.Clock()
movie = pygame.movie.Movie('vid.mp4')
screen = pygame.display.set_mode(movie.get_size())
movie_screen = pygame.Surface(movie.get_size()).convert()

movie.set_display(movie_screen)
movie.play()

playing = True
while playing:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         movie.stop()
         playing = False

   screen.blit(movie_screen,(0,0))
   pygame.display.update()
   clock.tick(FPS)
pygame.quit()
"""

from pygame import display,movie

pygame.init()

screen = pygame.display.set_mode((1024, 768))
background = pygame.Surface((1024, 768))

screen.blit(background, (0, 0))
pygame.display.update()

movie = pygame.movie.Movie('vid.mp4') 
mrect = pygame.Rect(0,0,140,113)
movie.set_display(screen, mrect.move(65, 150))
movie.set_volume(0)
movie.play()


import pygame
import moviepy.editor

pygame.init()
video = moviepy.editor.VideoFileClip("video.mp4")
video.preview()
pygame.quit()
"""