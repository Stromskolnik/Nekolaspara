from time import sleep
import pygame, sys
import time
import pygame
import cv2
import numpy as np
import os.path
import sys
from texty import *
pygame.init()
SCREEN = pygame.display.set_mode((1920, 1080))
#nastavení hudby
def hh():
    pygame.mixer.music.set_volume(1)
def nh():
    pygame.mixer.music.set_volume(0)
pygame.display.set_caption("Nekolaspara")
#POZADÍ
BG = pygame.image.load("asety/m.png")
bg1 = pygame.image.load("pozadi/s1.png")
bg2 =pygame.image.load("pozadi/s2.png")
bg3 =pygame.image.load("pozadi/krab1.png")
bg4 =pygame.image.load("pozadi/krab2.png")
bg5 =pygame.image.load("pozadi/varnavecer.png")
bg6 =pygame.image.load("pozadi/vecer.png")
bg7 =pygame.image.load("pozadi/namesti.png")
bg8=pygame.image.load("pozadi/office.png")
ls1=pygame.image.load("asety/ls1.png")
#Hudba

#animace textu 
def animacefunkcni():
    font =  pygame.font.Font("asety/fontus.ttf", 40)
    timer=pygame.time.Clock()
    messages = ["novej test ", "Krok jedna v krvi je želozo krok dva jeď do Kadaně krok tři:"]
    active_message = 0
    message = messages[active_message]
    snip= font.render("",True,"Black")
    counter= 0 
    speed =3
    run = True
    done =False
    while run:
        timer.tick(30)
        if counter <speed * len(message):
            counter +=1
        elif counter >= speed*len(message):
            done ==True
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and done and active_message< len(messages):
                    active_message +=1
                    done ==False
                    message = messages[active_message]
                    counter=0



        snip = font.render(message[0:counter//speed],True,"White")
        SCREEN.blit(snip,(300,790))
        pygame.display.flip()
#fotni
font =  pygame.font.Font("asety/fontus.ttf", 32)
def t1():
    dia1 = font.render(d1,True,"Black") ;SCREEN.blit(dia1,(275,790))    
def t2():
    dia1 = font.render(d2,True,"Black");SCREEN.blit(dia1,(275,790))   
def t3():
    dia1 = font.render(d3,True,"Black");SCREEN.blit(dia1,(275,790))   
def t4():
    dia1 = font.render(d4,True,"Black");SCREEN.blit(dia1,(275,790))   
def t5():
    dia1 = font.render(d5,True,"Black");SCREEN.blit(dia1,(275,790))   
def t6():
    dia1 = font.render(d6,True,"Black");SCREEN.blit(dia1,(275,790))   
def t7():
    dia1 = font.render(d7,True,"Black");SCREEN.blit(dia1,(275,790))   
def t8():
    dia1 = font.render(d8,True,"Black");SCREEN.blit(dia1,(275,790))   
def t9():
    dia1 = font.render(d9,True,"Black");SCREEN.blit(dia1,(275,790))   
def t10():
    dia1 = font.render(d10,True,"Black");SCREEN.blit(dia1,(275,790))    
def t11():
    dia1 = font.render(d11,True,"Black");SCREEN.blit(dia1,(275,790))    
def t12():
    dia1 = font.render(d12,True,"Black");SCREEN.blit(dia1,(275,790))    
def t13():
    dia1 = font.render(d13,True,"Black");SCREEN.blit(dia1,(275,790))    
def t14():
    dia1 = font.render(d14,True,"Black");SCREEN.blit(dia1,(275,790))    
def t15():
    dia1 = font.render(d15,True,"Black");SCREEN.blit(dia1,(275,790))    
def t16():
    dia1 = font.render(d16,True,"Black");SCREEN.blit(dia1,(275,790))    
def t17():
    dia1 = font.render(d17,True,"Black");SCREEN.blit(dia1,(275,790))    
def t18():
    dia1 = font.render(d18,True,"Black");SCREEN.blit(dia1,(275,790))    
def t19():
    dia1 = font.render(d19,True,"Black");SCREEN.blit(dia1,(275,790))    
def t20():
    dia1 = font.render(d20,True,"Black");SCREEN.blit(dia1,(275,790))    
def t21():
    dia1 = font.render(d21,True,"Black");SCREEN.blit(dia1,(275,790))    
def t22():
    dia1 = font.render(d22,True,"Black");SCREEN.blit(dia1,(275,790))    
def t23():
    dia1 = font.render(d23,True,"Black");SCREEN.blit(dia1,(275,790))    
def t24():
    dia1 = font.render(d24,True,"Black");SCREEN.blit(dia1,(275,790))    
def t25():
    dia1 = font.render(d25,True,"Black");SCREEN.blit(dia1,(275,790))    
def t26():
    dia1 = font.render(d26,True,"Black");SCREEN.blit(dia1,(275,790))    
def t27():
    dia1 = font.render(d27,True,"Black");SCREEN.blit(dia1,(275,790))    
def t28():
    dia1 = font.render(d28,True,"Black");SCREEN.blit(dia1,(275,790))    
def t29():
    dia1 = font.render(d29,True,"Black");SCREEN.blit(dia1,(275,790))    
def t29b():
    dia2 = font.render(d29b,True,"Black") ;SCREEN.blit(dia2,(275,830))   
def t30():
    dia1 = font.render(d30,True,"Black");SCREEN.blit(dia1,(275,790))    
def t31():
    dia1 = font.render(d31,True,"Black");SCREEN.blit(dia1,(275,790))    
def t31b():
    dia2 = font.render(d31b,True,"Black") ;SCREEN.blit(dia2,(275,830))   
def t32():
    dia1 = font.render(d32,True,"Black");SCREEN.blit(dia1,(275,790))    
def t33():
    dia1 = font.render(d33,True,"Black");SCREEN.blit(dia1,(275,790))    
def t34():
    dia1 = font.render(d34,True,"Black");SCREEN.blit(dia1,(275,790))    
def t35():
    dia1 = font.render(d35,True,"Black");SCREEN.blit(dia1,(275,790))    
def t36():
    dia1 = font.render(d36,True,"Black");SCREEN.blit(dia1,(275,790))    
def t36b():
    dia2 = font.render(d36b,True,"Black") ;SCREEN.blit(dia2,(275,830))  
def t37():
    dia1 = font.render(d37,True,"Black");SCREEN.blit(dia1,(275,790))    
def t38():
    dia1 = font.render(d38,True,"Black");SCREEN.blit(dia1,(275,790))    
def t39():
    dia1 = font.render(d39,True,"Black");SCREEN.blit(dia1,(275,790))    
def t40():
    dia1 = font.render(d40,True,"Black");SCREEN.blit(dia1,(275,790))    
def t41():
    dia1 = font.render(d41,True,"Black");SCREEN.blit(dia1,(275,790))    
def t42():
    dia1 = font.render(d42,True,"Black");SCREEN.blit(dia1,(275,790))    
def t42b():
    dia2 = font.render(d42b,True,"Black") ;SCREEN.blit(dia2,(275,830))     
def t43():
    dia1 = font.render(d43,True,"Black");SCREEN.blit(dia1,(275,790))    
def t44():
    dia1 = font.render(d44,True,"Black");SCREEN.blit(dia1,(275,790))    
def t44b():
    dia2 = font.render(d44b,True,"Black") ;SCREEN.blit(dia2,(275,830))  
def t45():
    dia1 = font.render(d45,True,"Black");SCREEN.blit(dia1,(275,790))    
def t45b():
    dia2 = font.render(d45b,True,"Black") ;SCREEN.blit(dia2,(275,830))  
def t46():
    dia1 = font.render(d46,True,"Black");SCREEN.blit(dia1,(275,790))    
def t47():
    dia1 = font.render(d47,True,"Black");SCREEN.blit(dia1,(275,790))    
def t48():
    dia1 = font.render(d48,True,"Black");SCREEN.blit(dia1,(275,790))    
def t49():
    dia1 = font.render(d49,True,"Black");SCREEN.blit(dia1,(275,790))    
def t49b():
    dia2 = font.render(d49b,True,"Black") ;SCREEN.blit(dia2,(275,830))
def t50():
    dia1 = font.render(d50,True,"Black");SCREEN.blit(dia1,(275,790))    
def t51():
    dia1 = font.render(d51,True,"Black");SCREEN.blit(dia1,(275,790))    
def t52():
    dia1 = font.render(d52,True,"Black");SCREEN.blit(dia1,(275,790))    
def t53():
    dia1 = font.render(d53,True,"Black");SCREEN.blit(dia1,(275,790))    
def t54():
    dia1 = font.render(d54,True,"Black");SCREEN.blit(dia1,(275,790))    
def t54b():
    dia2 = font.render(d54b,True,"Black") ;SCREEN.blit(dia2,(275,830)) 
def t55():
    dia1 = font.render(d55,True,"Black");SCREEN.blit(dia1,(275,790))    
def t56():
    dia1 = font.render(d56,True,"Black");SCREEN.blit(dia1,(275,790))    
def t57():
    dia1 = font.render(d57,True,"Black");SCREEN.blit(dia1,(275,790))    
def t58():
    dia1 = font.render(d58,True,"Black");SCREEN.blit(dia1,(275,790))    
def t59():
    dia1 = font.render(d59,True,"Black");SCREEN.blit(dia1,(275,790))    
def t60():
    dia1 = font.render(d60,True,"Black");SCREEN.blit(dia1,(275,790))    
def t61():
    dia1 = font.render(d61,True,"Black");SCREEN.blit(dia1,(275,790))    
def t62():
    dia1 = font.render(d62,True,"Black");SCREEN.blit(dia1,(275,790))    
def t63():
    dia1 = font.render(d63,True,"Black");SCREEN.blit(dia1,(275,790))    
def t64():
    dia1 = font.render(d64,True,"Black");SCREEN.blit(dia1,(275,790))    
def t65():
    dia1 = font.render(d65,True,"Black");SCREEN.blit(dia1,(275,790))    
def t66():
    dia1 = font.render(d66,True,"Black");SCREEN.blit(dia1,(275,790))    
def t67():
    dia1 = font.render(d67,True,"Black");SCREEN.blit(dia1,(275,790))    
def t68():
    dia1 = font.render(d68,True,"Black");SCREEN.blit(dia1,(275,790))    
def t69():
    dia1 = font.render(d69,True,"Black");SCREEN.blit(dia1,(275,790))    
def t70():
    dia1 = font.render(d70,True,"Black");SCREEN.blit(dia1,(275,790))    
def t71():
    dia1 = font.render(d71,True,"Black");SCREEN.blit(dia1,(275,790))    
def t72():
    dia1 = font.render(d72,True,"Black");SCREEN.blit(dia1,(275,790))    
def t73():
    dia1 = font.render(d73,True,"Black");SCREEN.blit(dia1,(275,790))    
def t74():
    dia1 = font.render(d74,True,"Black");SCREEN.blit(dia1,(275,790))    
def t75():
    dia1 = font.render(d75,True,"Black");SCREEN.blit(dia1,(275,790))    
def t76():
    dia1 = font.render(d76,True,"Black");SCREEN.blit(dia1,(275,790))    
def t77():
    dia1 = font.render(d77,True,"Black");SCREEN.blit(dia1,(275,790))    
def t78():
    dia1 = font.render(d78,True,"Black");SCREEN.blit(dia1,(275,790))      
def t79():
    dia1 = font.render(d79,True,"Black");SCREEN.blit(dia1,(275,790))    
def t80():
    dia1 = font.render(d80,True,"Black");SCREEN.blit(dia1,(275,790))      
def t81():
    dia1 = font.render(d81,True,"Black");SCREEN.blit(dia1,(275,790))     
def t82():
    dia1 = font.render(d82,True,"Black");SCREEN.blit(dia1,(275,790))     
def t83():
    dia1 = font.render(d83,True,"Black");SCREEN.blit(dia1,(275,790))     
def t84():
    dia1 = font.render(d84,True,"Black");SCREEN.blit(dia1,(275,790))     
def t85():
    dia1 = font.render(d85,True,"Black");SCREEN.blit(dia1,(275,790))     
def t86():
    dia1 = font.render(d86,True,"Black");SCREEN.blit(dia1,(275,790))     
def t87():
    dia1 = font.render(d87,True,"Black");SCREEN.blit(dia1,(275,790))     
def t88():
    dia1 = font.render(d88,True,"Black");SCREEN.blit(dia1,(275,790))     
def t89():
    dia1 = font.render(d89,True,"Black");SCREEN.blit(dia1,(275,790))     
def t90():
    dia1 = font.render(d90,True,"Black");SCREEN.blit(dia1,(275,790))     
def t91():
    dia1 = font.render(d91,True,"Black");SCREEN.blit(dia1,(275,790))     
def t92():
    dia1 = font.render(d92,True,"Black");SCREEN.blit(dia1,(275,790))     
def t93():
    dia1 = font.render(d93,True,"Black");SCREEN.blit(dia1,(275,790))     
def t94():
    dia1 = font.render(d94,True,"Black");SCREEN.blit(dia1,(275,790))     
def t95():
    dia1 = font.render(d95,True,"Black");SCREEN.blit(dia1,(275,790))     
def t96():
    dia1 = font.render(d96,True,"Black");SCREEN.blit(dia1,(275,790))     
def t97():
    dia1 = font.render(d97,True,"Black");SCREEN.blit(dia1,(275,790))     
def t98():
    dia1 = font.render(d98,True,"Black");SCREEN.blit(dia1,(275,790))     
def t99():
    dia1 = font.render(d99,True,"Black");SCREEN.blit(dia1,(275,790))     
def t100():
    dia1 = font.render(d100,True,"Black");SCREEN.blit(dia1,(275,790))   
def t101():
    dia1 = font.render(d101,True,"Black");SCREEN.blit(dia1,(275,790))  
def t102():
    dia1 = font.render(d102,True,"Black");SCREEN.blit(dia1,(275,790))  
def t103():
    dia1 = font.render(d103,True,"Black");SCREEN.blit(dia1,(275,790)) 
def t104():
    dia1 = font.render(d104,True,"Black");SCREEN.blit(dia1,(275,790))   
def t105():
    dia1 = font.render(d105,True,"Black");SCREEN.blit(dia1,(275,790))   
def t106():
    dia1 = font.render(d106,True,"Black");SCREEN.blit(dia1,(275,790))   
def t107():
    dia1 = font.render(d107,True,"Black");SCREEN.blit(dia1,(275,790))   
def t108():
    dia1 = font.render(d108,True,"Black");SCREEN.blit(dia1,(275,790)) 
def t109():
    dia1 = font.render(d109,True,"Black");SCREEN.blit(dia1,(275,790))   
def t110():
    dia1 = font.render(d110,True,"Black");SCREEN.blit(dia1,(275,790))  
def t111():
    dia1 = font.render(d111,True,"Black");SCREEN.blit(dia1,(275,790))  
def t111b():
    dia2 = font.render(d111b,True,"Black");SCREEN.blit(dia2,(275,830))  
def t112():
    dia1 = font.render(d112,True,"Black");SCREEN.blit(dia1,(275,790))  
def t112b():
    dia2 = font.render(d112b,True,"Black");SCREEN.blit(dia2,(275,830)) 
def t113():
    dia1 = font.render(d113,True,"Black");SCREEN.blit(dia1,(275,790))  
def t114():
    dia1 = font.render(d114,True,"Black");SCREEN.blit(dia1,(275,790)) 
def t115():
    dia1 = font.render(d115,True,"Black");SCREEN.blit(dia1,(275,790)) 
def t116():
    dia1 = font.render(d116,True,"Black");SCREEN.blit(dia1,(275,790)) 
def t117():
    dia1 = font.render(d117,True,"Black");SCREEN.blit(dia1,(275,790))  
def t118():
    dia1 = font.render(d118,True,"Black");SCREEN.blit(dia1,(275,790))  
def t119():
    dia1 = font.render(d119,True,"Black");SCREEN.blit(dia1,(275,790))  
def sakondd1():
    dia1 = font.render(sakond1,True,"Black");SCREEN.blit(dia1,(275,790))
def sakondd2():
    dia1 = font.render(sakond2,True,"Black");SCREEN.blit(dia1,(275,790))
def sakondd3():
    dia1 = font.render(sakond3,True,"White");SCREEN.blit(dia1,(960,540))  
def t120():
    dia1 = font.render(d120,True,"Black");SCREEN.blit(dia1,(275,790)) 
def t121():
    dia1 = font.render(d121,True,"Black");SCREEN.blit(dia1,(275,790))   
def t122():
    dia1 = font.render(d122,True,"Black");SCREEN.blit(dia1,(275,790))  
def t123():
    dia1 = font.render(d123,True,"Black");SCREEN.blit(dia1,(275,790))  
def t124():
    dia1 = font.render(d124,True,"Black");SCREEN.blit(dia1,(275,790))    
def t125():
    dia2 = font.render(d125,True,"Black");SCREEN.blit(dia2,(275,830))     

class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)
	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False
	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)
def get_font(size):
    return pygame.font.Font("asety/fontus.ttf", size)
def play():
    pygame.mixer.music.stop()
    pygame.mixer.music.load("songus/usti.mp3")
    pygame.mixer.music.play(loops=-1)
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg1, (0, -3))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            s1()
        pygame.display.update()
        sleep(3)
        #skoušim vymyslet aby se zastavilo to psaní protože je to v while True , je to display flipem
        #animacefunkcni()
        #taklhle můžu dát text na obrazovku bez hoven

#def buttonu
DALSI_BUTTON = Button(image=pygame.image.load("asety/dalsi.png"), pos=(960, 540), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")
DOKNO_BUTTON= Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")
MOKNO_BUTTONPB= Button(image=None, pos=(425, 725),
                            text_input="Pan Bílý", font=get_font(30), base_color="White", hovering_color="White")
MOKNO_BUTTONN = Button(image=None, pos=(425, 725),
                            text_input="Nekolas", font=get_font(30), base_color="White", hovering_color="White")
MOKNO_BUTTONC= Button(image=None, pos=(425, 725),
                            text_input="Cedník", font=get_font(30), base_color="White", hovering_color="White")
MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")
SAKON1_BUTTON= Button(image=pygame.image.load("asety/vyberbutton.png"), pos=(500, 600), 
                                    text_input="Kde to je?", font=get_font(50), base_color="White", hovering_color="#4e61de")
SAKON2_BUTTON= Button(image=pygame.image.load("asety/vyberbutton.png"), pos=(1250, 600), 
                                    text_input="Co to je?", font=get_font(50), base_color="White", hovering_color="#4e61de")
#semeny
def s1():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg1, (0, -3))                                                                                 
        PLAY_BACK
        DOKNO_BUTTON
        MOKNO_BUTTONPB     
        DALSI_BUTTON
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONPB.update(SCREEN)
        t1()                                                                 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s2()                                                                                    
        pygame.display.update()
def s2():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg1, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTON
        DALSI_BUTTON
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.update(SCREEN)
        t2()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s3()                                                                                    
        pygame.display.update()
def s3():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg1, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTON
        DALSI_BUTTON
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.update(SCREEN)
        t3()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s4()                                                                                    
        pygame.display.update()
def s4():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB
        DALSI_BUTTON

        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONPB.update(SCREEN)
        t4()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s5()                                                                                    
        pygame.display.update()
def s5():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTON
        DALSI_BUTTON

        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.update(SCREEN)
        t5()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s6()                                                                                    
        pygame.display.update()
def s6():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTON
        DALSI_BUTTON

        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.update(SCREEN)
        t6()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    skr()                                                                                    
        pygame.display.update()
def skr():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg3, (0, -3))                                                                                #pozadi                                                                                           
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            skr2()                                                                                    
        pygame.display.update()
        sleep(3)
def skr2():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg4, (0, -3))                                                                                #pozadi                                                                                           
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            s7()                                                                                    
        pygame.display.update()
        sleep(3)
def s7():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t7()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s8()                                                                                    
        pygame.display.update()
def s8():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                         
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONPB.update(SCREEN)
        t8()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s9()                                                                                    
        pygame.display.update()
def s9():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                            
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t9()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s10()                                                                                    
        pygame.display.update()
def s10():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                            
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONPB.update(SCREEN)
        t10()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s11()                                                                                    
        pygame.display.update()
def s11():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t11()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s12()                                                                                    
        pygame.display.update()
def s12():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                          
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONPB.update(SCREEN)
        t12()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s13()                                                                                    
        pygame.display.update()
def s13():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t13()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s14()                                                                                    
        pygame.display.update()
def s14():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONPB.update(SCREEN)
        t14()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s15()                                                                                    
        pygame.display.update()
def s15():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t15()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s16()                                                                                    
        pygame.display.update()
def s16():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t16()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s17()                                                                                    
        pygame.display.update()
def s17():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONPB.update(SCREEN)
        t17()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s18()                                                                                    
        pygame.display.update()
def s18():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONPB.update(SCREEN)
        t18()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s19()                                                                                    
        pygame.display.update()
def s19():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t19()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s20()                                                                                    
        pygame.display.update()
def s20():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t20()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s21()                                                                                    
        pygame.display.update()
def s21():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONPB.update(SCREEN)
        t21()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s22()                                                                                    
        pygame.display.update()
def s22():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t22()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s23()                                                                                    
        pygame.display.update()
def s23():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t23()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s24()                                                                                    
        pygame.display.update()
def s24():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONPB.update(SCREEN)
        t24()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s25()                                                                                    
        pygame.display.update()
def s25():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t25()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s26()                                                                                    
        pygame.display.update()
def s26():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t26()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s27()                                                                                    
        pygame.display.update()
def s27():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t27()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s28()                                                                                    
        pygame.display.update()
def s28():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONPB.update(SCREEN)
        t28()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s29()                                                                                    
        pygame.display.update()
def s29():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t29()
        t29b()                                                                                             
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s30()                                                                                    
        pygame.display.update()
def s30():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t30()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s31()                                                                                    
        pygame.display.update()
def s31():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t31()
        t31b()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s32()                                                                                    
        pygame.display.update()
def s32():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONPB.update(SCREEN)
        t32()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s33()                                                                                    
        pygame.display.update()
def s33():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONPB.update(SCREEN)
        t33()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s34()                                                                                    
        pygame.display.update()
def s34():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t35()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s36()                                                                                    
        pygame.display.update()
def s36():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t36()
        t36b()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s37()                                                                                    
        pygame.display.update()
def s37():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONPB.update(SCREEN)
        t37()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s38()                                                                                    
        pygame.display.update()
def s38():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t38()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s39()                                                                                    
        pygame.display.update()
def s39():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONPB.update(SCREEN)
        t39()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s40()                                                                                    
        pygame.display.update()
def s40():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONPB.update(SCREEN)
        t40()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s41()                                                                                    
        pygame.display.update()
def s41():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t41()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s42()                                                                                    
        pygame.display.update()
def s42():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONPB.update(SCREEN)
        t42()   
        t42b()                                                                                             
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s43()                                                                                    
        pygame.display.update()
def s43():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t43()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s44()                                                                                    
        pygame.display.update()
def s44():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONPB.update(SCREEN)
        t44()
        t44b()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    intro()                                                                                    
        pygame.display.update()
def intro():
    while True:
        pygame.mixer.music.stop()    
        file_name = "vid/intro.mp4"
        window_name = "window"
        interframe_wait_ms = 30

        cap = cv2.VideoCapture(file_name)
        if not cap.isOpened():

            exit()

        cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        while (True):
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imshow(window_name, frame)
            if cv2.waitKey(interframe_wait_ms) & 0x7F == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()
        s45()
def s45():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg5, (0, -3))                                                                                #pozadi
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (700, 200))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONPB.update(SCREEN)
        t45() 
        t45b()                                                                                              
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s46()                                                                                    
        pygame.display.update()
def s46():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg5, (0, -3))                                                                                #pozadi
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (700, 200))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t46()                                                                                               
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s47()                                                                                    
        pygame.display.update()
def s47():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg5, (0, -3))                                                                                #pozadi
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (700, 200))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t47()                                                                                               
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s48()                                                                                    
        pygame.display.update()
def s48():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg5, (0, -3))                                                                                #pozadi
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (700, 200))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONPB.update(SCREEN)
        t48()                                                                                               
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s49()                                                                                    
        pygame.display.update()
def s49():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg5, (0, -3))                                                                                #pozadi
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (700, 200))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t49() 
        t49b()                                                                                               
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s50()                                                                                    
        pygame.display.update()
def s50():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg5, (0, -3))                                                                                #pozadi
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (700, 200))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONPB.update(SCREEN)
        t50()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s51()                                                                                    
        pygame.display.update()
def s51():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg5, (0, -3))                                                                                #pozadi
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (700, 200))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t51()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s52()                                                                                    
        pygame.display.update()
def s52():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg5, (0, -3))                                                                                #pozadi
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (700, 200))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONPB.update(SCREEN)
        t52()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s53()                                                                                    
        pygame.display.update()
def s53():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg5, (0, -3))                                                                                #pozadi
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (700, 200))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t53()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    svec()                                                                                    
        pygame.display.update()
def svec():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg6, (0, -3))  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            s54()
        pygame.display.update()
        sleep(3)
def s54():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg6, (0, -3))                                                                                #pozadi
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.update(SCREEN)
        t54() 
        t54b()                                                                                               
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s55()                                                                                    
        pygame.display.update()
def s55():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg6, (0, -3))                                                                                #pozadi
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="???", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/neznam.png').convert()                                                           #postava  
        SCREEN.blit(imp, (700, 200))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.update(SCREEN)
        t55()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s56()                                                                                    
        pygame.display.update()
def s56():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg6, (0, -3))                                                                                #pozadi
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.update(SCREEN)
        t56()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s57()                                                                                    
        pygame.display.update()
def s57():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg6, (0, -3))                                                                                #pozadi
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="???", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/neznam.png').convert()                                                           #postava  
        SCREEN.blit(imp, (700, 200))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.update(SCREEN)
        t57()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s58()                                                                                    
        pygame.display.update()
def s58():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg6, (0, -3))                                                                                #pozadi
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/neznam.png').convert()                                                           #postava  
        SCREEN.blit(imp, (700, 200))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONPB.update(SCREEN)
        t58()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s59()                                                                                    
        pygame.display.update()
def s59():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg6, (0, -3))                                                                                #pozadi
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="???", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/neznam.png').convert()                                                           #postava  
        SCREEN.blit(imp, (700, 200))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.update(SCREEN)
        t59()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    sls1()                                                                                    
        pygame.display.update()
def sls1():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(ls1, (0, -3))
        f = open("save1.txt", "w")
        f.close()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            s60()
        pygame.display.update()
        sleep(5)
def s60():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg1, (0, -3))                                                                                #pozadi
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.update(SCREEN)
        t60()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s61()                                                                                    
        pygame.display.update()
def s61():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg1, (0, -3))                                                                                #pozadi
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.update(SCREEN)
        t61()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s62()                                                                                    
        pygame.display.update()
def s62():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (700, 200))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t62()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s63()                                                                                    
        pygame.display.update()
def s63():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (700, 200))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONPB.update(SCREEN)
        t63()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s64()                                                                                    
        pygame.display.update()
def s64():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (700, 200))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t64()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s64w()                                                                                    
        pygame.display.update()
def s64w():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg1, (0, -3))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            s65()
        pygame.display.update()
        sleep(1)
def s65():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg1, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (500, 200))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONPB.update(SCREEN)
        t65()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s66()                                                                                    
        pygame.display.update()
def s66():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg1, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (500, 200))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t66()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s67()                                                                                    
        pygame.display.update()
def s67():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg1, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (500, 200))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONPB.update(SCREEN)
        t67()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s68()                                                                                    
        pygame.display.update()
def s68():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg1, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (500, 200))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t68()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s69()                                                                                    
        pygame.display.update()
def s69():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg1, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (500, 200))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONPB.update(SCREEN)
        t69()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s70w()                                                                                    
        pygame.display.update()
def s70w():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg7, (0, -3))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            s70()
        pygame.display.update()
        sleep(3)
def s70():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg7, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (900, 200))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t70()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s71()                                                                                    
        pygame.display.update()
def s71():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg7, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (900, 200))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t71()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s72()                                                                                    
        pygame.display.update()
def s72():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg7, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (900, 200))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONPB.update(SCREEN)
        t72()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s73()                                                                                    
        pygame.display.update()
def s73():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg7, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (900, 200))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t73()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s74()                                                                                    
        pygame.display.update()
def s74():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg7, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (900, 200))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t74()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s75w()                                                                                    
        pygame.display.update()
def s75w():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg7, (0, -3))
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (900, 200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            s75()
        pygame.display.update()
        sleep(5)
def s75():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg7, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (900, 200))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONPB.update(SCREEN)
        t75()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s76()                                                                                    
        pygame.display.update()
def s76():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg7, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (900, 200))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t76()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s77()                                                                                    
        pygame.display.update()
def s77():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg7, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (900, 200))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t77()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s78()                                                                                    
        pygame.display.update()
def s78():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg7, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (900, 200))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t78()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s79()                                                                                    
        pygame.display.update()
def s79():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg7, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (900, 200))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t79()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s80()                                                                                    
        pygame.display.update()
def s80():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg7, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (900, 200))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t80()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s81()                                                                                    
        pygame.display.update()
def s81():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg7, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (900, 200))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONPB.update(SCREEN)
        t81()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s82()                                                                                    
        pygame.display.update()
def s82():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg7, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (900, 200))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t82()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s83()                                                                                    
        pygame.display.update()
def s83():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg7, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (900, 200))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t83()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s84()                                                                                    
        pygame.display.update()
def s84():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg7, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (900, 200))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t84()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s85()                                                                                    
        pygame.display.update()
def s85():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg7, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON

        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (900, 200))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t85()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s86()                                                                                    
        pygame.display.update()
def s86():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg8, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, (400, 200))                                                         #postava  
        SCREEN.blit(imp, (1000, 170))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t86()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s87()                                                                                    
        pygame.display.update()
def s87():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg8, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONC     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, (400, 170))
        SCREEN.blit(imp, (1000, 200))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONC.update(SCREEN)
        t87()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s88()                                                                                    
        pygame.display.update()
def s88():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg8, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp2 = pygame.image.load('postavy/cednik.png').convert() 
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 170))
        SCREEN.blit(imp2, (400, 200))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t88()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s89()                                                                                    
        pygame.display.update()
def s89():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg8, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON                                                       #postava  
        DALSI_BUTTON.update(SCREEN)
        imp2 = pygame.image.load('postavy/cednik.png').convert() 
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 200))
        SCREEN.blit(imp2, (400, 200))
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONPB.update(SCREEN)
        t89()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s90()                                                                                    
        pygame.display.update()
def s90():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg8, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONC     
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 200))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, (400, 170))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONC.update(SCREEN)
        t90()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s91()                                                                                    
        pygame.display.update()
def s91():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg8, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONC     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 200))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, (400, 170))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONC.update(SCREEN)
        t91()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s92()                                                                                    
        pygame.display.update()
def s92():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg8, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON

        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 170))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, (400, 200))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t92()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s93()                                                                                    
        pygame.display.update()
def s93():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg8, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 200))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, (400, 200))                                                  #postava  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONPB.update(SCREEN)
        t93()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s94()                                                                                    
        pygame.display.update()
def s94():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg8, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONC     #jmeno
        DALSI_BUTTON

        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 200))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, (400, 170))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONC.update(SCREEN)
        t94()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s95()                                                                                    
        pygame.display.update()
def s95():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg8, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONC     #jmeno
        DALSI_BUTTON

        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 200))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, (400, 170))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONC.update(SCREEN)
        t95()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s96()                                                                                    
        pygame.display.update()
def s96():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg8, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON

        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 170))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, (400, 200))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t96()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s97()                                                                                    
        pygame.display.update()
def s97():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg8, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONC     #jmeno
        DALSI_BUTTON

        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 200))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, (400, 170))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONC.update(SCREEN)
        t97()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s98()                                                                                    
        pygame.display.update()
def s98():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg8, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 200))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, (400, 200))                                             #postava  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONPB.update(SCREEN)
        t98()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s99()                                                                                    
        pygame.display.update()
def s99():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg8, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON

        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 170))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, (400, 200))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t99()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s100()                                                                                    
        pygame.display.update()
def s100():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg8, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONC     #jmeno
        DALSI_BUTTON

        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 200))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, (400, 170))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONC.update(SCREEN)
        t100()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s101()                                                                                    
        pygame.display.update()
def s101():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg8, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON

        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 170))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, (400, 200))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t101()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s102()                                                                                    
        pygame.display.update()
def s102():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg8, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     
        DALSI_BUTTON

                                                           
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.update(SCREEN)
        t102()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s103()                                                                                    
        pygame.display.update()
def s103():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg8, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONC   
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 200))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, (400, 170))                                            
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONC.update(SCREEN)
        t103()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s104()                                                                                    
        pygame.display.update()
def s104():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg8, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN  
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 170))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, (400, 200))                                                  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t104()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s105()                                                                                    
        pygame.display.update()
def s105():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg8, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONC 
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 200))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, (400, 170))                                           
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONC.update(SCREEN)
        t105()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s106()                                                                                    
        pygame.display.update()
def s106():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg8, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONC 
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 200))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, (400, 170))                                              
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONC.update(SCREEN)
        t106()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s107()                                                                                    
        pygame.display.update()
def s107():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg8, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB
        DALSI_BUTTON                                                   
        DALSI_BUTTON.update(SCREEN)
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 200))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, (400, 200))
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONPB.update(SCREEN)
        t107()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s108()                                                                                    
        pygame.display.update()
def s108():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg8, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 170))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, (400, 200))                                              
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t108()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s109()                                                                                    
        pygame.display.update()
def s109():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg8, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONC 
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 200))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, (400, 170))                                                 
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONC.update(SCREEN)
        t109()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s110()                                                                                    
        pygame.display.update()
def s110():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg7, (0, -3))                                                                               
        PLAY_BACK   
        DALSI_BUTTON                                               
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        t110()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s111()                                                                                    
        pygame.display.update()
def s111():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg7, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()  
        SCREEN.blit(imp, (900, 200))                                                 
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        t111()   
        t111b()                                                                                             
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s112()                                                                                    
        pygame.display.update()
def s112():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg7, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()  
        SCREEN.blit(imp, (900, 200))                                                 
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN) 
        t112()
        t112b()                                                                                             
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s113()                                                                                    
        pygame.display.update()
def s113():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg7, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTON
        DALSI_BUTTON                                                
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.update(SCREEN) 
        t113()                                                                                           
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s114()                                                                                    
        pygame.display.update()
def s114():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg8, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONC
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 200))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, (400, 170))                                                
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONC.update(SCREEN) 
        t114()                                                                                           
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s115()                                                                                    
        pygame.display.update()
def s115():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg8, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 170))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, (400, 200))                                                  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN) 
        t115()                                                                                           
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s116()                                                                                    
        pygame.display.update()
def s116():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg8, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB
        DALSI_BUTTON                                               
        DALSI_BUTTON.update(SCREEN)
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 200))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, (400, 200))  
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONPB.update(SCREEN) 
        t116()                                                                                           
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s117()                                                                                    
        pygame.display.update()
def s117():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg8, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 170))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, (400, 200))                                                   
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN) 
        t117()                                                                                           
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s118()                                                                                    
        pygame.display.update()
def s118():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg8, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONC
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 200))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, (400, 170))                                                  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONC.update(SCREEN) 
        t118()                                                                                           
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s119()                                                                                    
        pygame.display.update()
def s119():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg8, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 170))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, (400, 200))                                                 
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN) 
        t119()                                                                                           
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s120()                                                                                    
        pygame.display.update()
def s120():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg8, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN
        SAKON1_BUTTON
        SAKON2_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 200))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, (400, 200))                                                   
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        SAKON1_BUTTON.update(SCREEN)
        SAKON2_BUTTON.update(SCREEN)
        SAKON1_BUTTON.changeColor(PLAY_MOUSE_POS)
        SAKON2_BUTTON.changeColor(PLAY_MOUSE_POS)                                                                                           
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if SAKON1_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s121()    
                if SAKON2_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    sakon1()                                                                              
        pygame.display.update()
def sakon1():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg8, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB                                                 
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONPB.update(SCREEN) 
        sakondd1()                                                                                      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()   
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    sakon2()                                                                          
        pygame.display.update()
def sakon2():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg8, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN                                               
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        imp = pygame.image.load('postavy/Nekolas.png').convert()
        SCREEN.blit(imp, (900, 200))    
        sakondd2() 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()   
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    sakon3()                                                                          
        pygame.display.update()
def sakon3():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        sakondd3() 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()   
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    pygame.quit()
                    sys.exit()                                                                       
        pygame.display.update()
def s121():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg8, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB
        DALSI_BUTTON                                              
        DALSI_BUTTON.update(SCREEN)
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 200))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, (400, 200))  
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONPB.update(SCREEN) 
        t120()                                                                                           
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s122()                                                                                    
        pygame.display.update()
def s122():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg8, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONC
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 200))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, (400, 170))                                                  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONC.update(SCREEN) 
        t121()                                                                                           
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s123()                                                                                    
        pygame.display.update()
def s123():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg8, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 170))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, (400, 200))                                                
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN) 
        t122()                                                                                           
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s124()                                                                                    
        pygame.display.update()
def s124():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg8, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 170))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, (400, 200))                                                 
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN) 
        t123()                                                                                           
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s125()                                                                                    
        pygame.display.update()
def s125():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg8, (0, -3))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 170))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, (400, 200))                                                  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN) 
        t124()  
        t125()                                                                                         
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    sls2()                                                                                    
        pygame.display.update()
def sls2():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos();SCREEN.fill("black");SCREEN.blit(ls1, (0, -3));f = open("save2.txt", "w");f.close()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();sys.exit()
            s125()
        pygame.display.update()
        sleep(5)







def ses():
    pygame.mixer.music.stop()
    pygame.mixer.music.load("songus/finger.mp3")
    pygame.mixer.music.play(loops=0)
#def buttonu v menu
PLAY_BUTTON = Button(image=pygame.image.load("asety/startus.png"), pos=(1750, 300), 
                                    text_input="Nová hra", font=get_font(50), base_color="#732c06", hovering_color="White")
OPTIONS_BUTTON = Button(image=pygame.image.load("asety/nastus.png"), pos=(1750, 700), 
                                    text_input="Nastavení", font=get_font(50), base_color="#732c06", hovering_color="White")
QUIT_BUTTON = Button(image=pygame.image.load("asety/koncus.png"), pos=(1750, 900), 
                                    text_input="Konec", font=get_font(50), base_color="#732c06", hovering_color="White")
SES_BUTTON = Button(image=pygame.image.load("asety/ses.png"), pos=(715, 153), 
                                    text_input="", font=get_font(50), base_color="#732c06", hovering_color="White")
POK_BUTTON = Button(image=pygame.image.load("asety/pokus.png"), pos=(1750, 500), 
                                    text_input="Pokračovat", font=get_font(45), base_color="#732c06", hovering_color="White")
def POMOC():
    pygame.mixer.music.load("songus/songusamogusdruhus.mp3")
    pygame.mixer.music.load("songus/songusamongus.mp3")
    pygame.mixer.music.play(loops=-1)
    save1 = os.path.exists("save1.txt")
    save2=os.path.exists("save2.txt")
    if save2:
        def main_menu3():
            while True:
                SCREEN.blit(BG, (0, 0))
                MENU_MOUSE_POS = pygame.mouse.get_pos()
                MENU_TEXT = get_font(100).render("", True, "#732c06")
                MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
                PLAY_BUTTON 
                OPTIONS_BUTTON 
                QUIT_BUTTON 
                SES_BUTTON 
                POK_BUTTON
                SCREEN.blit(MENU_TEXT, MENU_RECT)
                def options():
                    while True:
                        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
                        
                        SCREEN.fill("white")
                        OPTIONS_TEXT = get_font(45).render("Nastav si radši mámu", True, "Black")
                        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
                        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

                        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")
                        ROZ_BUTTON = Button(image=pygame.image.load("asety/nh.png"), pos=(640, 660), 
                                            text_input=None, font=get_font(75), base_color="Black", hovering_color="Green")              
                        HH_BUTTON = Button(image=pygame.image.load("asety/hh.png"), pos=(1040, 660),
                                            text_input=None, font=get_font(75), base_color="Black", hovering_color="Green")
                        HH_BUTTON.update(SCREEN)
                        ROZ_BUTTON.changeColor(OPTIONS_MOUSE_POS)
                        ROZ_BUTTON.update(SCREEN)                     
                        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
                        OPTIONS_BACK.update(SCREEN)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                                    main_menu3()
                                if ROZ_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                                    nh()
                                if HH_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                                    hh()
                        pygame.display.update()
                for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON, SES_BUTTON,POK_BUTTON]:
                    button.changeColor(MENU_MOUSE_POS)
                    button.update(SCREEN)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                            play()
                        if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                            options()
                        if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                            pygame.quit()
                            sys.exit()
                        if SES_BUTTON.checkForInput(MENU_MOUSE_POS):
                            ses()
                        if POK_BUTTON.checkForInput(MENU_MOUSE_POS):
                            pygame.mixer.music.rewind()
                            sls2()
                pygame.display.update()
        main_menu3()
    if save1:
        def main_menu2():
            while True:
                SCREEN.blit(BG, (0, 0))
                MENU_MOUSE_POS = pygame.mouse.get_pos()
                MENU_TEXT = get_font(100).render("", True, "#732c06")
                MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
                PLAY_BUTTON 
                OPTIONS_BUTTON 
                QUIT_BUTTON 
                SES_BUTTON 
                POK_BUTTON
                SCREEN.blit(MENU_TEXT, MENU_RECT)
                def options():
                    while True:
                        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
                        
                        SCREEN.fill("white")
                        OPTIONS_TEXT = get_font(45).render("Nastav si radši mámu", True, "Black")
                        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
                        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

                        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

                        ROZ_BUTTON = Button(image=pygame.image.load("asety/nh.png"), pos=(640, 660), 
                                            text_input=None, font=get_font(75), base_color="Black", hovering_color="Green")
                                        
                        HH_BUTTON = Button(image=pygame.image.load("asety/hh.png"), pos=(1040, 660),
                                            text_input=None, font=get_font(75), base_color="Black", hovering_color="Green")
                        HH_BUTTON.update(SCREEN)

                        ROZ_BUTTON.changeColor(OPTIONS_MOUSE_POS)
                        ROZ_BUTTON.update(SCREEN)           
                                    
                        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
                        OPTIONS_BACK.update(SCREEN)

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                                    main_menu2()
                                if ROZ_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                                    nh()
                                if HH_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                                    hh()

                        pygame.display.update()
                for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON, SES_BUTTON,POK_BUTTON]:
                    button.changeColor(MENU_MOUSE_POS)
                    button.update(SCREEN)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                            play()
                        if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                            options()
                        if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                            pygame.quit()
                            sys.exit()
                        if SES_BUTTON.checkForInput(MENU_MOUSE_POS):
                            ses()
                        if POK_BUTTON.checkForInput(MENU_MOUSE_POS):
                            pygame.mixer.music.rewind()
                            sls1()
                pygame.display.update()
        main_menu2()
    else:
        def main_menu():
            while True:
                SCREEN.blit(BG, (0, 0))
                MENU_MOUSE_POS = pygame.mouse.get_pos()
                MENU_TEXT = get_font(100).render("", True, "#732c06")
                MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
                PLAY_BUTTON
                OPTIONS_BUTTON
                QUIT_BUTTON
                SES_BUTTON
                SCREEN.blit(MENU_TEXT, MENU_RECT)
                def options():
                    while True:
                        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
                        
                        SCREEN.fill("white")
                        OPTIONS_TEXT = get_font(45).render("Nastav si radši mámu", True, "Black")
                        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
                        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

                        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

                        ROZ_BUTTON = Button(image=pygame.image.load("asety/nh.png"), pos=(640, 660), 
                                            text_input=None, font=get_font(75), base_color="Black", hovering_color="Green")
                                        
                        HH_BUTTON = Button(image=pygame.image.load("asety/hh.png"), pos=(1040, 660),
                                            text_input=None, font=get_font(75), base_color="Black", hovering_color="Green")
                        HH_BUTTON.update(SCREEN)

                        ROZ_BUTTON.changeColor(OPTIONS_MOUSE_POS)
                        ROZ_BUTTON.update(SCREEN)           
                                    
                        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
                        OPTIONS_BACK.update(SCREEN)

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                                    main_menu()
                                if ROZ_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                                    nh()
                                if HH_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                                    hh()

                        pygame.display.update()
                for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON, SES_BUTTON]:
                    button.changeColor(MENU_MOUSE_POS)
                    button.update(SCREEN)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                            pygame.mixer.music.rewind()
                            play()
                        if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                            options()
                        if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                            pygame.quit()
                            sys.exit()
                        if SES_BUTTON.checkForInput(MENU_MOUSE_POS):
                            ses()
                pygame.display.update()
        main_menu()
POMOC()
