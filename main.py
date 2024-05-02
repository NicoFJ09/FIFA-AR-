import pygame
import serial
import sys
sys.path.append('../')
from var_consts import *


#==================================================== GAME SETUP ==================================

pygame.init()
pygame.display.set_caption("FIFA LIVE ACTION")
screen = pygame.display.set_mode((HWIDTH,HHEIGHT))
screen.fill(white)
clock = pygame.time.Clock()


#==================================================== SCREEN IMPORTS =============================
from Screens.home import home_screen
from Screens.start import start_screen
#==================================================== ASSET IMPORTS ==============================

Hbackground = pygame.transform.scale(pygame.image.load("Assets/Backgrounds/Home_BG.png").convert_alpha(), (HWIDTH,HHEIGHT))
GTITLE =  pygame.transform.scale(pygame.image.load("Assets/Sprites/CE_SOCCER.png").convert_alpha(), (4*HWIDTH/5, HHEIGHT/10))
Hfont = pygame.font.Font("Assets/Font/PressStart2P.ttf",30)

#=================================================== CHECK RASPBERRY PI DETECTION =================

def open_serial_port(port):
    try:
        Rpi = serial.Serial(port=port, baudrate=115200)
        print("Conectado")
        return Rpi
    except Exception:
        return None

def translate(Rpi):
    try:
        READ = Rpi.readline() # Esto se recibe en bytes.
        TRANSLATED = READ.decode('UTF-8') # Conversión de Byte a String
        print(TRANSLATED)
    except Exception:
        pass

Rpi = open_serial_port("COM7")

#====================================================== CONTROL MANAGEMENT ============================

def main():
    global selected_index, current_screen
    while RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if current_screen == "home" and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    selected_index = (selected_index - 1) % len(Home_options)
                    print("Currently selected option:", Home_options[selected_index])
                elif event.key == pygame.K_DOWN  or event.key == pygame.K_s:
                    selected_index = (selected_index + 1) % len(Home_options)
                    print("Currently selected option:", Home_options[selected_index])
                elif event.key == pygame.K_RETURN:
                    current_screen = Home_options[selected_index]
                    print("Selected index:", Home_options[selected_index])
                    # Here you can return the selected index value

        # Render home screen outside the event loop
        if current_screen == "home":
            home_screen(screen, Hbackground, GTITLE, Hfont, HWIDTH, HHEIGHT, selected_index, Home_options)
        elif current_screen == "START":
            start_screen(screen, Hfont, HWIDTH, HHEIGHT)
        elif current_screen == "SETTINGS":
            None
        elif current_screen == "GAME INFO":
            None
        elif current_screen == "ABOUT":
            None
        # Update and fps tick
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
   main()
