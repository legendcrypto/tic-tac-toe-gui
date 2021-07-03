#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pygame
pygame.init()
screen  =  pygame.display.set_mode((550,  550))
pygame.display.set_caption('Tic-Tac-Toe')
first  =  pygame.draw.rect(screen,  (255,  255,  255),  (25,  25,  150,  150))
second  =  pygame.draw.rect(screen,  (255,  255,  255),  (200,  25,  150,  150))
third  =  pygame.draw.rect(screen,  (255,  255,  255),  (375,  25,  150,  150))
fourth  =  pygame.draw.rect(screen,  (255,  255,  255),  (25, 200, 150, 150))
fifth  =  pygame.draw.rect(screen,  (255,  255,  255),  (200,200,150,150))
sixth  =  pygame.draw.rect(screen,  (255,  255,  255),  (375,200,150,150))
seventh  =  pygame.draw.rect(screen,  (255,  255,  255),  (25,  375,  150,  150))
eighth  =  pygame.draw.rect(screen,  (255,  255,  255),  (200,  375,  150,  150))
ninth  =  pygame.draw.rect(screen,  (255,  255,  255),  (375,  375,  150,  150))

rect_won  =  pygame.image.load('rect  won.png') 
circle_won  =  pygame.image.load('circle  won.png')
draw  =  pygame.image.load('draw.png')

running = True
draw_object  =  'rect'
al_p = True
sal_p = True 
tal_p = True 
foal_p = True 
fial_p = True 
sial_p = True 
seal_p = True
eal_p = True 
nal_p = True
li  =  ['  '  for  i  in  range(9)] 
var = ''
def  checkresult(li): 
    global  var   
    count=0
    for g in li:
        if(g=='X'):
            count+=1 
        elif(g=='O'):
            count-=1 
    if(abs(count)<2):
        bool=False 
        ec=False
        if(li[0]==li[1]==li[2]!='  '):
            bool=True 
            var  =  li[0]
        elif(li[3]==li[4]==li[5]!='  '): 
            bool=True
            var  =  li[3]
        elif(li[6]==li[7]==li[8]!='  '): 
            var  =  li[6]
            bool=True 
        elif(li[0]==li[3]==li[6]!='  '):
            var  =  li[0] 
            bool=True
        elif(li[1]==li[4]==li[7]!='  '): 
            bool=True
            var  =  li[1] 
        elif(li[2]==li[5]==li[8]!='  '):
            var  =  li[2] 
            bool=True
        elif(li[0]==li[4]==li[8]!='  '  or  li[2]==li[4]==li[6]!='  '): 
            var  =  li[4]
            bool=True
        if  bool==False  :
            for  i  in  li: 
                acount=0
                if  i  ==  "X"  or  i=="O": 
                    continue
                break
            else:
                var  =  'Draw'
                bool=True 
        return var

while  running: 
    pygame.time.delay(300)
    for  event  in  pygame.event.get(): 
        if  event.type  ==  pygame.QUIT:
            running  =  False
        if  event.type  ==  pygame.KEYDOWN:
            if  event.key  ==  pygame.K_SPACE:
                screen.fill((0,  0,  0))
                li = [' ' for i in range(9)]
                draw_object = 'rect'
                var = ''
                al_p = True
                sal_p = True
                tal_p = True
                foal_p = True
                fial_p = True
                sial_p = True
                seal_p = True
                eal_p = True
                nal_p = True
                first = pygame.draw.rect(screen, (255, 255, 255), (25, 25, 150, 150))
                second = pygame.draw.rect(screen, (255, 255, 255), (200, 25, 150, 150))
                third = pygame.draw.rect(screen, (255, 255, 255), (375, 25, 150, 150))
                fourth = pygame.draw.rect(screen, (255, 255, 255), (25, 200, 150, 150))
                fifth = pygame.draw.rect(screen, (255, 255, 255), (200, 200, 150, 150))
                sixth = pygame.draw.rect(screen, (255, 255, 255), (375, 200,150, 150))
                seventh = pygame.draw.rect(screen, (255, 255, 255), (25, 375,150, 150))
                eighth = pygame.draw.rect(screen, (255, 255, 255), (200, 375,150, 150))
                ninth = pygame.draw.rect(screen, (255, 255, 255), (375, 375,150, 150))
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if first.collidepoint(pos) and al_p:
                        if draw_object == 'rect':
                            pygame.draw.rect(screen, (255, 0, 0), (50, 50, 100, 100))
                            draw_object = 'c'
                            li[0] = 'X'
                        else:
                            pygame.draw.circle(screen, (0,255,0), (100, 100), 50)
                            draw_object = 'rect'
                            li[0] = 'O'
                        al_p = False
                    if second.collidepoint(pos) and sal_p:
                        if draw_object == 'rect':
                            pygame.draw.rect(screen, (255, 0, 0), (225, 50, 100, 100))
                            draw_object = 'c'
                            li[1] = 'X'
                        else:
                            pygame.draw.circle(screen, (0,255,0), (275, 100), 50)
                            draw_object = 'rect'
                            li[1] = 'O'
                        sal_p = False
                    if third.collidepoint(pos) and tal_p:
                        if draw_object == 'rect':
                            pygame.draw.rect(screen, (255, 0, 0), (400, 50, 100, 100))
                            draw_object = 'c'
                            li[2] = 'X'
                        else:
                            pygame.draw.circle(screen, (0,255,0), (450, 100), 50)
                            draw_object = 'rect'
                            li[2] = 'O'
                        tal_p = False
                    if fourth.collidepoint(pos) and foal_p:
                        if draw_object == 'rect':
                            pygame.draw.rect(screen, (255, 0, 0), (50, 225, 100, 100))
                            draw_object = 'c'
                            li[3] = 'X'
                        else:
                            pygame.draw.circle(screen, (0,255,0), (100, 275), 50)
                            draw_object = 'rect'
                            li[3] = 'O'
                        foal_p = False
                    if fifth.collidepoint(pos) and fial_p:
                        if draw_object == 'rect':
                            pygame.draw.rect(screen, (255, 0, 0), (225, 225, 100,100))
                            draw_object = 'c'
                            li[4] = 'X'
                        else:
                            pygame.draw.circle(screen, (0,255,0), (275, 275), 50)
                            draw_object = 'rect'
                            li[4] = 'O'
                        fial_p = False
                    if sixth.collidepoint(pos) and sial_p:
                        if draw_object == 'rect':
                            pygame.draw.rect(screen, (255, 0, 0), (400, 225, 100,100))
                            draw_object = 'c'
                            li[5] = 'X'
                        else:
                            pygame.draw.circle(screen, (0,255,0), (450, 275), 50)
                            draw_object = 'rect'
                            li[5] = 'O'
                        sial_p = False
                    if seventh.collidepoint(pos) and seal_p:
                        if draw_object == 'rect':
                            pygame.draw.rect(screen, (255, 0, 0), (50, 400, 100, 100))
                            draw_object = 'c'
                            li[6] = 'X'
                        else:
                            pygame.draw.circle(screen, (0,255,0), (100, 450), 50)
                            draw_object = 'rect'
                            li[6] = 'O'
                        seal_p = False
                    if eighth.collidepoint(pos) and eal_p:
                        if draw_object == 'rect':
                            pygame.draw.rect(screen, (255, 0, 0), (225, 400, 100,100))
                            draw_object = 'c'
                            li[7] = 'X'
                        else:
                            pygame.draw.circle(screen, (0,255,0), (275, 450), 50)
                            draw_object = 'rect'
                            li[7] = 'O'
                        eal_p = False
                    if ninth.collidepoint(pos) and nal_p:
                        if draw_object == 'rect':
                            pygame.draw.rect(screen, (255, 0, 0), (400, 400, 100,100))
                            draw_object = 'c'
                            li[8] = 'X'
                        else:
                            pygame.draw.circle(screen, (0,255,0), (450, 450), 50)
                            draw_object = 'rect'
                            li[8] = 'O'
                        nal_p = False
                    b=checkresult(li)
                    if b:
                        if var == 'X':
                            screen.fill((255,0,0))
                            screen.blit(rect_won, (101, 184))
                        elif var == "O":
                            screen.fill((0,255,0))
                            screen.blit(circle_won, (115, 114))
                        else:
                            screen.fill((255,255,255))
                            screen.blit(draw, (159, 216))
                        b = False
            pygame.display.update()











