import pygame 
import time
import random

pygame.init() 

win = pygame.display.set_mode((500, 750)) 
pygame.display.set_caption("Scaley") 

x = 600
y = 200

run = True

background_color = (255,182,193)

#imports
img = pygame.image.load('icons/logo.jpg')
img = pygame.transform.scale(img, (500, 160))

#fonts
font = pygame.font.SysFont('CourierNew',30,bold=True)
font2 = pygame.font.SysFont('CourierNew',75,bold=True)
font3 = pygame.font.SysFont('CourierNew',20)
surf = font.render('start',True,'white')

button = pygame.Rect(200,480,100,50)
#music
pygame.mixer.init() 
  
pygame.mixer.music.load("audio/bgm.mp3") 
  
pygame.mixer.music.set_volume(0.7) 

pygame.mixer.music.play(-1) 

def draw_text(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    win.blit(img,(x,y))

while run: 
	pygame.time.delay(10) 
	for event in pygame.event.get(): 
		pygame.display.update()
		draw_text("by AK STUDIOS 2023",font3,(245,250,200),150,700)
		win.blit(img,(0,200))  
		pygame.draw.rect(win, (255,228,225), pygame.Rect(0,0, 15, 750))
		pygame.draw.rect(win, (255,228,225), pygame.Rect(485,0, 15, 750))
		pygame.draw.rect(win, (255,228,225), pygame.Rect(0,0, 500, 15))
		pygame.draw.rect(win, (255,228,225), pygame.Rect(0,736, 500, 15))
		if event.type == pygame.QUIT:  
			run = False
	keys = pygame.key.get_pressed() 
	x-=1
	win.fill(background_color) 
    

pygame.quit() 
