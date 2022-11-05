from asyncio import sleep
import pygame, sys
import time
import pygame


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
S1 = pygame.image.load("asety/s1.png")
S2 =pygame.image.load("asety/s2.png")
S3 =pygame.image.load("asety/krab1.png")
S4 =pygame.image.load("asety/krab2.png")

"""""
tutorijal pro kreteni
VSUDE KDE JE ZAVYNAC JE PROSTE TAM JAKO DEJ TO NO JAKO NOVY CISLO NEBO JA NEVIM NAZEF
nejdrif udelat novy d@
potom 
def pbd@():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d(tvojecislo),True,"Black")
    SCREEN.blit(dia1,(275,790))
a pak
def s1d@():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(S2, (0, -3))                                                                                     TO JE POZADI ASI??
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")    TO ZŮSTANE STEJNÍ
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="@", font=get_font(30), base_color="White", hovering_color="White")      TO JE MÉNO
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(1500, 900), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")      TO JE JAKO DALSI
        imp = pygame.image.load('@').convert()                                                                OBRAZEK POSTAVY TO ZMEN VOLE
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        pbd@()                                                                                                TO ZMEN TAKI
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s1d@()                                                                                     TO TAKY LINA SVINE
        pygame.display.update()
"""
#Hudba
#pygame.mixer.music.load("songus/songusamongus.mp3")
#pygame.mixer.music.load("songus/songusamogusdruhus.mp3")
#pygame.mixer.music.play(-1)
#pygame.mixer.music.queue("songus/songusamogusdruhus.mp3")
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
d1="Konečně jsem se přestěhoval po čtvrté sérii do České Republiky."
d2 = "Lýdije měla pravdu, je tu hodně feťáků, navíc v tomto městě."
d3= "No teď jen rozbalit a začít vařit."
d4 ="Jen je problém, že není nikdo kdo by to prodával."
d5 = "Něco se hejbe v krabici"
d6 = "Pane Bílý váš krystalický met je bomba."
d7 = "Co jsi sakra zač?"
d8 = "Já jsem ten kdo neklepe."
d9 = "Co si to myslíš? Propašovat se mou krabicí do mého auta."
d10 ="Vy znáte chemii, a já znám Ústí."
d11 = "Kdo tě za mnou poslal? Co máš za účel?"
d12= "Nejsem proti vám, chci vám pomoct."
d13= "Zdá se, že víš kdo jsem. Odkud víš kdo jsem?"
d14= "Já vím hodně věcí, bohužel až moc."
d15= "Odedneška budeme vařit krystalický met."
d16= "Takže ty chceš, aby jsme byli partneři."
d17 ="chápu to dobře?"
d18 ="V tomto drsném městě sami nepřežijete,"
d18x2="budete potřebovat mou pomoc."
d19= "Nejsi tedy, od DEA? Nebo v utajení?"
d20= "V utajení jsem, ale s policií ne."
d21= "Policie o mě nic neví a ani nikdy nebude."
d22= "Ještě jedna věc, proč máš na hlavě kočičí uši?"
d23 ="Toto je Ústí nad Labem, zde je možné vše."
def test_text():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render("Tak, to je poslední krabice.",True,"Black")
    SCREEN.blit(dia1,(275,790))
def pbd1():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d1,True,"Black")
    SCREEN.blit(dia1,(275,790))
def pbd1l1():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia4 = font.render(d2,True,"Black")
    SCREEN.blit(dia4,(275,830))
def pbd2():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d3,True,"Black")
    SCREEN.blit(dia1,(275,790))
def pbd3():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d4,True,"Black")
    SCREEN.blit(dia1,(275,790))
def pbd4():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d5,True,"Black")
    SCREEN.blit(dia1,(275,790))
def nd1():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d6,True,"Black")
    SCREEN.blit(dia1,(275,790))
def pbd5():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d7,True,"Black")
    SCREEN.blit(dia1,(275,790))
def nd2():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d8,True,"Black")
    SCREEN.blit(dia1,(275,790))
def pbd6():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d9,True,"Black")
    SCREEN.blit(dia1,(275,790))
def nd3():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d10,True,"Black")
    SCREEN.blit(dia1,(275,790))
def pbd7():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d11,True,"Black")
    SCREEN.blit(dia1,(275,790))
def nd3():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d12,True,"Black")
    SCREEN.blit(dia1,(275,790))
    pygame.display.flip()
def pbd8():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d13,True,"Black")
    SCREEN.blit(dia1,(275,790))
    pygame.display.flip()
def nd4():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d14,True,"Black")
    SCREEN.blit(dia1,(275,790))
    pygame.display.flip()
def pbd9():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d15,True,"Black")
    SCREEN.blit(dia1,(275,790))
    pygame.display.flip()
def nd5():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d16,True,"Black")
    SCREEN.blit(dia1,(275,790))
    pygame.display.flip()
def pbd10():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d17,True,"Black")
    SCREEN.blit(dia1,(275,790))
    pygame.display.flip()
def nd6():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d18,True,"Black")
    SCREEN.blit(dia1,(275,790))
def nd6l2():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia3 = font.render(d18x2,True,"Black")
    SCREEN.blit(dia3,(275,830))
def pbd11():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d19,True,"Black")
    SCREEN.blit(dia1,(275,790))
    pygame.display.flip()
def nd7():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d20,True,"Black")
    SCREEN.blit(dia1,(275,790))
    pygame.display.flip()
def pbd12():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d21,True,"Black")
    SCREEN.blit(dia1,(275,790))
def nd8():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d22,True,"Black")
    SCREEN.blit(dia1,(275,790))
def pbd13():
    font =  pygame.font.Font("asety/fontus.ttf", 32)
    dia1 = font.render(d23,True,"Black")
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
    
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        #pygame.mixer.music.stop()
        #pygame.mixer.music.load("songus/usti.mp3")
        #pygame.mixer.music.play(loops=-1)
        SCREEN.fill("black")
        SCREEN.blit(S1, (0, -3))

        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(1500, 900), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s1d1()
        pygame.display.update()
        #skoušim vymyslet aby se zastavilo to psaní protože je to v while True , je to display flipem
        #animacefunkcni()
        #taklhle můžu dát text na obrazovku bez hoven
        test_text()





    pygame.display.update()
#scéna 1    
def s1d1():
       while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        SCREEN.blit(S1, (0, -3))

        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725), 
                            text_input="Pan Bílý", font=get_font(30), base_color="White", hovering_color="White")
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(1500, 900), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")
                        
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s1d3()
        pbd1()
        pbd1l1()
        pygame.display.update()
def s1d2():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        SCREEN.blit(S1, (0, -3))

        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Pan Bílý", font=get_font(30), base_color="White", hovering_color="White")
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(1500, 900), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")
        imp = pygame.image.load('asety/ja.png').convert()
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s1d2()
        pbd2()
        pygame.display.update()
def s1d3():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        SCREEN.blit(S1, (0, -3))

        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"),pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Pan Bílý", font=get_font(30), base_color="White", hovering_color="White")
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(1500, 900), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s1d4()
        pbd3()
        pygame.display.update()
def s1d4():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        SCREEN.blit(S3, (0, -3))

        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(1500, 900), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s1d5()
        
        pbd4()
        pygame.display.update()
def s1d5():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(S4, (0, -3))

        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(1500, 900), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s1d6()
        
        pygame.display.update()
def s1d6():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        SCREEN.blit(S4, (0, -3))
        #pygame.mixer.music.stop()
        #pygame.mixer.music.load("songus/songusamongus.mp3")
        #pygame.mixer.music.play(loops=-1)
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Nekolas", font=get_font(30), base_color="White", hovering_color="White")
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(1500, 900), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")
        imp = pygame.image.load('asety/ja.png').convert()
        SCREEN.blit(imp, (700,200))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s1d7()
        
        nd1()
        pygame.display.update()
def s1d7():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        SCREEN.blit(S2, (0, -3))

        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"),pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Pan Bílý", font=get_font(30), base_color="White", hovering_color="White")
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(1500, 900), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")
        imp = pygame.image.load('asety/ja.png').convert()
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s1d8()
        
        pbd5()
        pygame.display.update()
def s1d8():
    while True:
        zmackunti = 0
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        font =  pygame.font.Font("asety/fontus.ttf", 32)
        SCREEN.fill("black")
        SCREEN.blit(S2, (0, -3))
        dia1 = font.render(d9,False,"Black")
        SCREEN.blit(dia1,(275,790))
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Nekolas", font=get_font(30), base_color="White", hovering_color="White")
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(1500, 900), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")
        imp = pygame.image.load('asety/ja.png').convert()
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        nd2()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s1d9()


        
        pygame.display.update()
def s1d9():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(S2, (0, -3))
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Pan Bílý", font=get_font(30), base_color="White", hovering_color="White")
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(1500, 900), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")
        imp = pygame.image.load('asety/ja.png').convert()
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        pbd6()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s1d10()


        
        pygame.display.update()
def s1d10():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(S2, (0, -3))
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Nekolas", font=get_font(30), base_color="White", hovering_color="White")
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(1500, 900), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")
        imp = pygame.image.load('asety/ja.png').convert()
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        nd3()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s1d11()


        
        pygame.display.update()
def s1d11():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(S2, (0, -3))
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Pan Bílý", font=get_font(30), base_color="White", hovering_color="White")
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(1500, 900), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")
        imp = pygame.image.load('asety/ja.png').convert()
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        pbd8()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s1d12()


        
        pygame.display.update()
def s1d12():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(S2, (0, -3))
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Nekolas", font=get_font(30), base_color="White", hovering_color="White")
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(1500, 900), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")
        imp = pygame.image.load('asety/ja.png').convert()
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        nd4()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s1d13()


        
        pygame.display.update()
def s1d13():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(S2, (0, -3))
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Nekolas", font=get_font(30), base_color="White", hovering_color="White")
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(1500, 900), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")
        imp = pygame.image.load('asety/ja.png').convert()
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        pbd9()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s1d14()


        
        pygame.display.update()
def s1d14():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(S2, (0, -3))
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Pan Bílý", font=get_font(30), base_color="White", hovering_color="White")
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(1500, 900), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")
        imp = pygame.image.load('asety/ja.png').convert()
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        nd5()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s1d15()


        
        pygame.display.update()
def s1d15():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(S2, (0, -3))
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Pan Bílý", font=get_font(30), base_color="White", hovering_color="White")
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(1500, 900), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")
        imp = pygame.image.load('asety/ja.png').convert()
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        pbd10()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s1d16()


        
        pygame.display.update()
def s1d16():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(S2, (0, -3))
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Nekolas", font=get_font(30), base_color="White", hovering_color="White")
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(1500, 900), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")
        imp = pygame.image.load('asety/ja.png').convert()
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        nd6()
        nd6l2()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s1d17()


        
        pygame.display.update()
def s1d17():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(S2, (0, -3))
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Pan Bílý", font=get_font(30), base_color="White", hovering_color="White")
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(1500, 900), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")
        imp = pygame.image.load('asety/ja.png').convert()
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        pbd11()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s1d18()


        
        pygame.display.update()
def s1d18():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(S2, (0, -3))
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Nekolas", font=get_font(30), base_color="White", hovering_color="White")
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(1500, 900), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")
        imp = pygame.image.load('asety/ja.png').convert()
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        nd7()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s1d19()


        
        pygame.display.update()
def s1d19():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(S2, (0, -3))
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Nekolas", font=get_font(30), base_color="White", hovering_color="White")
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(1500, 900), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")
        imp = pygame.image.load('asety/ja.png').convert()
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        pbd12()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s1d20()


        
        pygame.display.update()
def s1d20():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(S2, (0, -3))
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Pan Bílý", font=get_font(30), base_color="White", hovering_color="White")
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(1500, 900), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")
        imp = pygame.image.load('asety/ja.png').convert()
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        nd8()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s1d21()


        
        pygame.display.update()
def s1d21():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        SCREEN.blit(S2, (0, -3))
        PLAY_BACK = Button(image=None, pos=(1750, 50), 
                            text_input="Hlavní Menu", font=get_font(40), base_color="White", hovering_color="Green")
        DOKNO_BUTTON = Button(image=pygame.image.load("asety/mdva.png"), pos=(780, 500), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="Green")
        MOKNO_BUTTON= Button(image=None, pos=(425, 725),
                            text_input="Nekolas", font=get_font(30), base_color="White", hovering_color="White")
        DALSI_BUTTON= Button(image=pygame.image.load("asety/dalsi.png"), pos=(1500, 900), 
                            text_input="", font=get_font(30), base_color="White", hovering_color="White")
        imp = pygame.image.load('asety/ja.png').convert()
        SCREEN.blit(imp, (1000, 300))
        DALSI_BUTTON.update(SCREEN)
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        DOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        DOKNO_BUTTON.update(SCREEN)
        MOKNO_BUTTON.changeColor(PLAY_MOUSE_POS)
        MOKNO_BUTTON.update(SCREEN)
        pbd13()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if DALSI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    s1d21()


        
        pygame.display.update()








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


        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
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

        pygame.display.update()

main_menu()
