from time import sleep
import pygame, sys
import time
import pygame
import cv2
import numpy as np
import os.path
import sys
from texty import *
import win32api
from win32api import GetSystemMetrics
import random
Width = GetSystemMetrics(0);Height = GetSystemMetrics(1)
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
def get_font(size):
    return pygame.font.Font("asety/fontus.ttf", size)
def smrdis():
    if os.path.exists("save1.txt"):os.remove("save1.txt")
    if os.path.exists("save2.txt"):os.remove("save2.txt")
    if os.path.exists("save3.txt"):os.remove("save3.txt")
    if os.path.exists("save4.txt"):os.remove("save4.txt")
    if os.path.exists("save5.txt"):os.remove("save5.txt")
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

AVARAGE TOHOVNO

promeny:
texbox=resized_mdva #budevkazdym    to podtim ne
hohnapr=PLAY_MOUSE_POS=pygame.mouse.get_pos();PLAY_BACK;MOKNO_BUTTONN;DALSI_BUTTON;DOKNO_BUTTON=Button(image=(textbox),pos=((Width/100)*40.625,(Height/100)*46.296),text_input="",font=font_meno, base_color="White", hovering_color="Green")
imp1 = pygame.image.load(postava1).convert_alpha();SCREEN.blit(imp1,((Width/100)*52.083,(Height/100)*15.740))  
postava1=('postavy/strom.png') #budevkazdym
#postava2=('postavy/strom.png')#budevkazdym
lajna=(d69) #budevkazdym
hohnapo=DALSI_BUTTON.update(SCREEN);PLAY_BACK.changeColor(PLAY_MOUSE_POS);PLAY_BACK.update(SCREEN);DOKNO_BUTTON.update(SCREEN);MOKNO_BUTTONS.update(SCREEN);dia1=font.render(lajna,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
imp2 = pygame.image.load(postava2).convert();SCREEN.blit(imp2,((Width/100)*5.2083,(Height/100)*18.518)) 



def s222():
        while True:
            SCREEN.blit(resized_bg1, (0, 0));PLAY_MOUSE_POS = pygame.mouse.get_pos();PLAY_BACK;MOKNO_BUTTONN;DALSI_BUTTON
            DOKNO_BUTTON= Button(image=(resized_mdva), pos=((Width/100)*40.625,(Height/100)*46.296),text_input="", font=font_meno, base_color="White", hovering_color="Green")
            imp3 = pygame.image.load('postavy/strom.png').convert_alpha()                                                           
            SCREEN.blit(imp3, ((Width/100)*52.083, (Height/100)*15.740))
            imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           
            SCREEN.blit(imp2, ((Width/100)*5.2083,(Height/100)*18.518))  
            DALSI_BUTTON.update(SCREEN);PLAY_BACK.changeColor(PLAY_MOUSE_POS);PLAY_BACK.update(SCREEN);DOKNO_BUTTON.update(SCREEN);MOKNO_BUTTONS.update(SCREEN)
            dia1 = font.render(d222,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
            for event in pygame.event.get():
                if event.type==pygame.QUIT:pygame.quit();sys.exit()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):POMOC()
                    if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):s223()
            pygame.display.update()







def sŘŘŘ():
        while True:
            SCREEN.blit(ŘŘŘ, (0, 0))
            PLAY_MOUSE_POS=pygame.mouse.get_pos();PLAY_BACK;MOKNO_BUTTONN;DALSI_BUTTON
            DOKNO_BUTTON=Button(image=(resized_mdva),pos=((Width/100)*40.625,(Height/100)*46.296),text_input="",font=font_meno,base_color="White",hovering_color="Green")
            imp3=pygame.image.load('postavy/strom.png').convert_alpha()   řřř                                                        
            SCREEN.blit(imp3, ((Width/100)*52.083, (Height/100)*18.518))
            imp2=pygame.image.load('postavy/cednik.png').convert()      řřř                                                     
            SCREEN.blit(imp2, ((Width/100)*5.2083,(Height/100)*15.740))  
            DALSI_BUTTON.update(SCREEN);PLAY_BACK.changeColor(PLAY_MOUSE_POS);PLAY_BACK.update(SCREEN);DOKNO_BUTTON.update(SCREEN);MOKNO_BUTTONC.update(SCREEN)
            dia1=font.render(d223,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148)) řřř
            for event in pygame.event.get():
                if event.type==pygame.QUIT:pygame.quit();sys.exit()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):POMOC()
                    if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):s224() řřř
            pygame.display.update()
"""                                                            
xpb=Width/100;xsb=Height*100;ypb=Height/100;yob=Height/100;yqb=Height/100;ysb=Height/100;ypob=Height/100
PLAY_BUTTON = Button(image=pygame.image.load("asety/startus.png"), pos=(xpb*91.18, ypb*27.8), text_input="Nová hra", font=font_vyber, base_color="#732c06", hovering_color="White")
OPTIONS_BUTTON = Button(image=pygame.image.load("asety/nastus.png"), pos=(xpb*91.18, yob*64.82), text_input="Nastavení", font=font_vyber, base_color="#732c06", hovering_color="White")
QUIT_BUTTON = Button(image=pygame.image.load("asety/koncus.png"), pos=(xpb*91.18, yqb*83.34 ), text_input="Konec", font=font_vyber, base_color="#732c06", hovering_color="White")
POK_BUTTON = Button(image=pygame.image.load("asety/pokus.png"), pos=(xpb*91.18, ypob*46.3), text_input="Pokračovat", font=font_vyber, base_color="#732c06", hovering_color="White")
DALSI_BUTTON = Button(image=pygame.image.load("asety/dalsi.png"), pos=((Width/100)*50, (Height/100)*50), text_input="", font=font_meno, base_color="White", hovering_color="White")
