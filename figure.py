import pygame
import speech_recognition as sr
from settings import A1, A2, A3, A4, A5, A6, A7, A8, B1, B2,\
    B3, B4, B5, B6, B7, B8, C1, C2, C3, C4, C5, C6, C7, C8, D1,\
    D2, D3, D4, D5, D6, D7, D8, E1, E2, E3, E4, E5, E6, E7, E8,\
    F1, F2, F3, F4, F5, F6, F7, F8, G1, G2, G3, G4, G5, G6, G7,\
    G8, H1, H2, H3, H4, H5, H6, H7, H8
from speech_recognition import *
import pyttsx3
r = sr.Recognizer()
mic = sr.Microphone()
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)
sr.LANGUAGE = 'ru-RU'


class Figure(pygame.sprite.Sprite):
    def __init__(self, color, x, y, fType, image, groups):
        super().__init__(groups)
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.color = color
        self.x = x
        self.y = y
        self.type = fType
        self.rect = self.image.get_rect(topleft=(x, y))
    

    # def draw(self):
    #     pygame.draw.rect(self.image,(100,100,100),(0,0,50,50))
    # if rect.collidepoint(pygame.mouse.get_pos()):
    def move(self, events):
        for event in events:
            # if query == 'начало':
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                if self.type == 'чер_пешка1':
                    self.rect.x = 0
                    self.rect.y = 50
                    positionbpesk1 = A7
                    print(positionbpesk1)
                if self.type == 'чер_пешка2':
                    self.rect.x = 50
                    self.rect.y = 50
                    positionbpesk2 = B7
                    print(positionbpesk2)
                if self.type == 'чер_пешка3':
                    self.rect.x = 100
                    self.rect.y = 50
                    positionbpesk3 = C7
                    print(positionbpesk3)
                if self.type == 'чер_пешка4':
                    self.rect.x = 150
                    self.rect.y = 50
                    positionbpesk4 = D7
                    print(positionbpesk4)
                if self.type == 'чер_пешка5':
                    self.rect.x = 200
                    self.rect.y = 50
                    positionbpesk5 = E7
                    print(positionbpesk5)
                if self.type == 'чер_пешка6':
                    self.rect.x = 250
                    self.rect.y = 50
                    positionbpesk6 = F7
                    print(positionbpesk6)
                if self.type == 'чер_пешка7':
                    self.rect.x = 300
                    self.rect.y = 50
                    positionbpesk7 = G7
                    print(positionbpesk7)
                if self.type == 'чер_пешка8':
                    self.rect.x = 350
                    self.rect.y = 50
                    positionbpesk8 = H7
                    print(positionbpesk8)

                if self.type == 'бел_пешка1':
                    self.rect.x = 0
                    self.rect.y = 300
                    positionwpesk1 = A2
                    print(positionwpesk1)
                if self.type == 'бел_пешка2':
                    self.rect.x = 50
                    self.rect.y = 300
                    positionwpesk2 = B2
                    print(positionwpesk2)
                if self.type == 'бел_пешка3':
                    self.rect.x = 100
                    self.rect.y = 300
                    positionwpesk3 = C2
                    print(positionwpesk3)
                if self.type == 'бел_пешка4':
                    self.rect.x = 150
                    self.rect.y = 300
                    positionwpesk4 = D2
                    print(positionwpesk4)
                if self.type == 'бел_пешка5':
                    self.rect.x = 200
                    self.rect.y = 300
                    positionwpesk5 = E2
                    print(positionwpesk5)
                if self.type == 'бел_пешка6':
                    self.rect.x = 250
                    self.rect.y = 300
                    positionwpesk6 = F2
                    print(positionwpesk6)
                if self.type == 'бел_пешка7':
                    self.rect.x = 300
                    self.rect.y = 300
                    positionwpesk7 = G2
                    print(positionwpesk7)
                if self.type == 'бел_пешка8':
                    self.rect.x = 350
                    self.rect.y = 300
                    positionwpesk8 = H2
                    print(positionwpesk8)

                if self.type == 'чер_конь1':
                    self.rect.x = 50
                    self.rect.y = 0
                    positionbkon1 = B8
                    print(positionbkon1)
                if self.type == 'чер_конь2':
                    self.rect.x = 300
                    self.rect.y = 0
                    positionbkon2 = G8
                    print(positionbkon2)
                if self.type == 'чер_слон1':
                    self.rect.x = 100
                    self.rect.y = 0
                    positionbslon1 = C8
                    print(positionbslon1)
                if self.type == 'чер_слон2':
                    self.rect.x = 250
                    self.rect.y = 0
                    positionbslon2 = F8
                    print(positionbslon2)
                if self.type == 'чер_ладья1':
                    self.rect.x = 0
                    self.rect.y = 0
                    positionblad1 = A8
                    print(positionblad1)
                if self.type == 'чер_ладья2':
                    self.rect.x = 350
                    self.rect.y = 0
                    positionblad2 = H8
                    print(positionblad2)
                if self.type == 'чер_королева1':
                    self.rect.x = 200
                    self.rect.y = 0
                    positionbkor = E8
                    print(positionbkor)
                if self.type == 'чер_король2':
                    self.rect.x = 150
                    self.rect.y = 0
                    positionbk = D8
                    print(positionbk)

                if self.type == 'бел_конь1':
                    self.rect.x = 50
                    self.rect.y = 350
                    positionwkon1 = B1
                    print(positionwkon1)
                if self.type == 'бел_конь2':
                    self.rect.x = 300
                    self.rect.y = 350
                    positionwkon2 = G1
                    print(positionwkon2)
                if self.type == 'бел_слон1':
                    self.rect.x = 100
                    self.rect.y = 350
                    positionwslon2 = C1
                    print(positionwslon2)
                if self.type == 'бел_слон2':
                    self.rect.x = 250
                    self.rect.y = 350
                    positionwslon1 = F1
                    print(positionwslon1)
                if self.type == 'бел_ладья1':
                    self.rect.x = 0
                    self.rect.y = 350
                    positionwlad1 = A1
                    print(positionwlad1)
                if self.type == 'бел_ладья2':
                    self.rect.x = 350
                    self.rect.y = 350
                    positionwlad2 = H1
                    print(positionwlad2)
                if self.type == 'бел_королева1':
                    self.rect.x = 200
                    self.rect.y = 350
                    positionwkor = E1
                    print(positionwkor)
                if self.type == 'бел_король2':
                    self.rect.x = 150
                    self.rect.y = 350
                    positionwk = [[self.rect.x],[self.rect.y]]
                    print(positionwk)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    engine.say('Говорите')
                    engine.runAndWait()
                    with mic as source:
                        r.adjust_for_ambient_noise(source)
                        print('Запись пошла...')
                        audio = r.listen(source)
                    text = r.recognize_google(audio, language='ru-RU')
                    print(f"{text}")
                    command = [word.split() for word in text.split()]
                    print(command)
                    if text == 'старт':
                        if self.type == 'чер_пешка1':
                            self.rect.x = 0
                            self.rect.y = 50
                            print('pressed')
                        if self.type == 'чер_пешка2':
                            self.rect.x = 50
                            self.rect.y = 50
                            print('pressed')
                        if self.type == 'чер_пешка3':
                            self.rect.x = 100
                            self.rect.y = 50
                            print('pressed')
                        if self.type == 'чер_пешка4':
                            self.rect.x = 150
                            self.rect.y = 50
                            print('pressed')
                        if self.type == 'чер_пешка5':
                            self.rect.x = 200
                            self.rect.y = 50
                            print('pressed')
                        if self.type == 'чер_пешка6':
                            self.rect.x = 250
                            self.rect.y = 50
                            print('pressed')
                        if self.type == 'чер_пешка7':
                            self.rect.x = 300
                            self.rect.y = 50
                            print('pressed')
                        if self.type == 'чер_пешка8':
                            self.rect.x = 350
                            self.rect.y = 50
                            print('pressed')

                        if self.type == 'бел_пешка1':
                            self.rect.x = 0
                            self.rect.y = 300
                            print('pressed')
                        if self.type == 'бел_пешка2':
                            self.rect.x = 50
                            self.rect.y = 300
                            print('pressed')
                        if self.type == 'бел_пешка3':
                            self.rect.x = 100
                            self.rect.y = 300
                            print('pressed')
                        if self.type == 'бел_пешка4':
                            self.rect.x = 150
                            self.rect.y = 300
                            print('pressed')
                        if self.type == 'бел_пешка5':
                            self.rect.x = 200
                            self.rect.y = 300
                            print('pressed')
                        if self.type == 'бел_пешка6':
                            self.rect.x = 250
                            self.rect.y = 300
                            print('pressed')
                        if self.type == 'бел_пешка7':
                            self.rect.x = 300
                            self.rect.y = 300
                            print('pressed')
                        if self.type == 'бел_пешка8':
                            self.rect.x = 350
                            self.rect.y = 300
                            print('pressed')

                        if self.type == 'чер_конь1':
                            self.rect.x = 50
                            self.rect.y = 0
                            print('pressed')
                        if self.type == 'чер_конь2':
                            self.rect.x = 300
                            self.rect.y = 0
                            print('pressed')
                        if self.type == 'чер_слон1':
                            self.rect.x = 100
                            self.rect.y = 0
                            print('pressed')
                        if self.type == 'чер_слон2':
                            self.rect.x = 250
                            self.rect.y = 0
                            print('pressed')
                        if self.type == 'чер_ладья1':
                            self.rect.x = 0
                            self.rect.y = 0
                            print('pressed')
                        if self.type == 'чер_ладья2':
                            self.rect.x = 350
                            self.rect.y = 0
                            print('pressed')
                        if self.type == 'чер_королева1':
                            self.rect.x = 200
                            self.rect.y = 0
                            print('pressed')
                        if self.type == 'чер_король2':
                            self.rect.x = 150
                            self.rect.y = 0
                            print('pressed')

                        if self.type == 'бел_конь1':
                            self.rect.x = 50
                            self.rect.y = 350
                            print('pressed')
                        if self.type == 'бел_конь2':
                            self.rect.x = 300
                            self.rect.y = 350
                            print('pressed')
                        if self.type == 'бел_слон1':
                            self.rect.x = 100
                            self.rect.y = 350
                            print('pressed')
                        if self.type == 'бел_слон2':
                            self.rect.x = 250
                            self.rect.y = 350
                            print('pressed')
                        if self.type == 'бел_ладья1':
                            self.rect.x = 0
                            self.rect.y = 350
                            print('pressed')
                        if self.type == 'бел_ладья2':
                            self.rect.x = 350
                            self.rect.y = 350
                            print('pressed')
                        if self.type == 'бел_королева1':
                            self.rect.x = 200
                            self.rect.y = 350
                            print('pressed')
                        if self.type == 'бел_король2':
                            self.rect.x = 150
                            self.rect.y = 350
                            print('pressed')
                    #if command[1]
                    #    click_pos = pygame.mouse.get_pos()
                    #    print(click_pos)
                    #    if self.rect.x and self.rect.y== self.rect.collidepoint(click_pos):

                    #        next_event = pygame.event.wait()
                    #        if next_event.type == pygame.MOUSEBUTTONDOWN:
                    #            if next_event.button == 1:
                    #                new_pos = pygame.mouse.get_pos()
                    #                self.rect.x, self.rect.y = new_pos

                    # if event.button == 1:
                    #    mouse_x, mouse_y = pygame.mouse.get_pos()
                    #    if self.rect.y==mouse_y  and  self.rect.x==mouse_x:
                    #        self.rect.y==mouse_y
                    #        self.rect.x==mouse_x
                    # if event.button == 1:
                    #    self.rect.y, self.rect.x==pygame.mouse.get_pos()

                    #    mouse_x2, mouse_y2=mouse_x, mouse_y

                    # if event.button == 1:
                    #    mouse_x, mouse_y = pygame.mouse.get_pos()
                    #    mouse_x2, mouse_y2=mouse_x, mouse_y

                    if 75 <= self.rect.x <= 125:
                        self.rect.x = 100
                    if 125 < self.rect.x <= 175:
                        self.rect.x = 150
                    if 175 < self.rect.x <= 225:
                        self.rect.x = 200
                    if 225 < self.rect.x <= 275:
                        self.rect.x = 250
                    if 275 < self.rect.x <= 325:
                        self.rect.x = 300
                    if 325 < self.rect.x <= 390:
                        self.rect.x = 350
                    if 25 <= self.rect.x < 75:
                        self.rect.x = 50
                    if -25 <= self.rect.x < 25:
                        self.rect.x = 0

                    if 77 <= self.rect.y <= 127:
                        self.rect.y = 100
                    if 127 < self.rect.y <= 177:
                        self.rect.y = 150
                    if 177 < self.rect.y <= 227:
                        self.rect.y = 200
                    if 227 < self.rect.y <= 277:
                        self.rect.y = 250
                    if 277 < self.rect.y <= 327:
                        self.rect.y = 300
                    if 327 < self.rect.y <= 377:
                        self.rect.y = 350
                    if 27 <= self.rect.y < 77:
                        self.rect.y = 50
                    if -25 <= self.rect.y < 27:
                        self.rect.y = 0
                    

                    # if 75<=self.rect.y<=127:
                    #     self.rect.y=100

    def update(self, events):
        self.move(events)