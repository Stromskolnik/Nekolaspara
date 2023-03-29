from time import sleep
import pygame, sys
import time
import pygame
import cv2
import numpy as np
import os.path
import sys
from texty import *
import random
from sys import platform
Width = 0
Height = 0
if platform == "linux" or platform == "linux2":
    import Xlib.display # pip install python-xlib
    display = Xlib.display.Display()
    screen = display.screen()
    Width = screen.width_in_pixels
    Height = screen.height_in_pixels
elif platform == "win32":
    import win32api
    from win32api import GetSystemMetrics
    Width = GetSystemMetrics(0)
    Height = GetSystemMetrics(1)
os.chdir(os.path.dirname(os.path.abspath(__file__)));pygame.init()
SCREEN = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Nekolaspara")
bg1 = pygame.image.load("pozadi/s1.png")
resized_bg1= pygame.transform.scale(bg1,(Width,Height))
dokno=pygame.image.load("asety/mdva.png")
resized_mdva= pygame.transform.scale(dokno,((Width/100)*100,(Height/100)*100))
font =  pygame.font.Font("asety/fontus.ttf", (Height//100)*3)
font_meno =pygame.font.Font("asety/fontus.ttf", (Height//100)*(277//100))
font_vyber=pygame.font.Font("asety/fontus.ttf", (Height//100)*(4629//1000))
BG = pygame.image.load("asety/m.png")
resized_BG= pygame.transform.scale(BG,(Width,Height))

class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
	def update(self, screen):
		if self.image is not None:screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)
	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):return True
		return False
	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:self.text = self.font.render(self.text_input, True, self.base_color)
xpb=Width/100;xsb=Height*100;ypb=Height/100;yob=Height/100;yqb=Height/100;ysb=Height/100;ypob=Height/100
PLAY_BUTTON = Button(image=pygame.image.load("asety/startus.png"), pos=(xpb*91.18, ypb*27.8), text_input="Nová hra", font=font_vyber, base_color="#732c06", hovering_color="White")
OPTIONS_BUTTON = Button(image=pygame.image.load("asety/nastus.png"), pos=(xpb*91.18, yob*64.82), text_input="Nastavení", font=font_vyber, base_color="#732c06", hovering_color="White")
QUIT_BUTTON = Button(image=pygame.image.load("asety/koncus.png"), pos=(xpb*91.18, yqb*83.34 ), text_input="Konec", font=font_vyber, base_color="#732c06", hovering_color="White")
POK_BUTTON = Button(image=pygame.image.load("asety/pokus.png"), pos=(xpb*91.18, ypob*46.3), text_input="Pokračovat", font=font_vyber, base_color="#732c06", hovering_color="White")
DALSI_BUTTON = Button(image=pygame.image.load("asety/dalsi.png"), pos=((Width/100)*50, (Height/100)*50), text_input="", font=font_meno, base_color="White", hovering_color="White")
def get_font(size):
    return pygame.font.Font("asety/fontus.ttf", size)
def smrdis():
    pygame.mixer.music.stop()
    pygame.mixer.music.load("songus/dg.mp3")
    pygame.mixer.music.play(loops=-1)
    while True:
        SCREEN.fill("black")
        SCREEN.blit(pygame.image.load("asety/ono.png"), (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:exit()                                                                                  
        pygame.display.update()


""" PTSD EFEKT
def s113():
    pygame.mixer.music.stop()
    pygame.mixer.music.load("songus/prenescasu.wav")
    pygame.mixer.music.play(loops=0)
    while True:
        pygame.mouse.get_pos()
        SCREEN.fill("black");SCREEN.blit(pygame.image.load("pozadi/pd1.png"), (0, 0))
        pygame.display.update() 
        SCREEN.fill("black");SCREEN.blit(pygame.image.load("pozadi/pd2.png"), (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:s114()                                                                                  
        pygame.display.update() 

"""                                                            

