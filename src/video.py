#Basic Code for the video
import pygame
import moviepy.editor

pygame.init()
video = moviepy.editor.VideoFileClip(r'C:\Users\ekemi\Programming\Projects\Python\Media Player\Media-player\src\est_vid.mp4')
video.preview()
pygame.quit() 