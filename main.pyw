from glob import glob1
from turtle import back
from xml.etree.ElementTree import C14NWriterTarget
import pygame
import time
import random

scorebox=500

pygame.init()

r= 255
g= 182
b= 193

background_colour = (r, g, b) 
screen = pygame.display.set_mode((500, 750)) 
pygame.display.set_caption('Scaley') 
screen.fill(background_colour) 
pygame.display.flip() 
running = True
resx1 = 85
resx2  = 75

img = pygame.image.load('icons/logo.jpg')
img = pygame.transform.scale(img, (500, 160))

item1=pygame.image.load('icons/brick.png')
item1 = pygame.transform.scale(item1, (resx1, resx1))

item2=pygame.image.load('icons/coin.png')
item2 = pygame.transform.scale(item2, (resx2, resx2-15))

item3=pygame.image.load('icons/brick.png')
item3 = pygame.transform.scale(item3, (resx1, resx1))

item4=pygame.image.load('icons/coin.png')
item4 = pygame.transform.scale(item4, (resx2, resx2-15))

item5=pygame.image.load('icons/brick.png')
item5 = pygame.transform.scale(item5, (resx1, resx1))

font = pygame.font.SysFont('CourierNew',30,bold=True)
gont = pygame.font.SysFont('CourierNew',75,bold=True)
surf = font.render('start',True,'white')
btngy=0
btngx=0
button = pygame.Rect(200,380,100+btngx,50+btngy)
pont = pygame.font.SysFont('CourierNew',20)

x=[]
y=[]
show_score1 = 0
show_score2 = 0
loop = 0

score=0

start = 0
g=10
r=11
def draw_text(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    screen.blit(img,(x,y))

pygame.mixer.init() 
  
pygame.mixer.music.load("audio/bgm.mp3") 
  
pygame.mixer.music.set_volume(0.7) 

pygame.mixer.music.play(-1) 

while running:  
    for event in pygame.event.get():
        if start ==0:  
            screen.fill(background_colour) 
            pygame.mouse.set_visible(True)
            draw_text("  USE THE MOUSE TO SCALE THE PIPES TO ",pont,(255,255,255),20,500)
            draw_text("    AVOID OBSTACLES & GAIN COINS   ",pont,(255,255,255),20,530)
            draw_text("    SCALE DOWN TO SLOW THE SPEED",pont,(255,255,255),20,560)
            draw_text("     AND MAINTAIN HEALTH LEVEL  ",pont,(255,255,255),20,590)
            draw_text("by AK STUDIOS 2023",pont,(245,250,200),150,700)
            screen.blit(img,(0,200))  
            pygame.draw.rect(screen, (255,228,225), pygame.Rect(0,0, 15, 750))
            pygame.draw.rect(screen, (255,228,225), pygame.Rect(485,0, 15, 750))
            pygame.draw.rect(screen, (255,228,225), pygame.Rect(0,0, 500, 15))
            pygame.draw.rect(screen, (255,228,225), pygame.Rect(0,736, 500, 15))
            if event.type == pygame.QUIT: 
                running = False

            a,b= pygame.mouse.get_pos()
            if button.x <= a <= button.x+100+btngx and button.y <= b <= button.y+50+btngy:
                pygame.draw.rect(screen,(255,228,225),button)
            else:
                pygame.draw.rect(screen,(255, 182, 193),button )
            screen.blit(surf,(button.x+5,button.y+5))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.collidepoint(event.pos):
                    screen.fill((0,0,0))
                    pygame.mixer.music.pause() 
                    startsound = pygame.mixer.Sound('audio/button.mp3')
                    pygame.mixer.music.set_volume(0.8) 
                    startsound.play()
                    time.sleep(0.5)
                    pygame.mixer.music.play() 
                    pygame.display.flip()
                    start = 1
            
            #pygame.display.update() 
             

        if start ==1:

 
            c1 = pygame.image.load("icons/coin.png")
            b1 = pygame.image.load("icons/brick.png")
            


            bg = pygame.image.load("icons/bg.jpg")
            bg = pygame.transform.scale(bg, (500, 750))

            bod = pygame.image.load("icons/bod.png").convert()
            bod = pygame.image.load("icons/bod.png").convert_alpha()
            
            
            lock = pygame.image.load('icons/lock.png').convert()
            lock = pygame.image.load('icons/lock.png').convert_alpha()    
            lock = pygame.transform.scale(lock, (75, 75))

            edge = pygame.image.load("icons/edge.png").convert()
            edge = pygame.image.load("icons/edge.png").convert_alpha()

            bod = pygame.transform.scale(bod, (160, 160))

            face = pygame.image.load("icons/face.png").convert()
            face = pygame.image.load("icons/face.png").convert_alpha()
            face = pygame.transform.scale(face, (50, 50))

            
            
            if event.type == pygame.QUIT: 
                    running = False
            
            #pygame.display.update()
    if start==2:
                bg = pygame.image.load("icons/bg.jpg")
                bg = pygame.transform.scale(bg, (500, 750))
                screen.blit(bg, (0, 0))
                pygame.mixer.music.pause() 
                gameover = pygame.mixer.Sound('audio/error.mp3')
                pygame.mixer.music.set_volume(0.8) 
                gameover.play()
                loop = 0
                x=[]
                y=[]
                draw_text("GAME OVER",gont,(245,250,200),500/2-200,750/2-100)
                pygame.display.update()
                time.sleep(1)
                time.sleep(1.5)
                pygame.mixer.music.play() 
                start = 0

    if start == 1:
                
        if scorebox<0:
            start=2
        scorebox-=0.05
        print(scorebox)
        screen.blit(bg, (0, 0))
        if loop ==0:
            scorebox=500
            show_score1=0
            show_score2=0
            for i in range(0,5):
                if i%2==0:
                    y.append(random.randint(250,650))

                else:
                    y.append(random.randint(480,650))
                x.append(random.randint(550,610))

            print(y)
            print(x)
        loop=1
        #duck x
        a=0.5
        x[0]-=a
        x[1]-=a
        x[2]-=a
        x[3]-=a
        x[4]-=a
        
        citem1=item1.get_rect()
        citem1.x = x[0]
        citem1.y=  y[0]
        screen.blit(item1,citem1)

        citem2=item2.get_rect()
        citem2.x= x[4]
        citem2.y= y[4]
        

        citem3=item4.get_rect()
        citem3.x = x[1]
        citem3.y= y[1]
        


        if x[0]==-67:
            x[0]=random.randint(500,700)
            y[0]=random.randint(180,350)

        if x[1]==-67:
            x[1]=random.randint(1100,1300)
            y[1]=random.randint(350,480)
            
        if x[2]==-67:
            x[2]=random.randint(900,1100)
            y[2]=random.randint(250,350)

        if x[3]==-67:
            x[3]=random.randint(1100,1300)
            y[3]=random.randint(250,350)

        if x[4]==-50:
            x[4]=random.randint(1300,1500)
            y[4]=random.randint(350,480)
            show_score2=1
        
        if x[1]==-50:
            show_score1=1
        if x[4]==-50:
            show_score2=1
        
            
           
        
        
        #pygame.draw.rect(screen, (255, 0, 0), (x, 100, 20, 20)) 
        pygame.mouse.set_visible(False)
        (mx,my) = pygame.mouse.get_pos()
            #the new start
        
        bod = pygame.transform.scale(bod, (60, my))
        cbod = bod.get_rect()
        cbod.x = 500/2-150
        cbod.y = 20
        

        edge = pygame.transform.scale(edge, (60, 120))
        screen.blit( edge, (500/2-150,-30),)

        edge2 = pygame.transform.rotate(edge, 180)
        cedge = edge2.get_rect()
        cedge.x= 500/2-150
        cedge.y = my-50
        screen.blit(edge2,cedge)

        if cedge.colliderect(citem1):
            start=2
        if cbod.colliderect(citem1) :
            start = 2
        if cbod.colliderect(citem2)or cedge.colliderect(citem2) and show_score1==1:
            score+=1
            scorebox+=1
            show_score1=0
            scrbgm = pygame.mixer.Sound('audio/score.mp3')
            pygame.mixer.music.set_volume(0.4) 
            scrbgm.play()  
        if cedge.colliderect(citem3)or cbod.colliderect(citem3) and show_score2==1:
            score+=1
            scorebox+=1
            show_score2=0
            pygame.mixer.music.set_volume(0.4) 
            scrbgm = pygame.mixer.Sound('audio/score.mp3')
         
            scrbgm.play()  

        
        pygame.draw.rect(screen, (255,228,255), pygame.Rect(0,680, scorebox, 50))
        if show_score1 == 1:
            screen.blit(item2,citem2)
        if show_score2 == 1:
            screen.blit(item4,citem3)
        screen.blit( bod,cbod)
        
        #screen.blit(face,(500/2-155,my-50),)
        #print(my)
        
        screen.blit(lock,(mx,my),)
        
    pygame.display.update()    





#fduck its over