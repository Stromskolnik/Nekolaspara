from time import sleep
import pygame, sys
import time
import pygame
import cv2
import numpy as np

pygame.init()
SCREEN = pygame.display.set_mode((1920, 1080))
#nastavení hudby
def hh():
    pygame.mixer.music.set_volume(1)
def nh():
    pygame.mixer.music.set_volume(0)
pygame.mixer.music.load("songus/songusamongus.mp3")
pygame.mixer.music.load("songus/songusamogusdruhus.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.queue("songus/songusamogusdruhus.mp3")
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
"""""
def s():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg, (0, -3))                                                                                #pozadi
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")   
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(960, 540), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        t()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s()                                                                                    
        pygame.display.update()
def tja():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(dja,True,"Black")
    SCREEN.blit(dia1,(275,790))       
"""
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

#texty
#max 56 pismen nevim nejak tak
d1="Tak, to je poslední krabice."
d2="Konečně jsem se přestěhoval po čtvrté sérii do České Republiky."
d3 = "Lýdije měla pravdu, je tu hodně feťáků, navíc v tomto městě."
d4= "No teď jen rozbalit a začít vařit."
d5 ="Jen je problém, že není nikdo kdo by to prodával."
d6 = "(Něco se hejbe v krabici)"
d7 = "Pane Bílý váš krystalický met je bomba."
d8 = "Co jsi sakra zač?"
d9 = "Já jsem ten kdo neklepe."
d10 = "Co si to myslíš? Propašovat se mou krabicí do mého auta."
d11 ="Vy znáte chemii, a já znám Ústí."
d12 = "Kdo tě za mnou poslal? Co máš za účel?"
d13= "Nejsem proti vám, chci vám pomoct."
d14= "Zdá se, že víš kdo jsem. Odkud víš kdo jsem?"
d15= "Já vím hodně věcí, bohužel až moc."
d16= "Odedneška budeme vařit krystalický met."
d17= "Takže ty chceš, aby jsme byli partneři."
d18 ="Chápu to dobře?"
d19 ="V tomto drsném městě sami nepřežijete."
d20="Budete potřebovat mou pomoc."
d21= "Nejsi tedy, od DEA? Nebo v utajení?"
d22= "V utajení jsem, ale s policií ne."
d23= "Policie o mě nic neví a ani nikdy nebude."
d24= "Co když tvou pomoc nechci?"
d25="Jak jsem říkal, beze mě tu nepřežijete."
d26="Nemáte zkušenost s českem ani dealováním."
d27="Stačí když budete se mnou vařit a já obstarám ostatní"
d28="Máš nějaký důvod proč mi chceš tak moc pomoct?"
d29="Vidím velký potenciál ve vašem produktu,"
d29b="vybral jste si správné město."
d30="Zde smažky neznají čistotu vašeho krystalu."
d31="Jen asi kolem šedesát procent čistoty," 
d31b="my společně dokážeme udělat stoprocentní."
d32="Ty si myslíš že společně uděláme STO% čistý perník?"
d33="Vařil jsi vůbec někdy?"
d34="Jo, ale moji chábři jsou neschopní."
d35="Zkoušel jsem vařit se třema."
d36="Jenom jeden z nich je alkoholik a kuřák" 
d36b="a dva kompletní idioti."
d37="Co mají znamenat vůbec ty uši na hlavě?"
d38 ="Toto je Ústí nad Labem, zde je možné vše."
#intor
d39="Prokaž mi že umíš opravdu vařit."
d40="Jak uděláme met, když nemáme efedrin a pseudoefedrin?"
d41="Vy to děláte redukční aminací fenylacetonu methylaminem."
d42="A jestli redukce není stereospecifická, jak můžeme vyrobit"
d42b="enantiospecifický čístý produkt?"
d43="Však stereospecifičnost neovlivňuje enantiospecifičnost."
d44="Dobře můžu ti věřit, tak se dejme do práce."
#varnavecer
d45="Šlo ti to skvěle, víš toho víc než.. Ale jak poznáme jak moc" #Pb
d45b="je to čistý?"                                                #Pb
d46="Nebojte znám na to specialistu. Zítra se za ním můžeme vydat."#N
d47="Dneska to stačilo."                                           #N
d48="Hele neznáš místo, kam bych mohl schovat karavan na noc?"     #Pb
d49="Hádám že půjdete přespat do nějakého hotelu. Když máte peníze"#N
d49b="z minulých vařeních."
d50="Co takhle kdyby jsi ho pohlídal ty?"                          #Pb
d51="Tak jo, karavan můžete nechat tady, a jít se vyspat do hotelu"#N
d52="Klíčky si nechám u sebe. Jestli tu zítra něco nebude je konec."#PB
d53="Nemějte obavy"                                                #N
#bgvecer
d54="Nejsem si furt jistý jestli mu mám věřit, zničehonic se objeví."
d54b="a chce se mnou vařit."
d55="Hej kámo nemáš pár korun na pučení?"                              #??
d56="Hmph jenom další žebrák."
d57="Hej mluvim s tebou, nemáš drobný?"
d58="A co by jsi s nima udělal? Koupíš si za to jen chlast. Za moje peníze."#Pb
d59="Tak jdi do prdele."                                            #??

#fotni
def t1():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d1,True,"Black")
    SCREEN.blit(dia1,(275,790))
def t2():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d2,True,"Black")
    SCREEN.blit(dia1,(275,790))
def t3():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d3,True,"Black")
    SCREEN.blit(dia1,(275,790))
def t4():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d4,True,"Black")
    SCREEN.blit(dia1,(275,790))
def t5():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d5,True,"Black")
    SCREEN.blit(dia1,(275,790))
def t6():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d6,True,"Black")
    SCREEN.blit(dia1,(275,790))

def t7():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d7,True,"Black")
    SCREEN.blit(dia1,(275,790))

def t8():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d8,True,"Black")
    SCREEN.blit(dia1,(275,790))

def t9():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d9,True,"Black")
    SCREEN.blit(dia1,(275,790))

def t10():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d10,True,"Black")
    SCREEN.blit(dia1,(275,790))

def t11():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d11,True,"Black")
    SCREEN.blit(dia1,(275,790))

def t12():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d12,True,"Black")
    SCREEN.blit(dia1,(275,790))

def t13():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d13,True,"Black")
    SCREEN.blit(dia1,(275,790))

def t14():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d14,True,"Black")
    SCREEN.blit(dia1,(275,790))

def t15():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d15,True,"Black")
    SCREEN.blit(dia1,(275,790))

def t16():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d16,True,"Black")
    SCREEN.blit(dia1,(275,790))

def t17():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d17,True,"Black")
    SCREEN.blit(dia1,(275,790))

def t18():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d18,True,"Black")
    SCREEN.blit(dia1,(275,790))

def t19():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d19,True,"Black")
    SCREEN.blit(dia1,(275,790))

def t20():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d20,True,"Black")
    SCREEN.blit(dia1,(275,790))
def t21():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d21,True,"Black")
    SCREEN.blit(dia1,(275,790))

def t22():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d22,True,"Black")
    SCREEN.blit(dia1,(275,790))

def t23():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d23,True,"Black")
    SCREEN.blit(dia1,(275,790))

def t24():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d24,True,"Black")
    SCREEN.blit(dia1,(275,790))

def t25():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d25,True,"Black")
    SCREEN.blit(dia1,(275,790))

def t26():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d26,True,"Black")
    SCREEN.blit(dia1,(275,790))

def t27():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d27,True,"Black")
    SCREEN.blit(dia1,(275,790))

def t28():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d28,True,"Black")
    SCREEN.blit(dia1,(275,790))

def t29():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d29,True,"Black")
    SCREEN.blit(dia1,(275,790))
def t29b():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d29b,True,"Black")
    SCREEN.blit(dia1,(275,830))

def t30():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d30,True,"Black")
    SCREEN.blit(dia1,(275,790))

def t31():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d31,True,"Black")
    SCREEN.blit(dia1,(275,790))
def t31b():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d31b,True,"Black")
    SCREEN.blit(dia1,(275,830))

def t32():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d32,True,"Black")
    SCREEN.blit(dia1,(275,790))

def t33():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d33,True,"Black")
    SCREEN.blit(dia1,(275,790))

def t34():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d34,True,"Black")
    SCREEN.blit(dia1,(275,790))

def t35():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d35,True,"Black")
    SCREEN.blit(dia1,(275,790))

def t36():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d36,True,"Black")
    SCREEN.blit(dia1,(275,790))
def t36b():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d36b,True,"Black")
    SCREEN.blit(dia1,(275,830))

def t37():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d37,True,"Black")
    SCREEN.blit(dia1,(275,790))

def t38():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d38,True,"Black")
    SCREEN.blit(dia1,(275,790))

def t39():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d39,True,"Black")
    SCREEN.blit(dia1,(275,790))

def t40():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d40,True,"Black")
    SCREEN.blit(dia1,(275,790))

def t41():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d41,True,"Black")
    SCREEN.blit(dia1,(275,790))

def t42():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d42,True,"Black")
    SCREEN.blit(dia1,(275,790))
def t42b():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d42b,True,"Black")
    SCREEN.blit(dia1,(275,830))    

def t43():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d43,True,"Black")
    SCREEN.blit(dia1,(275,790))

def t44():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d44,True,"Black")
    SCREEN.blit(dia1,(275,790))
def t45():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d45,True,"Black")
    SCREEN.blit(dia1,(275,790))
def t45b():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d45b,True,"Black")
    SCREEN.blit(dia1,(275,830))
def t46():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d46,True,"Black")
    SCREEN.blit(dia1,(275,790))
def t47():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d47,True,"Black")
    SCREEN.blit(dia1,(275,790))
def t48():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d48,True,"Black")
    SCREEN.blit(dia1,(275,790))
def t49():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d49,True,"Black")
    SCREEN.blit(dia1,(275,790))
def t49b():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d49b,True,"Black")
    SCREEN.blit(dia1,(275,790))
def t50():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d50,True,"Black")
    SCREEN.blit(dia1,(275,790))
def t51():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d51,True,"Black")
    SCREEN.blit(dia1,(275,790))
def t52():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d52,True,"Black")
    SCREEN.blit(dia1,(275,790))
def t53():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d53,True,"Black")
    SCREEN.blit(dia1,(275,790))
def t54():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d54,True,"Black")
    SCREEN.blit(dia1,(275,790))
def t55():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d55,True,"Black")
    SCREEN.blit(dia1,(275,790))
def t56():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d56,True,"Black")
    SCREEN.blit(dia1,(275,790))
def t57():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d57,True,"Black")
    SCREEN.blit(dia1,(275,790))
def t58():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d58,True,"Black")
    SCREEN.blit(dia1,(275,790))
def t59():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d59,True,"Black")
    SCREEN.blit(dia1,(275,790))




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









#semeny
def s1():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg1, (0, -3))                                                                                 
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")   
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Pan Bílý", font=get_font(30), base_color="White", hovering_color="White")     
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(960, 540), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")      
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        t1()                                                                                           
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s2()                                                                                    
        pygame.display.update()
def s2():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg1, (0, -3))                                                                               
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")   
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(960, 540), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        t2()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s3()                                                                                    
        pygame.display.update()
def s3():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg1, (0, -3))                                                                               
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")   
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(960, 540), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        t3()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s4()                                                                                    
        pygame.display.update()


def s4():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")   
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Pan Bílý", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(960, 540), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     

        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        t4()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s5()                                                                                    
        pygame.display.update()
def s5():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")   
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(960, 540), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     

        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        t5()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s6()                                                                                    
        pygame.display.update()
def s6():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")   
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(960, 540), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     

        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        t6()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
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
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")   
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Nekolas", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(960, 540), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        t7()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s8()                                                                                    
        pygame.display.update()
def s8():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")   
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Pan Bílý", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(960, 540), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        t8()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s9()                                                                                    
        pygame.display.update()
def s9():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")   
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Nekolas", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(960, 540), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        t9()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s10()                                                                                    
        pygame.display.update()
def s10():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")   
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Pan Bílý", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(960, 540), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        t10()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s11()                                                                                    
        pygame.display.update()
def s11():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")   
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Nekolas", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(960, 540), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        t11()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s12()                                                                                    
        pygame.display.update()
def s12():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")   
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Pan Bílý", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(960, 540), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        t12()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s13()                                                                                    
        pygame.display.update()
def s13():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")   
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Nekolas", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(960, 540), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        t13()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s14()                                                                                    
        pygame.display.update()
def s14():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")   
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Pan Bílý", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(960, 540), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        t14()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s15()                                                                                    
        pygame.display.update()
def s15():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")   
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Nekolas", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(960, 540), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        t15()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s16()                                                                                    
        pygame.display.update()
def s16():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")   
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Nekolas", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(960, 540), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        t16()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s17()                                                                                    
        pygame.display.update()
def s17():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")   
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Pan Bílý", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(960, 540), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        t17()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s18()                                                                                    
        pygame.display.update()
def s18():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")   
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Pan Bílý", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(960, 540), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        t18()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s19()                                                                                    
        pygame.display.update()
def s19():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")   
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Nekolas", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(960, 540), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        t19()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s20()                                                                                    
        pygame.display.update()
def s20():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")   
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Nekolas", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(960, 540), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        t20()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s21()                                                                                    
        pygame.display.update()
def s21():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")   
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Pan Bílý", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(960, 540), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        t21()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s22()                                                                                    
        pygame.display.update()
def s22():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")   
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Nekolas", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(960, 540), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        t22()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s23()                                                                                    
        pygame.display.update()
def s23():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")   
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Nekolas", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(960, 540), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        t23()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s24()                                                                                    
        pygame.display.update()
def s24():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")   
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Pan Bílý", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(960, 540), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        t24()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s25()                                                                                    
        pygame.display.update()
def s25():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")   
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Nekolas", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(960, 540), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        t25()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s26()                                                                                    
        pygame.display.update()
def s26():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")   
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Nekolas", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(960, 540), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        t26()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s27()                                                                                    
        pygame.display.update()
def s27():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")   
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Nekolas", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(960, 540), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        t27()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s28()                                                                                    
        pygame.display.update()
def s28():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")   
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Pan Bílý", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(960, 540), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        t28()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s29()                                                                                    
        pygame.display.update()
def s29():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")   
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Nekolas", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(960, 540), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        t29()
        t29b()                                                                                             
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s30()                                                                                    
        pygame.display.update()
def s30():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")   
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Nekolas", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(960, 540), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        t30()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s31()                                                                                    
        pygame.display.update()
def s31():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")   
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Nekolas", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(960, 540), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        t31()
        t31b()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s32()                                                                                    
        pygame.display.update()
def s32():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")   
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Pan Bílý", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(960, 540), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        t32()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s33()                                                                                    
        pygame.display.update()
def s33():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")   
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Pan Bílý", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(960, 540), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        t33()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s34()                                                                                    
        pygame.display.update()
def s34():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")   
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Nekolas", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(960, 540), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        t35()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s36()                                                                                    
        pygame.display.update()
def s36():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")   
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Nekolas", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(960, 540), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        t36()
        t36b()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s37()                                                                                    
        pygame.display.update()
def s37():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")   
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Pan Bílý", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(960, 540), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        t37()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s38()                                                                                    
        pygame.display.update()
def s38():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")   
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Nekolas", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(960, 540), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        t38()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s39()                                                                                    
        pygame.display.update()
def s39():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")   
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Pan Bílý", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(960, 540), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        t39()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s40()                                                                                    
        pygame.display.update()
def s40():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")   
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Pan Bílý", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(960, 540), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        t40()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s41()                                                                                    
        pygame.display.update()
def s41():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")   
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Nekolas", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(960, 540), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        t41()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s42()                                                                                    
        pygame.display.update()
def s42():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")   
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Pan Bílý", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(960, 540), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        t42()   
        t42b()                                                                                             
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s43()                                                                                    
        pygame.display.update()
def s43():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")   
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Nekolas", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(960, 540), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        t43()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s44()                                                                                    
        pygame.display.update()
def s44():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(bg2, (0, -3))                                                                               
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")   
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Pan Bílý", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(960, 540), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        t44()                                                                                                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    intro()                                                                                    
        pygame.display.update()

def intro():
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
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")   
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Pan Bílý", font=get_font(30), base_color="White", hovering_color="White")     #jmeno
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(960, 540), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")     
        imp = pygame.image.load('postavy/nekolas.png').convert()                                                           #postava  
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        t45() 
        t45b()                                                                                              
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s45()                                                                                    
        pygame.display.update()
 











def ses():
    pygame.mixer.music.load("songus/finger.mp3")
    pygame.mixer.music.play(loops=0)
    main_menu()




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


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(100).render("", True, "#732c06")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("asety/startus.png"), pos=(1750, 300), 
                            text_input="Nová hra", font=get_font(50), base_color="#732c06", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("asety/nastus.png"), pos=(1750, 500), 
                            text_input="Nastavení", font=get_font(50), base_color="#732c06", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("asety/koncus.png"), pos=(1750, 700), 
                            text_input="Konec", font=get_font(50), base_color="#732c06", hovering_color="White")
        SES_BUTTON = Button(image=pygame.image.load("asety/ses.png"), pos=(715, 153), 
                            text_input="", font=get_font(50), base_color="#732c06", hovering_color="White")


        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON, SES_BUTTON]:
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

        pygame.display.update()

main_menu()
