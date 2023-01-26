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
Width = GetSystemMetrics(0)
Height = GetSystemMetrics(1)
os.chdir(os.path.dirname(os.path.abspath(__file__)))
pygame.init()
SCREEN = pygame.display.set_mode((Width, Height))
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
bg9 = pygame.image.load("pozadi/busak.png")
bg10=pygame.image.load("pozadi/tyrsak.png")
bg11=pygame.image.load("pozadi/gympl.png")
bg12=pygame.image.load("pozadi/billa.png")
bg13=pygame.image.load("pozadi/kostel.png")
bg14=pygame.image.load("pozadi/pramen.png")
bg15=pygame.image.load("pozadi/zs.png")
bg16=pygame.image.load("pozadi/mesto.png")
bg17=pygame.image.load("pozadi/sakon.png")
bg18=pygame.image.load("pozadi/america.png")
bg19=pygame.image.load("pozadi/kopecek.png")
bg20=pygame.image.load("pozadi/podsance.png")
bg21=pygame.image.load("pozadi/park.png")
bg22=pygame.image.load("pozadi/cednikzoom.png")
ls1=pygame.image.load("asety/ls1.png")
dokno=pygame.image.load("asety/mdva.png")
mtri=pygame.image.load("asety/mtri.png")
mctyri=pygame.image.load("asety/mctyri.png")
vyberbutton=pygame.image.load("asety/vyberbutton.png")
resized_BG= pygame.transform.scale(BG,(Width,Height))
resized_bg1= pygame.transform.scale(bg1,(Width,Height))
resized_bg2= pygame.transform.scale(bg2,(Width,Height))
resized_bg3= pygame.transform.scale(bg3,(Width,Height))
resized_bg4= pygame.transform.scale(bg4,(Width,Height))
resized_bg5= pygame.transform.scale(bg5,(Width,Height))
resized_bg6= pygame.transform.scale(bg6,(Width,Height))
resized_bg7= pygame.transform.scale(bg7,(Width,Height))
resized_bg8= pygame.transform.scale(bg8,(Width,Height))
resized_bg9= pygame.transform.scale(bg9,(Width,Height))
resized_bg10= pygame.transform.scale(bg10,(Width,Height))
resized_bg11= pygame.transform.scale(bg11,(Width,Height))
resized_bg12= pygame.transform.scale(bg12,(Width,Height))
resized_bg13= pygame.transform.scale(bg13,(Width,Height))
resized_bg14= pygame.transform.scale(bg14,(Width,Height))
resized_bg15= pygame.transform.scale(bg15,(Width,Height))
resized_bg16= pygame.transform.scale(bg16,(Width,Height))
resized_bg17= pygame.transform.scale(bg17,(Width,Height))
resized_bg18= pygame.transform.scale(bg18,(Width,Height))
resized_bg19= pygame.transform.scale(bg19,(Width,Height))
resized_bg20= pygame.transform.scale(bg20,(Width,Height))
resized_bg21= pygame.transform.scale(bg21,(Width,Height))
resized_bg22= pygame.transform.scale(bg22,(Width,Height))
resized_mdva= pygame.transform.scale(dokno,((Width/100)*100,(Height/100)*100))
resized_ls= pygame.transform.scale(ls1,((Width/100)*100,(Height/100)*100))
resized_mtri=pygame.transform.scale(mtri,((Width/100)*100,(Height/100)*100))
resized_mctyri=pygame.transform.scale(mctyri,((Width/100)*100,(Height/100)*100))
resized_vyberbutton=pygame.transform.scale(vyberbutton,((Width/100)*30,(Height/100)*9.0740740740741))
#fotni
font =  pygame.font.Font("asety/fontus.ttf", (Height//100)*3)
font_meno =pygame.font.Font("asety/fontus.ttf", (Height//100)*(277//100))
font_vyber=pygame.font.Font("asety/fontus.ttf", (Height//100)*(4629//1000))
def t1():
    dia1 = font.render(d1,True,"Black") ;SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t2():
    dia1 = font.render(d2,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))   
def t3():
    dia1 = font.render(d3,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))   
def t4():
    dia1 = font.render(d4,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))   
def t5():
    dia1 = font.render(d5,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))   
def t6():
    dia1 = font.render(d6,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))   
def t7():
    dia1 = font.render(d7,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))   
def t8():
    dia1 = font.render(d8,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))   
def t9():
    dia1 = font.render(d9,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))   
def t10():
    dia1 = font.render(d10,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t11():
    dia1 = font.render(d11,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t12():
    dia1 = font.render(d12,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t13():
    dia1 = font.render(d13,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t14():
    dia1 = font.render(d14,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t15():
    dia1 = font.render(d15,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t16():
    dia1 = font.render(d16,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t17():
    dia1 = font.render(d17,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t18():
    dia1 = font.render(d18,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t19():
    dia1 = font.render(d19,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t20():
    dia1 = font.render(d20,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t21():
    dia1 = font.render(d21,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t22():
    dia1 = font.render(d22,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t23():
    dia1 = font.render(d23,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t24():
    dia1 = font.render(d24,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t25():
    dia1 = font.render(d25,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t26():
    dia1 = font.render(d26,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t27():
    dia1 = font.render(d27,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t28():
    dia1 = font.render(d28,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t29():
    dia1 = font.render(d29,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t29b():
    dia2 = font.render(d29b,True,"Black") ;SCREEN.blit(dia2,((Width/100)*14.322916,(Height/100)*76.851851851852))   
def t30():
    dia1 = font.render(d30,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t31():
    dia1 = font.render(d31,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t31b():
    dia2 = font.render(d31b,True,"Black") ;SCREEN.blit(dia2,((Width/100)*14.322916,(Height/100)*76.851851851852))   
def t32():
    dia1 = font.render(d32,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t33():
    dia1 = font.render(d33,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t34():
    dia1 = font.render(d34,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t35():
    dia1 = font.render(d35,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t36():
    dia1 = font.render(d36,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t36b():
    dia2 = font.render(d36b,True,"Black") ;SCREEN.blit(dia2,((Width/100)*14.322916,(Height/100)*76.851851851852))  
def t37():
    dia1 = font.render(d37,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t38():
    dia1 = font.render(d38,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t39():
    dia1 = font.render(d39,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t40():
    dia1 = font.render(d40,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t41():
    dia1 = font.render(d41,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t42():
    dia1 = font.render(d42,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t42b():
    dia2 = font.render(d42b,True,"Black") ;SCREEN.blit(dia2,((Width/100)*14.322916,(Height/100)*76.851851851852))     
def t43():
    dia1 = font.render(d43,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t44():
    dia1 = font.render(d44,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t44b():
    dia2 = font.render(d44b,True,"Black") ;SCREEN.blit(dia2,((Width/100)*14.322916,(Height/100)*76.851851851852))  
def t45():
    dia1 = font.render(d45,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t45b():
    dia2 = font.render(d45b,True,"Black") ;SCREEN.blit(dia2,((Width/100)*14.322916,(Height/100)*76.851851851852))  
def t46():
    dia1 = font.render(d46,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t47():
    dia1 = font.render(d47,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t48():
    dia1 = font.render(d48,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t49():
    dia1 = font.render(d49,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t49b():
    dia2 = font.render(d49b,True,"Black") ;SCREEN.blit(dia2,((Width/100)*14.322916,(Height/100)*76.851851851852))
def t50():
    dia1 = font.render(d50,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t51():
    dia1 = font.render(d51,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t52():
    dia1 = font.render(d52,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t53():
    dia1 = font.render(d53,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t54():
    dia1 = font.render(d54,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t54b():
    dia2 = font.render(d54b,True,"Black") ;SCREEN.blit(dia2,((Width/100)*14.322916,(Height/100)*76.851851851852)) 
def t55():
    dia1 = font.render(d55,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t56():
    dia1 = font.render(d56,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t57():
    dia1 = font.render(d57,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t58():
    dia1 = font.render(d58,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t59():
    dia1 = font.render(d59,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t60():
    dia1 = font.render(d60,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t61():
    dia1 = font.render(d61,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t62():
    dia1 = font.render(d62,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t63():
    dia1 = font.render(d63,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t64():
    dia1 = font.render(d64,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t65():
    dia1 = font.render(d65,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t66():
    dia1 = font.render(d66,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t67():
    dia1 = font.render(d67,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t68():
    dia1 = font.render(d68,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t69():
    dia1 = font.render(d69,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t70():
    dia1 = font.render(d70,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t71():
    dia1 = font.render(d71,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t72():
    dia1 = font.render(d72,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t73():
    dia1 = font.render(d73,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t74():
    dia1 = font.render(d74,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t75():
    dia1 = font.render(d75,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t76():
    dia1 = font.render(d76,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t77():
    dia1 = font.render(d77,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t78():
    dia1 = font.render(d78,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))      
def t79():
    dia1 = font.render(d79,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t80():
    dia1 = font.render(d80,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))      
def t81():
    dia1 = font.render(d81,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))     
def t82():
    dia1 = font.render(d82,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))     
def t83():
    dia1 = font.render(d83,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))     
def t84():
    dia1 = font.render(d84,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))     
def t85():
    dia1 = font.render(d85,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))     
def t86():
    dia1 = font.render(d86,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))     
def t87():
    dia1 = font.render(d87,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))     
def t88():
    dia1 = font.render(d88,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))     
def t89():
    dia1 = font.render(d89,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))     
def t90():
    dia1 = font.render(d90,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))     
def t91():
    dia1 = font.render(d91,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))     
def t92():
    dia1 = font.render(d92,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))     
def t93():
    dia1 = font.render(d93,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))     
def t94():
    dia1 = font.render(d94,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))     
def t95():
    dia1 = font.render(d95,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))     
def t96():
    dia1 = font.render(d96,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))     
def t97():
    dia1 = font.render(d97,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))     
def t98():
    dia1 = font.render(d98,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))     
def t99():
    dia1 = font.render(d99,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))     
def t100():
    dia1 = font.render(d100,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))   
def t101():
    dia1 = font.render(d101,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))  
def t102():
    dia1 = font.render(d102,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))  
def t103():
    dia1 = font.render(d103,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148)) 
def t104():
    dia1 = font.render(d104,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))   
def t105():
    dia1 = font.render(d105,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))   
def t106():
    dia1 = font.render(d106,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))   
def t107():
    dia1 = font.render(d107,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))   
def t108():
    dia1 = font.render(d108,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148)) 
def t109():
    dia1 = font.render(d109,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))   
def t110():
    dia1 = font.render(d110,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))  
def t111():
    dia1 = font.render(d111,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))  
def t111b():
    dia2 = font.render(d111b,True,"Black");SCREEN.blit(dia2,((Width/100)*14.322916,(Height/100)*76.851851851852))  
def t112():
    dia1 = font.render(d112,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))  
def t112b():
    dia2 = font.render(d112b,True,"Black");SCREEN.blit(dia2,((Width/100)*14.322916,(Height/100)*76.851851851852)) 
def t113():
    dia1 = font.render(d113,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))  
def t114():
    dia1 = font.render(d114,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148)) 
def t115():
    dia1 = font.render(d115,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148)) 
def t116():
    dia1 = font.render(d116,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148)) 
def t117():
    dia1 = font.render(d117,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))  
def t118():
    dia1 = font.render(d118,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))  
def t119():
    dia1 = font.render(d119,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))  
def sakondd1():
    dia1 = font.render(sakond1,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
def sakondd2():
    dia1 = font.render(sakond2,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
def sakondd3():
    dia1 = font.render(sakond3,True,"White");SCREEN.blit(dia1,((Width/100)*50,(Height/100)*50))  
def t120():
    dia1 = font.render(d120,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148)) 
def t121():
    dia1 = font.render(d121,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))   
def t122():
    dia1 = font.render(d122,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))  
def t123():
    dia1 = font.render(d123,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))  
def t124():
    dia1 = font.render(d124,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))    
def t125():
    dia2 = font.render(d125,True,"Black");SCREEN.blit(dia2,((Width/100)*14.322916,(Height/100)*76.851851851852)) 
def t126():
    dia1 = font.render(d126,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148)) 
def t127():
    dia1 = font.render(d127,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
def t128():
    dia1 = font.render(d128,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148)) 
def t129():
    dia1 = font.render(d129,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148)) 
def t130():
    dia1 = font.render(d130,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
def t131():
    dia1 = font.render(d131,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
def t132():
    dia1 = font.render(d132,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
def t133():
    dia1 = font.render(d133,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
def t134():
    dia1 = font.render(d134,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
def t135():
    dia1 = font.render(d135,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
def t136():
    dia1 = font.render(d136,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
def t137():
    dia1 = font.render(d137,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
def t138():
    dia1 = font.render(d138,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
def t139():
    dia1 = font.render(d139,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
def t140():
    dia1 = font.render(d140,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))     

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
    pygame.mixer.music.load("songus/usti.wav")
    pygame.mixer.music.play(loops=-1)
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg1, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            s1()
        pygame.display.update()
        sleep(3)
#def buttonu
DALSI_BUTTON = Button(image=pygame.image.load("asety/dalsi.png"), pos=((Width/100)*50, (Height/100)*50), 
                            text_input="", font=font_meno, base_color="White", hovering_color="White")
DOKNO_BUTTON= Button(image=(resized_mdva), pos=((Width/100)*40.625,(Height/100)*46.296), 
                            text_input="", font=font_meno, base_color="White", hovering_color="Green")
PLAY_BACK = Button(image=None, pos=((Width/100)*91.14583, (Height/100)*4.629), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")
MOKNO_BUTTONPB= Button(image=None, pos=( (Width/100)*22.135416, (Height/100)*67.12962962963),
                            text_input="Pan Bílý", font=font_meno, base_color="White", hovering_color="White")
MOKNO_BUTTONN = Button(image=None, pos=((Width/100)*22.135416, (Height/100)*67.12962962963),
                            text_input="Nekolas", font=font_meno, base_color="White", hovering_color="White")
MOKNO_BUTTONC= Button(image=None, pos=((Width/100)*22.135416,(Height/100)*67.12962962963),
                            text_input="Cedník", font=font_meno, base_color="White", hovering_color="White")
MOKNO_BUTTON= Button(image=None, pos=((Width/100)*22.135416, (Height/100)*67.12962962963),
                            text_input="", font=font_meno, base_color="White", hovering_color="White")
MOKNO_BUTTONŠ= Button(image=None, pos=((Width/100)*22.135416, (Height/100)*67.12962962963),
                            text_input="Štěpán", font=font_meno, base_color="White", hovering_color="White")
MOKNO_BUTTONS=Button(image=None, pos=((Width/100)*22.135416, (Height/100)*67.12962962963),
                            text_input="Strom", font=font_meno, base_color="White", hovering_color="White")
MOKNO_BUTTONK =Button(image=None, pos=((Width/100)*22.135416, (Height/100)*67.12962962963),
                            text_input="Karviňáci", font=font_meno, base_color="White", hovering_color="White")
SAKON1_BUTTON= Button(image=(resized_vyberbutton), pos=((Width/100)*26.0416,(Height/100)*55.55), 
                                    text_input="Kde to je?", font=font_vyber, base_color="White", hovering_color="#4e61de")
SAKON2_BUTTON= Button(image=(resized_vyberbutton), pos=((Width/100)*65.10416,(Height/100)*55.55), 
                                    text_input="Co to je?", font=font_vyber, base_color="White", hovering_color="#4e61de")

#semeny
def s1():
    if os.path.exists("save1.txt"):
        os.remove("save1.txt")
    if os.path.exists("save2.txt"):
        os.remove("save2.txt")
    if os.path.exists("save3.txt"):
        os.remove("save3.txt")
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(resized_bg1, (0, 0))                                                                                 
        PLAY_BACK
        DOKNO_BUTTON
        MOKNO_BUTTONPB     
        DALSI_BUTTON
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTON
        DALSI_BUTTON
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTON
        DALSI_BUTTON
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        SCREEN.blit(resized_bg2, (0, 0))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB
        DALSI_BUTTON
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTON
        DALSI_BUTTON

        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTON
        DALSI_BUTTON
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        SCREEN.blit(resized_bg3, (0, 0))                                                                                #pozadi                                                                                           
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
        SCREEN.blit(resized_bg4, (0, 0))                                                                                #pozadi                                                                                           
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
        SCREEN.blit(resized_bg2, (0, 0))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*27.77))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                         
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*27.77))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                            
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*27.77))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                            
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*27.77))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*27.77))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                          
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*27.77))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*27.77))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*27.77))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*27.77))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*27.77))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*27.77))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*27.77))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*27.77))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*27.77))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*27.77))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*27.77))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*27.77))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*27.77))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*27.77))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*27.77))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*27.77))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*27.77))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*27.77))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*27.77))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*27.77))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*27.77))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*27.77))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*27.77))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*27.77))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*27.77))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*27.77))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*27.77))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*27.77))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*27.77))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*27.77))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*27.77))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*27.77))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        pygame.mixer.music.load("songus/songusamongus.wav")
        pygame.mixer.music.load("songus/songusamogusdruhus.wav")
        pygame.mixer.music.play(loops=-1)
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(resized_bg5, (0, 0))                                                                                #pozadi
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*36.4583, (Height/100)*18.518))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                               #pozadi
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*36.4583, (Height/100)*18.518))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                               #pozadi
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*36.4583, (Height/100)*18.518))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                               #pozadi
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*36.4583, (Height/100)*18.518))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                               #pozadi
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*36.4583, (Height/100)*18.518))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                               #pozadi
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*36.4583, (Height/100)*18.518))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                               #pozadi
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*36.4583, (Height/100)*18.518))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                               #pozadi
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*36.4583, (Height/100)*18.518))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                               #pozadi
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*36.4583, (Height/100)*18.518))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        SCREEN.blit(resized_bg6, (0, 0))  
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
        SCREEN.blit(resized_bg6, (0, 0))                                                                                #pozadi
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="", font=font_meno, base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                                #pozadi
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="???", font=font_meno, base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/neznam.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*36.4583, (Height/100)*18.518))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                                #pozadi
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="", font=font_meno, base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                                #pozadi
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="???", font=font_meno, base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/neznam.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*36.4583, (Height/100)*18.518))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                                #pozadi
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/neznam.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*36.4583, (Height/100)*18.518))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                                #pozadi
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="???", font=font_meno, base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/neznam.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*36.4583, (Height/100)*18.518))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        SCREEN.blit(resized_ls, (0, 0))
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
        SCREEN.blit(resized_bg1, (0, 0))                                                                                #pozadi
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="", font=font_meno, base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                               #pozadi
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="", font=font_meno, base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        SCREEN.blit(resized_bg2, (0, 0))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*36.4583, (Height/100)*18.518))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*36.4583, (Height/100)*18.518))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*36.4583, (Height/100)*18.518))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        SCREEN.blit(resized_bg1, (0, 0))
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*26.0416, (Height/100)*18.5185))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*26.0416, (Height/100)*18.5185))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*26.0416, (Height/100)*18.5185))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*26.0416, (Height/100)*18.5185))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*26.0416, (Height/100)*18.5185))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        SCREEN.blit(resized_bg7, (0, 0))
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*46.875, (Height/100)*18.518))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*46.875, (Height/100)*18.518))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*46.875, (Height/100)*18.518))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*46.875, (Height/100)*18.518))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*46.875, (Height/100)*18.518))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        SCREEN.blit(resized_bg7, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*46.875, (Height/100)*18.518))
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*46.875, (Height/100)*18.518))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*46.875, (Height/100)*18.518))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*46.875, (Height/100)*18.518))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*46.875, (Height/100)*18.518))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*46.875, (Height/100)*18.518))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*46.875, (Height/100)*18.518))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*46.875, (Height/100)*18.518))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*46.875, (Height/100)*18.518))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*46.875, (Height/100)*18.518))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*46.875, (Height/100)*18.518))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*46.875, (Height/100)*18.518))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        SCREEN.blit(resized_bg8, (0, 0))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*20.83, (Height/100)*18.518))                                                         #postava  
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*15.740))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        SCREEN.blit(resized_bg8, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                              
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONC     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/nekolas.png').convert()
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*20.83, (Height/100)*15.740))
        SCREEN.blit(imp, ((Width/100)*52.083,(Height/100)*18.518 ))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        SCREEN.blit(resized_bg8, (0, 0))                                                             
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp2 = pygame.image.load('postavy/cednik.png').convert() 
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*15.740))
        SCREEN.blit(imp2, ((Width/100)*20.83, (Height/100)*18.518)) 
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        SCREEN.blit(resized_bg8, (0, 0))                                                                     
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON                                                       #postava  
        DALSI_BUTTON.update(SCREEN)
        imp2 = pygame.image.load('postavy/cednik.png').convert() 
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083,(Height/100)*18.518 ))
        SCREEN.blit(imp2, ((Width/100)*20.83, (Height/100)*18.518)) 
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        SCREEN.blit(resized_bg8, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                   
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONC     
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083,(Height/100)*18.518 ))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*20.83, (Height/100)*15.740))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        SCREEN.blit(resized_bg8, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                              
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONC     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083,(Height/100)*18.518 ))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*20.83, (Height/100)*15.740))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        SCREEN.blit(resized_bg8, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                              
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*15.740))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*20.83, (Height/100)*18.518)) 
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        SCREEN.blit(resized_bg8, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                         
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083,(Height/100)*18.518 ))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*20.83, (Height/100)*18.518))                                                   #postava  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        SCREEN.blit(resized_bg8, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                           
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONC     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083,(Height/100)*18.518 ))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*20.83, (Height/100)*15.740))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        SCREEN.blit(resized_bg8, (0, 0))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONC     #jmeno
        DALSI_BUTTON
        SCREEN.blit(resized_bg8, (0, 0))
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083,(Height/100)*18.518 ))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*20.83, (Height/100)*15.740))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        SCREEN.blit(resized_bg8, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                              
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*15.740))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*20.83, (Height/100)*18.518)) 
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        SCREEN.blit(resized_bg8, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                             
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONC     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083,(Height/100)*18.518 ))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*20.83, (Height/100)*15.740))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        SCREEN.blit(resized_bg8, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                              
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083,(Height/100)*18.518 ))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*20.83, (Height/100)*18.518))                                              #postava  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        SCREEN.blit(resized_bg8, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                           
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*15.740))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*20.83, (Height/100)*18.518)) 
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        SCREEN.blit(resized_bg8, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                             
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONC     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083,(Height/100)*18.518 ))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*20.83, (Height/100)*15.740))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        SCREEN.blit(resized_bg8, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                            
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN     #jmeno
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*15.740))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*20.83, (Height/100)*18.518)) 
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        SCREEN.blit(resized_bg22, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                              
        PLAY_BACK      
        DALSI_BUTTON                           
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)                                                                                            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    flashback()                                                                                   
        pygame.display.update()
def flashback():
    while True:
        SCREEN.blit(resized_bg8, (0, 0))
        pygame.mixer.music.stop()
        pygame.mixer.music.load("songus/zabniju.wav")
        pygame.mixer.music.play(loops=0)
        file_name = "vid/zabniju.mp4"
        window_name = "window"
        interframe_wait_ms = 24
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
        s103()                      
def s103():
    while True:
        pygame.mixer.music.load("songus/songusamogusdruhus.wav")
        pygame.mixer.music.load("songus/songusamongus.wav")
        SCREEN.blit(resized_bg8, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                              
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONC   
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083,(Height/100)*18.518 ))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*20.83, (Height/100)*15.740))                                            
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        SCREEN.blit(resized_bg8, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                              
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN  
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*15.740))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*20.83, (Height/100)*18.518))                                                   
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        SCREEN.blit(resized_bg8, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                              
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONC 
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083,(Height/100)*18.518 ))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*20.83, (Height/100)*15.740))                                           
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        SCREEN.blit(resized_bg8, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                              
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONC 
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083,(Height/100)*18.518 ))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*20.83, (Height/100)*15.740))                                              
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        SCREEN.blit(resized_bg8, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                            
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB
        DALSI_BUTTON                                                   
        DALSI_BUTTON.update(SCREEN)
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083,(Height/100)*18.518 ))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*20.83, (Height/100)*18.518)) 
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        SCREEN.blit(resized_bg8, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                             
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*15.740))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*20.83, (Height/100)*18.518))                                               
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        SCREEN.blit(resized_bg8, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                             
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONC 
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083,(Height/100)*18.518 ))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*20.83, (Height/100)*15.740))                                                 
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        SCREEN.blit(resized_bg7, (0, 0))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()  
        SCREEN.blit(imp, ((Width/100)*46.875, (Height/100)*18.518))                                                 
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()  
        SCREEN.blit(imp, ((Width/100)*46.875, (Height/100)*18.518))                                                 
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        SCREEN.blit(resized_bg8, (0, 0))
        pygame.mixer.music.stop()
        pygame.mixer.music.load("songus/prenescasu.wav")
        pygame.mixer.music.play(loops=0)
        file_name = "vid/prenescasu.mp4"
        window_name = "window"
        interframe_wait_ms = 60
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
        s114()                                                                                      
def s114():
    while True:
        pygame.mixer.music.load("songus/songusamogusdruhus.wav")
        pygame.mixer.music.load("songus/songusamongus.wav")
        pygame.mixer.music.play(loops=-1)
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(resized_bg8, (0, 0))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONC
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083,(Height/100)*18.518 ))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*20.83, (Height/100)*15.740))                                                
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        SCREEN.blit(resized_bg8, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                              
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*15.740))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*20.83, (Height/100)*18.518))                                                   
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        SCREEN.blit(resized_bg8, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                             
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB
        DALSI_BUTTON                                               
        DALSI_BUTTON.update(SCREEN)
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083,(Height/100)*18.518 ))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*20.83, (Height/100)*18.518))   
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        SCREEN.blit(resized_bg8, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                             
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*15.740))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*20.83, (Height/100)*18.518))                                                    
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        SCREEN.blit(resized_bg8, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                            
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONC
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083,(Height/100)*18.518 ))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*20.83, (Height/100)*15.740))                                                  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        SCREEN.blit(resized_bg8, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                            
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*15.740))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*20.83, (Height/100)*18.518))                                                  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        SCREEN.blit(resized_bg8, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                             
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN
        SAKON1_BUTTON
        SAKON2_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083,(Height/100)*18.518 ))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*20.83, (Height/100)*18.518))                                                    
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        SCREEN.blit(resized_bg8, (0, 0))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB                                                 
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        SCREEN.blit(resized_bg8, (0, 0))                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN                                               
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        imp = pygame.image.load('postavy/Nekolas.png').convert()
        SCREEN.blit(imp, ((Width/100)*46.875, (Height/100)*18.518))    
        sakondd2() 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()   
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    pbdole()                                                                          
        pygame.display.update()
def pbdole():
    while True:
        pygame.mixer.music.stop()
        pygame.mixer.music.load("songus/lacrimosa.wav")
        pygame.mixer.music.play(loops=0)    
        file_name = "vid/pbdole.mp4"
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
        sakon3()
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
        SCREEN.blit(resized_bg8, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                            
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB
        DALSI_BUTTON                                              
        DALSI_BUTTON.update(SCREEN)
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083,(Height/100)*18.518 ))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*20.83, (Height/100)*18.518))   
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        SCREEN.blit(resized_bg8, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                              
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONC
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083,(Height/100)*18.518 ))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*20.83, (Height/100)*15.740))                                                  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        SCREEN.blit(resized_bg8, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                             
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*15.740))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*20.83, (Height/100)*18.518))                                                 
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        SCREEN.blit(resized_bg8, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                             
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*15.740))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*20.83, (Height/100)*18.518))                                                  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        SCREEN.blit(resized_bg8, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN
        DALSI_BUTTON
        imp = pygame.image.load('postavy/Nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, ((Width/100)*52.083, (Height/100)*15.740))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*20.83, (Height/100)*18.518))                                                   
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
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
        PLAY_MOUSE_POS = pygame.mouse.get_pos();SCREEN.fill("black");SCREEN.blit(resized_ls, (0, 0));f = open("save2.txt", "w");f.close()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();sys.exit()
            s126()
        pygame.display.update()
        sleep(5)
        pygame.mixer.stop()
        pygame.mixer.music.load("songus/lounytheme.wav")
        pygame.mixer.music.play(loops=-1)
def s126():
    while True:
        SCREEN.blit(resized_bg9, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONC
        DALSI_BUTTON
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*31.25,(Height/100)*18.518))                                                  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONC.update(SCREEN) 
        t126()                                                                                       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s127()                                                                                    
        pygame.display.update()
def s127():
    while True:
        SCREEN.blit(resized_bg9, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN
        DALSI_BUTTON
        imp2 = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*31.25,(Height/100)*18.518))                                                  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN) 
        t127()                                                                                       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s128()                                                                                    
        pygame.display.update()
def s128():
    while True:
        SCREEN.blit(resized_bg9, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONŠ
        DALSI_BUTTON
        imp2 = pygame.image.load('postavy/prozatimnistepan.png').convert()                                                           #štěpán
        SCREEN.blit(imp2, ((Width/100)*31.25,(Height/100)*18.518))                                                  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONŠ.update(SCREEN) 
        t128()                                                                                       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s129()                                                                                    
        pygame.display.update()
def s129():
    while True:
        SCREEN.blit(resized_bg9, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                              
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONPB
        DALSI_BUTTON                                             
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DALSI_BUTTON.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONPB.update(SCREEN) 
        t129()                                                                                      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()   
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s130()                                                                          
        pygame.display.update()
def s130():
    while True:
        SCREEN.blit(resized_bg9, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONC
        DALSI_BUTTON
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*31.25,(Height/100)*18.518))                                                  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONC.update(SCREEN) 
        t130()                                                                                       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s131()                                                                                    
        pygame.display.update()
def s131():
    while True:
        SCREEN.blit(resized_bg9, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                               
        PLAY_BACK   
        DOKNO_BUTTON
        MOKNO_BUTTONN
        DALSI_BUTTON
        imp2 = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*33.85416, (Height/100)*18.518))                                                  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN) 
        t131()                                                                                       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s132()                                                                                    
        pygame.display.update()
def s132():
    while True:
        SCREEN.blit(resized_bg9, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                               
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONPB;DALSI_BUTTON                                             
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DALSI_BUTTON.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONPB.update(SCREEN) 
        t132()                                                                                      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()   
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s133()                                                                          
        pygame.display.update()
def s133():
    while True:
        SCREEN.blit(resized_bg9, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                               
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONN;DALSI_BUTTON
        imp2 = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*33.85416, (Height/100)*18.518))                                                  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN) 
        t133()                                                                                       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s134()                                                                                    
        pygame.display.update()
def s134():
    while True:
        SCREEN.blit(resized_bg9, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                               
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONŠ;DALSI_BUTTON
        imp2 = pygame.image.load('postavy/prozatimnistepan.png').convert()                                                           #ŠTĚPÁN
        SCREEN.blit(imp2, ((Width/100)*31.25,(Height/100)*18.518))                                                  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONŠ.update(SCREEN) 
        t134()                                                                                       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s135()                                                                                    
        pygame.display.update()
def s135():
    while True:
        SCREEN.blit(resized_bg9, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                              
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONPB;DALSI_BUTTON                                               
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DALSI_BUTTON.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONPB.update(SCREEN) 
        t135()                                                                                      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()   
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s136()                                                                          
        pygame.display.update()
def s136():
    while True:
        SCREEN.blit(resized_bg9, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                               
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONN;DALSI_BUTTON
        imp2 = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*33.85416, (Height/100)*18.518))                                                  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN) 
        t136()                                                                                       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s137()                                                                                    
        pygame.display.update()
def s137():
    while True:
        SCREEN.blit(resized_bg9, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                               
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONC;DALSI_BUTTON
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*31.25,(Height/100)*18.518))                                                  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONC.update(SCREEN) 
        t137()                                                                                       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s138()                                                                                    
        pygame.display.update()
def s138():
    while True:
        SCREEN.blit(resized_bg9, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                               
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONŠ;DALSI_BUTTON
        imp2 = pygame.image.load('postavy/prozatimnistepan.png').convert()                                                           #ŠTĚPÁN
        SCREEN.blit(imp2, ((Width/100)*31.25,(Height/100)*18.518))                                                  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONŠ.update(SCREEN) 
        t138()                                                                                       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s139()                                                                                    
        pygame.display.update()
def s139():
    while True:
        SCREEN.blit(resized_bg9, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                               
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONN;DALSI_BUTTON
        imp2 = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*33.85416, (Height/100)*18.518))                                                  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN) 
        t139()                                                                                       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s140()                                                                                    
        pygame.display.update()
def s140():
    while True:
        SCREEN.blit(resized_bg9, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()                                                                               
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONŠ;DALSI_BUTTON
        imp2 = pygame.image.load('postavy/prozatimnistepan.png').convert()                                                           #ŠTĚPÁN
        SCREEN.blit(imp2, ((Width/100)*31.25,(Height/100)*18.518))                                                  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONŠ.update(SCREEN) 
        busak()                                                                                       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s140()                                                                                    
        pygame.display.update()
def busak():
    while True:
        SCREEN.blit(resized_bg9, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK;DOKNO_BUTTON
        VYB_BUTTONB =Button(image=(resized_vyberbutton), pos=((Width/100)*21.875, (Height/100)*55.55), 
                                        text_input="BILLA", font=font_vyber, base_color="White", hovering_color="#4e61de")
        VYB_BUTTONT =Button(image=(resized_vyberbutton), pos=((Width/100)*48.9583,(Height/100)*55.55), 
                                        text_input="Tyršák", font=font_vyber, base_color="White", hovering_color="#4e61de")
        VYB_BUTTONK =Button(image=(resized_vyberbutton), pos=((Width/100)*76.0416,(Height/100)*55.55), 
                                        text_input="Kostel", font=font_vyber, base_color="White", hovering_color="#4e61de")
        VYB_BUTTONB.changeColor(PLAY_MOUSE_POS)
        VYB_BUTTONT.changeColor(PLAY_MOUSE_POS)
        VYB_BUTTONK.changeColor(PLAY_MOUSE_POS)
        VYB_BUTTONB.update(SCREEN)
        VYB_BUTTONT.update(SCREEN)
        VYB_BUTTONK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        dia1 = font.render(b1,True,"Black") ;SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        dia2 = font.render(b2,True,"Black") ;SCREEN.blit(dia2,((Width/100)*14.322916,(Height/100)*76.851851851852))
        dia3 = font.render(b3,True,"Black") ;SCREEN.blit(dia3,((Width/100)*14.322916,(Height/100)*80.55))
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        POMOC()
                    if VYB_BUTTONB.checkForInput(PLAY_MOUSE_POS):
                        billa()  
                    if VYB_BUTTONT.checkForInput(PLAY_MOUSE_POS):
                        tyrsak()  
                    if VYB_BUTTONK.checkForInput(PLAY_MOUSE_POS):
                        kostel() 
        pygame.display.update()
def tyrsak():
    while True:
        SCREEN.blit(resized_bg10, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK
        DOKNO_BUTTON
        VYB_BUTTONG =Button(image=(resized_vyberbutton), pos=((Width/100)*21.875,(Height/100)*55.55), 
                                        text_input="Gympl", font=font_vyber, base_color="White", hovering_color="#4e61de")
        VYB_BUTTONS =Button(image=(resized_vyberbutton), pos=((Width/100)*48.9583,(Height/100)*55.55), 
                                        text_input="Autobusák", font=font_vyber, base_color="White", hovering_color="#4e61de")
        VYB_BUTTONP =Button(image=(resized_vyberbutton), pos=((Width/100)*76.0416,(Height/100)*55.55), 
                                        text_input="Pramen", font=font_vyber, base_color="White", hovering_color="#4e61de")
        VYB_BUTTONG.changeColor(PLAY_MOUSE_POS)
        VYB_BUTTONP.changeColor(PLAY_MOUSE_POS)
        VYB_BUTTONS.changeColor(PLAY_MOUSE_POS)
        VYB_BUTTONG.update(SCREEN)
        VYB_BUTTONP.update(SCREEN)
        VYB_BUTTONS.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        dia1 = font.render(ty1,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        dia2 = font.render(ty2,True,"Black");SCREEN.blit(dia2,((Width/100)*14.322916,(Height/100)*76.851851851852))
        dia3=font.render(ty3,True,"Black");SCREEN.blit(dia3,((Width/100)*14.322916,(Height/100)*80.55))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if VYB_BUTTONG.checkForInput(PLAY_MOUSE_POS):
                    gympl()  
                if VYB_BUTTONP.checkForInput(PLAY_MOUSE_POS):
                    pramen()  
                if VYB_BUTTONS.checkForInput(PLAY_MOUSE_POS):
                    busak()
        pygame.display.update() 
def gympl():
    while True:
        SCREEN.blit(resized_bg11, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK
        DOKNO_BUTTON
        VYB_BUTTONM =Button(image=(resized_vyberbutton), pos=((Width/100)*21.875,(Height/100)*55.55), 
                                        text_input="Město", font=font_vyber, base_color="White", hovering_color="#4e61de")
        VYB_BUTTONM.changeColor(PLAY_MOUSE_POS)
        VYB_BUTTONM.update(SCREEN)
        VYB_BUTTONT =Button(image=(resized_vyberbutton), pos=((Width/100)*76.0416,(Height/100)*55.55), 
                                        text_input="Tyršák", font=font_vyber, base_color="White", hovering_color="#4e61de")
        VYB_BUTTONT.changeColor(PLAY_MOUSE_POS)
        VYB_BUTTONT.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        dia1 = font.render(g1,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        dia2 = font.render(g2,True,"Black");SCREEN.blit(dia2,((Width/100)*14.322916,(Height/100)*76.851851851852))
        dia3=font.render(g3,True,"Black");SCREEN.blit(dia3,((Width/100)*14.322916,(Height/100)*80.55))
        dia4=font.render(g4,True,"Black");SCREEN.blit(dia4,((Width/100)*14.322916,(Height/100)*84.259))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if VYB_BUTTONM.checkForInput(PLAY_MOUSE_POS):
                    mesto()  
                if VYB_BUTTONT.checkForInput(PLAY_MOUSE_POS):
                    tyrsak()  
        pygame.display.update()
def kostel():
        pygame.mixer.music.stop()
        pygame.mixer.music.load("songus/khudba.wav")
        pygame.mixer.music.play(loops=1)
        while True:
            SCREEN.blit(resized_bg13, (0, 0))
            PLAY_MOUSE_POS = pygame.mouse.get_pos()
            PLAY_BACK
            DOKNO_BUTTON
            VYB_BUTTONA =Button(image=(resized_vyberbutton), pos=((Width/100)*48.9583,(Height/100)*55.55), 
                                            text_input="Amerika", font=font_vyber, base_color="White", hovering_color="#4e61de")
            VYB_BUTTONA.changeColor(PLAY_MOUSE_POS)
            VYB_BUTTONA.update(SCREEN)
            DOKNO_BUTTON.update(SCREEN)
            PLAY_BACK.changeColor(PLAY_MOUSE_POS)
            PLAY_BACK.update(SCREEN)
            dia1 = font.render(kmore,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
            dia2 = font.render(kfunguj,True,"Black");SCREEN.blit(dia2,((Width/100)*14.322916,(Height/100)*76.851851851852))
            dia3=font.render(k3,True,"Black");SCREEN.blit(dia3,((Width/100)*14.322916,(Height/100)*80.55))
            dia4=font.render(k4,True,"Black");SCREEN.blit(dia4,((Width/100)*14.322916,(Height/100)*84.259))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        POMOC()
                    if VYB_BUTTONA.checkForInput(PLAY_MOUSE_POS):
                        amerika()  
            pygame.display.update()
def mesto():
    while True:
        SCREEN.blit(resized_bg16, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK
        DOKNO_BUTTON= Button(image=(resized_mctyri), pos=((Width/100)*40.625,(Height/100)*46.296), 
                            text_input="", font=font_meno, base_color="White", hovering_color="Green")
        VYB_BUTTONZ =Button(image=(resized_vyberbutton), pos=((Width/100)*21.875,(Height/100)*55.55), 
                                        text_input="Základka", font=font_vyber, base_color="White", hovering_color="#4e61de")
        VYB_BUTTONPO =Button(image=(resized_vyberbutton), pos=((Width/100)*48.9583,(Height/100)*55.55), 
                                        text_input="Podšance", font=font_vyber, base_color="White", hovering_color="#4e61de")
        VYB_BUTTONG =Button(image=(resized_vyberbutton), pos=((Width/100)*76.0416,(Height/100)*55.55), 
                                        text_input="Gympl", font=font_vyber, base_color="White", hovering_color="#4e61de")
        VYB_BUTTONG.changeColor(PLAY_MOUSE_POS)
        VYB_BUTTONZ.changeColor(PLAY_MOUSE_POS)
        VYB_BUTTONPO.changeColor(PLAY_MOUSE_POS)
        VYB_BUTTONG.update(SCREEN)
        VYB_BUTTONZ.update(SCREEN)
        VYB_BUTTONPO.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        dia1 = font.render(m1,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        dia2 = font.render(m2,True,"Black");SCREEN.blit(dia2,((Width/100)*14.322916,(Height/100)*76.851851851852))
        dia3=font.render(m3,True,"Black");SCREEN.blit(dia3,((Width/100)*14.322916,(Height/100)*80.55))
        dia4=font.render(m4,True,"Black");SCREEN.blit(dia4,((Width/100)*14.322916,(Height/100)*84.259))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if VYB_BUTTONG.checkForInput(PLAY_MOUSE_POS):
                    gympl()  
                if VYB_BUTTONPO.checkForInput(PLAY_MOUSE_POS):
                    podsance()  
                if VYB_BUTTONZ.checkForInput(PLAY_MOUSE_POS):
                    zakladka() 
        pygame.display.update()
def billa():
    while True:
        SCREEN.blit(resized_bg12, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK
        DOKNO_BUTTON
        VYB_BUTTONM =Button(image=(resized_vyberbutton), pos=((Width/100)*21.875,(Height/100)*55.55), 
                                        text_input="Město", font=font_vyber, base_color="White", hovering_color="#4e61de")
        VYB_BUTTONK =Button(image=(resized_vyberbutton), pos=((Width/100)*76.0416,(Height/100)*55.55), 
                                        text_input="Kostel", font=font_vyber, base_color="White", hovering_color="#4e61de")
        VYB_BUTTONA =Button(image=(resized_vyberbutton), pos=((Width/100)*48.9583,(Height/100)*55.55), 
                                        text_input="Autobusák", font=font_vyber, base_color="White", hovering_color="#4e61de")
        VYB_BUTTONM.changeColor(PLAY_MOUSE_POS)
        VYB_BUTTONK.changeColor(PLAY_MOUSE_POS)
        VYB_BUTTONM.update(SCREEN)
        VYB_BUTTONK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        VYB_BUTTONA.changeColor(PLAY_MOUSE_POS)
        VYB_BUTTONA.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        dia1=font.render(bi1,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        dia2=font.render(bi2,True,"Black");SCREEN.blit(dia2,((Width/100)*14.322916,(Height/100)*76.851851851852))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if VYB_BUTTONM.checkForInput(PLAY_MOUSE_POS):
                    mesto()  
                if VYB_BUTTONK.checkForInput(PLAY_MOUSE_POS):
                    kostel()  
                if VYB_BUTTONA.checkForInput(PLAY_MOUSE_POS):
                    busak()  
        pygame.display.update()
def pramen():
    while True:
        SCREEN.blit(resized_bg14, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK
        DOKNO_BUTTON= Button(image=(resized_mtri), pos=((Width/100)*40.625,(Height/100)*46.296), 
                            text_input="", font=font_meno, base_color="White", hovering_color="Green")
        VYB_BUTTONZP =Button(image=(resized_vyberbutton), pos=((Width/100)*21.875,(Height/100)*55.55), 
                                        text_input="Zpět", font=font_vyber, base_color="White", hovering_color="#4e61de")
        VYB_BUTTONAP =Button(image=(resized_vyberbutton), pos=((Width/100)*76.0416,(Height/100)*55.55), 
                                        text_input="Napít se", font=font_vyber, base_color="White", hovering_color="#4e61de")
        VYB_BUTTONZP.changeColor(PLAY_MOUSE_POS)
        VYB_BUTTONAP.changeColor(PLAY_MOUSE_POS)
        VYB_BUTTONAP.update(SCREEN)
        VYB_BUTTONZP.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        dia1=font.render(p1,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        dia3=font.render(p3,True,"Black");SCREEN.blit(dia3,(275,830))
        dia4=font.render(p4,True,"Black");SCREEN.blit(dia4,(275,870))
        dia5=font.render(p5,True,"Black");SCREEN.blit(dia5,((Width/100)*14.322916,(Height/100)*84.259))
        dia6=font.render(p6,True,"Black");SCREEN.blit(dia6,(275,950))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if VYB_BUTTONZP.checkForInput(PLAY_MOUSE_POS):
                    tyrsak()  
                if VYB_BUTTONAP.checkForInput(PLAY_MOUSE_POS):
                    dedp()
        pygame.display.update()
def amerika():
    pygame.mixer.music.stop()
    pygame.mixer.music.load("songus/lounytheme.wav")
    pygame.mixer.music.play(loops=-1)
    while True:
        SCREEN.blit(resized_bg18, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK
        DOKNO_BUTTON= Button(image=(resized_mctyri), pos=((Width/100)*40.625,(Height/100)*46.296), 
                            text_input="", font=font_meno, base_color="White", hovering_color="Green")
        VYB_BUTTONAL =Button(image=(resized_vyberbutton), pos=((Width/100)*21.875,(Height/100)*55.55), 
                                        text_input="Levá", font=font_vyber, base_color="White", hovering_color="#4e61de")
        VYB_BUTTONAP =Button(image=(resized_vyberbutton), pos=((Width/100)*76.0416,(Height/100)*55.55), 
                                        text_input="Pravá", font=font_vyber, base_color="White", hovering_color="#4e61de")
        VYB_BUTTONAL.changeColor(PLAY_MOUSE_POS)
        VYB_BUTTONAP.changeColor(PLAY_MOUSE_POS)
        VYB_BUTTONAP.update(SCREEN)
        VYB_BUTTONAL.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        dia1 = font.render(a1,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        dia2 = font.render(a2,True,"Black");SCREEN.blit(dia2,((Width/100)*14.322916,(Height/100)*76.851851851852))
        dia3 = font.render(a3,True,"Black");SCREEN.blit(dia3,((Width/100)*14.322916,(Height/100)*80.55))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if VYB_BUTTONAL.checkForInput(PLAY_MOUSE_POS):
                    mesto()
                if VYB_BUTTONAP.checkForInput(PLAY_MOUSE_POS):
                    deda()
        pygame.display.update()
def zakladka():
    while True:
        SCREEN.blit(resized_bg15, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK
        DOKNO_BUTTON= Button(image=(resized_mctyri), pos=((Width/100)*40.625,(Height/100)*46.296), 
                            text_input="", font=font_meno, base_color="White", hovering_color="Green")
        VYB_BUTTONKOP =Button(image=(resized_vyberbutton), pos=((Width/100)*21.875,(Height/100)*55.55), 
                                        text_input="Kopeček", font=font_vyber, base_color="White", hovering_color="#4e61de")
        VYB_BUTTONPA =Button(image=(resized_vyberbutton), pos=((Width/100)*76.0416,(Height/100)*55.55), 
                                        text_input="Park", font=font_vyber, base_color="White", hovering_color="#4e61de")
        VYB_BUTTONKOP.changeColor(PLAY_MOUSE_POS)
        VYB_BUTTONKOP.update(SCREEN)
        VYB_BUTTONPA.changeColor(PLAY_MOUSE_POS)
        VYB_BUTTONPA.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        dia1=font.render(z1,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        dia2=font.render(z2,True,"Black");SCREEN.blit(dia2,((Width/100)*14.322916,(Height/100)*76.851851851852))
        dia3=font.render(z3,True,"Black");SCREEN.blit(dia3,((Width/100)*14.322916,(Height/100)*80.55))
        dia4=font.render(z4,True,"Black");SCREEN.blit(dia4,((Width/100)*14.322916,(Height/100)*84.259))
        dia5=font.render(z5,True,"Black");SCREEN.blit(dia5,((Width/100)*14.322916, (Height/100)*87.962))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if VYB_BUTTONKOP.checkForInput(PLAY_MOUSE_POS):
                    kopecek()  
                if VYB_BUTTONPA.checkForInput(PLAY_MOUSE_POS):
                    park() 
        pygame.display.update()
def kopecek():
    while True:
        SCREEN.blit(resized_bg19, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK
        DOKNO_BUTTON
        VYB_BUTTONS =Button(image=(resized_vyberbutton), pos=((Width/100)*48.9583,(Height/100)*55.55), 
                                        text_input="Sakon", font=font_vyber, base_color="White", hovering_color="#4e61de")
        VYB_BUTTONS.changeColor(PLAY_MOUSE_POS)
        VYB_BUTTONS.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        dia1 = font.render(ko1,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        dia2 = font.render(ko2,True,"Black");SCREEN.blit(dia2,((Width/100)*14.322916,(Height/100)*76.851851851852))
        dia3 = font.render(ko3,True,"Black");SCREEN.blit(dia3,((Width/100)*14.322916,(Height/100)*80.55))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if VYB_BUTTONS.checkForInput(PLAY_MOUSE_POS):
                    sakon()
        pygame.display.update()
def podsance():
        while True:
            SCREEN.blit(resized_bg20, (0, 0))
            PLAY_MOUSE_POS = pygame.mouse.get_pos()
            PLAY_BACK
            DOKNO_BUTTON= Button(image=(resized_mctyri), pos=((Width/100)*40.625,(Height/100)*46.296), 
                            text_input="", font=font_meno, base_color="White", hovering_color="Green")
            VYB_BUTTONG =Button(image=(resized_vyberbutton), pos=((Width/100)*21.875,(Height/100)*55.55), 
                                            text_input="Park", font=font_vyber, base_color="White", hovering_color="#4e61de")
            VYB_BUTTONS =Button(image=(resized_vyberbutton), pos=((Width/100)*48.9583,(Height/100)*55.55), 
                                            text_input="Město", font=font_vyber, base_color="White", hovering_color="#4e61de")
            VYB_BUTTONP =Button(image=(resized_vyberbutton), pos=((Width/100)*76.0416,(Height/100)*55.55), 
                                            text_input="Amerika", font=font_vyber, base_color="White", hovering_color="#4e61de")
            VYB_BUTTONG.changeColor(PLAY_MOUSE_POS)
            VYB_BUTTONP.changeColor(PLAY_MOUSE_POS)
            VYB_BUTTONS.changeColor(PLAY_MOUSE_POS)
            VYB_BUTTONG.update(SCREEN)
            VYB_BUTTONP.update(SCREEN)
            VYB_BUTTONS.update(SCREEN)
            DOKNO_BUTTON.update(SCREEN)
            PLAY_BACK.changeColor(PLAY_MOUSE_POS)
            PLAY_BACK.update(SCREEN)
            dia1 = font.render(po1,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
            dia2 = font.render(po2,True,"Black");SCREEN.blit(dia2,((Width/100)*14.322916,(Height/100)*76.851851851852))
            dia3=font.render(po3,True,"Black");SCREEN.blit(dia3,((Width/100)*14.322916,(Height/100)*80.55))
            dia4=font.render(po4,True,"Black");SCREEN.blit(dia4,((Width/100)*14.322916,(Height/100)*84.259))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        POMOC()
                    if VYB_BUTTONG.checkForInput(PLAY_MOUSE_POS):
                        park()  
                    if VYB_BUTTONP.checkForInput(PLAY_MOUSE_POS):
                        amerika()  
                    if VYB_BUTTONS.checkForInput(PLAY_MOUSE_POS):
                        mesto()
            pygame.display.update()
def park():
    while True:
        SCREEN.blit(resized_bg21, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK
        DOKNO_BUTTON
        VYB_BUTTONPO =Button(image=(resized_vyberbutton), pos=((Width/100)*21.875,(Height/100)*55.55), 
                                        text_input="Podšance", font=font_vyber, base_color="White", hovering_color="#4e61de")
        VYB_BUTTONM =Button(image=(resized_vyberbutton), pos=((Width/100)*76.0416,(Height/100)*55.55), 
                                        text_input="Město", font=font_vyber, base_color="White", hovering_color="#4e61de")
        VYB_BUTTONZ =Button(image=(resized_vyberbutton), pos=((Width/100)*48.9583,(Height/100)*55.55), 
                                        text_input="Základka", font=font_vyber, base_color="White", hovering_color="#4e61de")
        VYB_BUTTONPO.changeColor(PLAY_MOUSE_POS)
        VYB_BUTTONM.changeColor(PLAY_MOUSE_POS)
        VYB_BUTTONPO.update(SCREEN)
        VYB_BUTTONM.update(SCREEN)
        VYB_BUTTONZ.changeColor(PLAY_MOUSE_POS)
        VYB_BUTTONZ.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        dia1=font.render(pa1,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        dia2=font.render(pa2,True,"Black");SCREEN.blit(dia2,((Width/100)*14.322916,(Height/100)*76.851851851852))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if VYB_BUTTONPO.checkForInput(PLAY_MOUSE_POS):
                    podsance()  
                if VYB_BUTTONM.checkForInput(PLAY_MOUSE_POS):
                    mesto()  
                if VYB_BUTTONZ.checkForInput(PLAY_MOUSE_POS):
                    zakladka()
        pygame.display.update()
def deda():
    while True:
        SCREEN.fill("Black")
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        DALSI_BUTTON
        DALSI_BUTTON.update(SCREEN)
        dia1=font.render(da,True,"White");SCREEN.blit(dia1,((Width/100)*23.9583,(Height/100)*50))
        dia2=font.render(da2,True,"White");SCREEN.blit(dia2,((Width/100)*23.9583,(Height/100)*53.703))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    sls2()
        pygame.display.update()
def dedp():
    while True:
        SCREEN.fill("Black")
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        DALSI_BUTTON
        DALSI_BUTTON.update(SCREEN)
        dia1=font.render(dp,True,"White");SCREEN.blit(dia1,((Width/100)*23.9583,(Height/100)*50))
        dia2=font.render(dp2,True,"White");SCREEN.blit(dia2,((Width/100)*23.9583,(Height/100)*53.703))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    sls2()
        pygame.display.update()
def sakon():
    while True:
        SCREEN.blit(resized_bg17, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONS;DALSI_BUTTON
        imp3 = pygame.image.load('postavy/strom.png').convert_alpha()                                                        #ŠTĚPÁN
        SCREEN.blit(imp3, ((Width/100)*52.083, (Height/100)*13.88))                                                  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONS.update(SCREEN)
        dia1 = font.render(d141,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s142()
        pygame.display.update()
def s142():
    while True:
        SCREEN.blit(resized_bg17, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONN;DALSI_BUTTON
        imp1 = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp1, ((Width/100)*32.8125, (Height/100)*15.740))
        imp3 = pygame.image.load('postavy/strom.png').convert_alpha()                                                           
        SCREEN.blit(imp3, ((Width/100)*52.083, (Height/100)*15.740))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*5.2083,(Height/100)*18.518)) 
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        dia1 = font.render(d142,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s143()
        pygame.display.update()
def s143():
    while True:
        SCREEN.blit(resized_bg17, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONN;DALSI_BUTTON
        imp1 = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp1, ((Width/100)*32.8125, (Height/100)*15.740))
        imp3 = pygame.image.load('postavy/strom.png').convert_alpha()                                                           
        SCREEN.blit(imp3, ((Width/100)*52.083, (Height/100)*15.740))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*5.2083,(Height/100)*18.518))  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        dia1 = font.render(d143,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s144()
        pygame.display.update()
def s144():
    while True:
        SCREEN.blit(resized_bg17, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONS;DALSI_BUTTON
        imp1 = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp1, ((Width/100)*32.8125,(Height/100)*18.518))
        imp3 = pygame.image.load('postavy/strom.png').convert_alpha()                                                           
        SCREEN.blit(imp3, ((Width/100)*52.083, (Height/100)*13.88))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*5.2083,(Height/100)*18.518))  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONS.update(SCREEN)
        dia1 = font.render(d144,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s145()
        pygame.display.update()
def s145():
    while True:
        SCREEN.blit(resized_bg17, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONS;DALSI_BUTTON
        imp1 = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp1, ((Width/100)*32.8125,(Height/100)*18.518))
        imp3 = pygame.image.load('postavy/strom.png').convert_alpha()                                                           
        SCREEN.blit(imp3, ((Width/100)*52.083, (Height/100)*13.88))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*5.2083,(Height/100)*18.518))  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONS.update(SCREEN)
        dia1 = font.render(d145,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s146()
        pygame.display.update()
def s146():
    while True:
        SCREEN.blit(resized_bg17, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONPB;DALSI_BUTTON
        imp1 = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp1, ((Width/100)*32.8125,(Height/100)*18.518))
        imp3 = pygame.image.load('postavy/strom.png').convert_alpha()                                                           
        SCREEN.blit(imp3, ((Width/100)*52.083, (Height/100)*15.740))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*5.2083,(Height/100)*18.518))  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONPB.update(SCREEN)
        dia1 = font.render(d146,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s147()
        pygame.display.update()
def s147():
    while True:
        SCREEN.blit(resized_bg17, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONC;DALSI_BUTTON
        imp1 = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp1, ((Width/100)*32.8125,(Height/100)*18.518))
        imp3 = pygame.image.load('postavy/strom.png').convert_alpha()                                                           
        SCREEN.blit(imp3, ((Width/100)*52.083, (Height/100)*15.740))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, (100, 170)) 
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONC.update(SCREEN)
        dia1 = font.render(d147,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s148()
        pygame.display.update()
def s148():
    while True:
        SCREEN.blit(resized_bg17, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONN;DALSI_BUTTON
        imp1 = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp1, ((Width/100)*32.8125, (Height/100)*15.740))
        imp3 = pygame.image.load('postavy/strom.png').convert_alpha()                                                           
        SCREEN.blit(imp3, ((Width/100)*52.083, (Height/100)*15.740))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*5.2083,(Height/100)*18.518))  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        dia1 = font.render(d148,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s149()
        pygame.display.update()
def s149():
    while True:
        SCREEN.blit(resized_bg17, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONS;DALSI_BUTTON
        imp1 = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp1, ((Width/100)*32.8125,(Height/100)*18.518))
        imp3 = pygame.image.load('postavy/strom.png').convert_alpha()                                                           
        SCREEN.blit(imp3, ((Width/100)*52.083, (Height/100)*13.88))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*5.2083,(Height/100)*18.518))  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONS.update(SCREEN)
        dia1 = font.render(d149,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s150()
        pygame.display.update()
def s150():
    while True:
        SCREEN.blit(resized_bg17, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONK;DALSI_BUTTON
        imp1 = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp1, ((Width/100)*32.8125,(Height/100)*18.518))
        imp3 = pygame.image.load('postavy/strom.png').convert_alpha()                                                           
        SCREEN.blit(imp3, ((Width/100)*52.083, (Height/100)*15.740))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*5.2083,(Height/100)*18.518))  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONK.update(SCREEN)
        dia1 = font.render(d150,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s151()
        pygame.display.update()
def s151():
    while True:
        SCREEN.blit(resized_bg17, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONS;DALSI_BUTTON
        imp1 = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp1, ((Width/100)*32.8125,(Height/100)*18.518))
        imp3 = pygame.image.load('postavy/strom.png').convert_alpha()                                                           
        SCREEN.blit(imp3, ((Width/100)*52.083, (Height/100)*13.88))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*5.2083,(Height/100)*18.518))  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONS.update(SCREEN)
        dia1 = font.render(d151,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s152()
        pygame.display.update()
def s152():
    while True:
        SCREEN.blit(resized_bg17, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONC;DALSI_BUTTON
        imp1 = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp1, ((Width/100)*32.8125,(Height/100)*18.518))
        imp3 = pygame.image.load('postavy/strom.png').convert_alpha()                                                           
        SCREEN.blit(imp3, ((Width/100)*52.083, (Height/100)*15.740))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, (100, 170)) 
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONC.update(SCREEN)
        dia1 = font.render(d152,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s153()
        pygame.display.update()
def s153():
    while True:
        SCREEN.blit(resized_bg17, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONN;DALSI_BUTTON
        imp1 = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp1, ((Width/100)*32.8125, (Height/100)*15.740))
        imp3 = pygame.image.load('postavy/strom.png').convert_alpha()                                                           
        SCREEN.blit(imp3, ((Width/100)*52.083, (Height/100)*15.740))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*5.2083,(Height/100)*18.518))  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        dia1 = font.render(d153,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s154()
        pygame.display.update()
def s154():
    while True:
        SCREEN.blit(resized_bg17, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONN;DALSI_BUTTON
        imp1 = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp1, ((Width/100)*32.8125, (Height/100)*15.740))
        imp3 = pygame.image.load('postavy/strom.png').convert_alpha()                                                           
        SCREEN.blit(imp3, ((Width/100)*52.083, (Height/100)*15.740))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*5.2083,(Height/100)*18.518))  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        dia1 = font.render(d154,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s155()
        pygame.display.update()
def s155():
    while True:
        SCREEN.blit(resized_bg17, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONS;DALSI_BUTTON
        imp1 = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp1, ((Width/100)*32.8125,(Height/100)*18.518))
        imp3 = pygame.image.load('postavy/strom.png').convert_alpha()                                                           
        SCREEN.blit(imp3, ((Width/100)*52.083, (Height/100)*13.88))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*5.2083,(Height/100)*18.518))  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONS.update(SCREEN)
        dia1 = font.render(d155,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s156()
        pygame.display.update()
def s156():
    while True:
        SCREEN.blit(resized_bg17, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONC;DALSI_BUTTON
        imp1 = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp1, ((Width/100)*32.8125,(Height/100)*18.518))
        imp3 = pygame.image.load('postavy/strom.png').convert_alpha()                                                           
        SCREEN.blit(imp3, ((Width/100)*52.083, (Height/100)*15.740))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, (100, 170)) 
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONC.update(SCREEN)
        dia1 = font.render(d156,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s157()
        pygame.display.update()
def s157():
    while True:
        SCREEN.blit(resized_bg17, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONPB;DALSI_BUTTON
        imp1 = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp1, ((Width/100)*32.8125,(Height/100)*18.518))
        imp3 = pygame.image.load('postavy/strom.png').convert_alpha()                                                           
        SCREEN.blit(imp3, ((Width/100)*52.083, (Height/100)*15.740))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*5.2083,(Height/100)*18.518))  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONPB.update(SCREEN)
        dia1 = font.render(d157,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s158()
        pygame.display.update()
def s158():
    while True:
        SCREEN.blit(resized_bg17, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONK;DALSI_BUTTON
        imp1 = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp1, ((Width/100)*32.8125,(Height/100)*18.518))
        imp3 = pygame.image.load('postavy/strom.png').convert_alpha()                                                           
        SCREEN.blit(imp3, ((Width/100)*52.083, (Height/100)*15.740))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*5.2083,(Height/100)*18.518))  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONK.update(SCREEN)
        dia1 = font.render(d158,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        dia2 = font.render(d158b,True,"Black");SCREEN.blit(dia2,((Width/100)*14.322916,(Height/100)*76.851851851852))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s159()
        pygame.display.update()
def s159():
    while True:
        SCREEN.blit(resized_bg17, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONK;DALSI_BUTTON
        imp1 = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp1, ((Width/100)*32.8125,(Height/100)*18.518))
        imp3 = pygame.image.load('postavy/strom.png').convert_alpha()                                                           
        SCREEN.blit(imp3, ((Width/100)*52.083, (Height/100)*15.740))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*5.2083,(Height/100)*18.518))  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONK.update(SCREEN)
        dia1 = font.render(d159,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s160()
        pygame.display.update()
def s160():
    while True:
        SCREEN.blit(resized_bg17, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONN;DALSI_BUTTON
        imp1 = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp1, ((Width/100)*32.8125, (Height/100)*15.740))
        imp3 = pygame.image.load('postavy/strom.png').convert_alpha()                                                           
        SCREEN.blit(imp3, ((Width/100)*52.083, (Height/100)*15.740))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*5.2083,(Height/100)*18.518))  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        dia1 = font.render(d160,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s161()
        pygame.display.update()
def s161():
    while True:
        SCREEN.blit(resized_bg17, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONPB;DALSI_BUTTON
        imp1 = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp1, ((Width/100)*32.8125,(Height/100)*18.518))
        imp3 = pygame.image.load('postavy/strom.png').convert_alpha()                                                           
        SCREEN.blit(imp3, ((Width/100)*52.083, (Height/100)*15.740))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*5.2083,(Height/100)*18.518))  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONPB.update(SCREEN)
        dia1 = font.render(d161,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s162()
        pygame.display.update()
def s162():
    while True:
        SCREEN.blit(resized_bg17, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONK;DALSI_BUTTON
        imp1 = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp1, ((Width/100)*32.8125,(Height/100)*18.518))
        imp3 = pygame.image.load('postavy/strom.png').convert_alpha()                                                           
        SCREEN.blit(imp3, ((Width/100)*52.083, (Height/100)*15.740))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*5.2083,(Height/100)*18.518))  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONK.update(SCREEN)
        dia1 = font.render(d162,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s163()
        pygame.display.update()
def s163():
    while True:
        SCREEN.blit(resized_bg17, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONPB;DALSI_BUTTON
        imp1 = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp1, ((Width/100)*32.8125,(Height/100)*18.518))
        imp3 = pygame.image.load('postavy/strom.png').convert_alpha()                                                           
        SCREEN.blit(imp3, ((Width/100)*52.083, (Height/100)*15.740))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*5.2083,(Height/100)*18.518))  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONPB.update(SCREEN)
        dia1 = font.render(d163,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s164()
        pygame.display.update()
def s164():
    while True:
        SCREEN.blit(resized_bg17, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONN;DALSI_BUTTON
        imp1 = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp1, ((Width/100)*32.8125, (Height/100)*15.740))
        imp3 = pygame.image.load('postavy/strom.png').convert_alpha()                                                           
        SCREEN.blit(imp3, ((Width/100)*52.083, (Height/100)*15.740))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*5.2083,(Height/100)*18.518))  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        dia1 = font.render(d164,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s165()
        pygame.display.update()
def s165():
    while True:
        SCREEN.blit(resized_bg17, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONC;DALSI_BUTTON
        imp1 = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp1, ((Width/100)*32.8125,(Height/100)*18.518))
        imp3 = pygame.image.load('postavy/strom.png').convert_alpha()                                                           
        SCREEN.blit(imp3, ((Width/100)*52.083, (Height/100)*15.740))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, (100, 170)) 
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONC.update(SCREEN)
        dia1 = font.render(d165,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s166()
        pygame.display.update()
def s166():
    while True:
        SCREEN.blit(resized_bg17, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONN;DALSI_BUTTON
        imp1 = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp1, ((Width/100)*32.8125, (Height/100)*15.740))
        imp3 = pygame.image.load('postavy/strom.png').convert_alpha()                                                           
        SCREEN.blit(imp3, ((Width/100)*52.083, (Height/100)*15.740))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*5.2083,(Height/100)*18.518))  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        dia1 = font.render(d166,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s167()
        pygame.display.update()
def s167():
    while True:
        SCREEN.blit(resized_bg17, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONPB;DALSI_BUTTON
        imp1 = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp1, ((Width/100)*32.8125,(Height/100)*18.518))
        imp3 = pygame.image.load('postavy/strom.png').convert_alpha()                                                           
        SCREEN.blit(imp3, ((Width/100)*52.083, (Height/100)*15.740))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*5.2083,(Height/100)*18.518))  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONC.update(SCREEN)
        dia1 = font.render(d167,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s168()
        pygame.display.update()
def s168():
    while True:
        SCREEN.blit(resized_bg17, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONN;DALSI_BUTTON
        imp1 = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp1, ((Width/100)*32.8125, (Height/100)*15.740))
        imp3 = pygame.image.load('postavy/strom.png').convert_alpha()                                                           
        SCREEN.blit(imp3, ((Width/100)*52.083, (Height/100)*15.740))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*5.2083,(Height/100)*18.518))  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONS.update(SCREEN)
        dia1 = font.render(d168,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s169()
        pygame.display.update()
def s169():
    while True:
        SCREEN.blit(resized_bg17, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONPB;DALSI_BUTTON
        imp1 = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp1, ((Width/100)*32.8125,(Height/100)*18.518))
        imp3 = pygame.image.load('postavy/strom.png').convert_alpha()                                                           
        SCREEN.blit(imp3, ((Width/100)*52.083, (Height/100)*15.740))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*5.2083,(Height/100)*18.518))  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        dia1 = font.render(d169,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s170()
        pygame.display.update()
def s170():
    while True:
        SCREEN.blit(resized_bg17, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONS;DALSI_BUTTON
        imp1 = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp1, ((Width/100)*32.8125,(Height/100)*18.518))
        imp3 = pygame.image.load('postavy/strom.png').convert_alpha()                                                           
        SCREEN.blit(imp3, ((Width/100)*52.083, (Height/100)*13.88))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*5.2083,(Height/100)*18.518))  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONPB.update(SCREEN)
        dia1 = font.render(d170,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s171()
        pygame.display.update()
def s171():
    while True:
        SCREEN.blit(resized_bg17, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONN;DALSI_BUTTON
        imp1 = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp1, ((Width/100)*32.8125, (Height/100)*15.740))
        imp3 = pygame.image.load('postavy/strom.png').convert_alpha()                                                           
        SCREEN.blit(imp3, ((Width/100)*52.083, (Height/100)*15.740))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*5.2083,(Height/100)*18.518))  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONS.update(SCREEN)
        dia1 = font.render(d171,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s171()
        pygame.display.update()
def s172():
    while True:
        SCREEN.blit(resized_bg17, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONN;DALSI_BUTTON
        imp1 = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp1, ((Width/100)*32.8125, (Height/100)*15.740))
        imp3 = pygame.image.load('postavy/strom.png').convert_alpha()                                                           
        SCREEN.blit(imp3, ((Width/100)*52.083, (Height/100)*15.740))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*5.2083,(Height/100)*18.518))  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        dia1 = font.render(d172,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s171()
        pygame.display.update()
def s173():
    while True:
        SCREEN.blit(resized_bg17, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONN;DALSI_BUTTON
        imp1 = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp1, ((Width/100)*32.8125, (Height/100)*15.740))
        imp3 = pygame.image.load('postavy/strom.png').convert_alpha()                                                           
        SCREEN.blit(imp3, ((Width/100)*52.083, (Height/100)*15.740))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*5.2083,(Height/100)*18.518))  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONC.update(SCREEN)
        dia1 = font.render(d173,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s171()
        pygame.display.update()
def s174():
    while True:
        SCREEN.blit(resized_bg17, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONN;DALSI_BUTTON
        imp1 = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp1, ((Width/100)*32.8125, (Height/100)*15.740))
        imp3 = pygame.image.load('postavy/strom.png').convert_alpha()                                                           
        SCREEN.blit(imp3, ((Width/100)*52.083, (Height/100)*15.740))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*5.2083,(Height/100)*18.518))  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONS.update(SCREEN)
        dia1 = font.render(d174,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s171()
        pygame.display.update()
def s175():
    while True:
        SCREEN.blit(resized_bg17, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONN;DALSI_BUTTON
        imp1 = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp1, ((Width/100)*32.8125, (Height/100)*15.740))
        imp3 = pygame.image.load('postavy/strom.png').convert_alpha()                                                           
        SCREEN.blit(imp3, ((Width/100)*52.083, (Height/100)*15.740))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*5.2083,(Height/100)*18.518))  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        dia1 = font.render(d175,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s171()
        pygame.display.update()
def s176():
    while True:
        SCREEN.blit(resized_bg17, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONN;DALSI_BUTTON
        imp1 = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp1, ((Width/100)*32.8125, (Height/100)*15.740))
        imp3 = pygame.image.load('postavy/strom.png').convert_alpha()                                                           
        SCREEN.blit(imp3, ((Width/100)*52.083, (Height/100)*15.740))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*5.2083,(Height/100)*18.518))  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        dia1 = font.render(d176,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s171()
        pygame.display.update()
def s177():
    while True:
        SCREEN.blit(resized_bg17, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONN;DALSI_BUTTON
        imp1 = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp1, ((Width/100)*32.8125, (Height/100)*15.740))
        imp3 = pygame.image.load('postavy/strom.png').convert_alpha()                                                           
        SCREEN.blit(imp3, ((Width/100)*52.083, (Height/100)*15.740))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*5.2083,(Height/100)*18.518))  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONPB.update(SCREEN)
        dia1 = font.render(d177,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s171()
        pygame.display.update()
def s178():
    while True:
        SCREEN.blit(resized_bg17, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONN;DALSI_BUTTON
        imp1 = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp1, ((Width/100)*32.8125, (Height/100)*15.740))
        imp3 = pygame.image.load('postavy/strom.png').convert_alpha()                                                           
        SCREEN.blit(imp3, ((Width/100)*52.083, (Height/100)*15.740))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*5.2083,(Height/100)*18.518))  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONC.update(SCREEN)
        dia1 = font.render(d178,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s171()
        pygame.display.update()
def s179():
    while True:
        SCREEN.blit(resized_bg17, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK;DOKNO_BUTTON;MOKNO_BUTTONN;DALSI_BUTTON
        imp1 = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp1, ((Width/100)*32.8125, (Height/100)*15.740))
        imp3 = pygame.image.load('postavy/strom.png').convert_alpha()                                                           
        SCREEN.blit(imp3, ((Width/100)*52.083, (Height/100)*15.740))
        imp2 = pygame.image.load('postavy/cednik.png').convert()                                                           #postava  
        SCREEN.blit(imp2, ((Width/100)*5.2083,(Height/100)*18.518))  
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTONN.update(SCREEN)
        dia1 = font.render(d179,True,"Black");SCREEN.blit(dia1,((Width/100)*14.322916,(Height/100)*73.148))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    POMOC()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s171()
        pygame.display.update()

def sls3():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos();SCREEN.fill("black");SCREEN.blit(resized_ls, (0, 0));f = open("save3.txt", "w");f.close()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();sys.exit()
            s179()
        pygame.display.update()
        sleep(5)

def ses():
    pygame.mixer.music.stop()
    pygame.mixer.music.load("songus/finger.wav")
    pygame.mixer.music.play(loops=0)
#def buttonu v menu
xpb=Width/100;xsb=Height*100;ypb=Height/100;yob=Height/100;yqb=Height/100;ysb=Height/100;ypob=Height/100
PLAY_BUTTON = Button(image=pygame.image.load("asety/startus.png"), pos=(xpb*91.18, ypb*27.8), 
                                    text_input="Nová hra", font=font_vyber, base_color="#732c06", hovering_color="White")
OPTIONS_BUTTON = Button(image=pygame.image.load("asety/nastus.png"), pos=(xpb*91.18, yob*64.82), 
                                    text_input="Nastavení", font=font_vyber, base_color="#732c06", hovering_color="White")
QUIT_BUTTON = Button(image=pygame.image.load("asety/koncus.png"), pos=(xpb*91.18,  yqb*83.34 ), 
                                    text_input="Konec", font=font_vyber, base_color="#732c06", hovering_color="White")
SES_BUTTON = Button(image=pygame.image.load("asety/ses.png"), pos=(xsb*37.239583, ysb*10.8), 
                                    text_input="", font=font_vyber, base_color="#732c06", hovering_color="White")
POK_BUTTON = Button(image=pygame.image.load("asety/pokus.png"), pos=(xpb*91.18, ypob*46.3), 
                                    text_input="Pokračovat", font=font_vyber, base_color="#732c06", hovering_color="White")
def POMOC():
    pygame.mixer.music.load("songus/songusamogusdruhus.wav")
    pygame.mixer.music.load("songus/songusamongus.wav")
    pygame.mixer.music.play(loops=-1)
    save1 = os.path.exists("save1.txt")
    save2=os.path.exists("save2.txt")
    save3=os.path.exists("save3.txt")
    if save3:
        def main_menu4():
            while True:
                SCREEN.blit(resized_BG, (0, 0))
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
                            sls3()
                pygame.display.update()
        main_menu4()
    if save2:
        def main_menu3():
            while True:
                SCREEN.blit(resized_BG, (0, 0))
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
                SCREEN.blit(resized_BG, (0, 0))
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
                SCREEN.blit(resized_BG, (0, 0))
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
