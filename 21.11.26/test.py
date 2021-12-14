import pygame, sys, random
from pygame.locals import *

# pygame 셋업
pygame.init() #초기화 코드 반드시 필요함 
mainClock = pygame.time.Clock()

#윈도우 설정
screen_width= 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

#타이틀 제목 설정 
pygame.display.set_caption("지렁이 키우기?")

#색상 설정
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# 푸드와 지렁이 정보 셋업
foodCounter = 0
NEWFOOD = 60
FOODSIZE = 15

worm = pygame.Rect(400, 300, 15, 15)
worm_x=0
worm_y=0
worm_x_position = (screen_width / 2) - (15 / 2)
worm_y_position = screen_height - 15

moveLeft=False
moveRight = False
moveUp = False
moveDown = False
 
MOVESPEED = 6

#푸드 생성 
foods = []
for i in range(10):
    foods.append(pygame.Rect(random.randint(0, screen_width - FOODSIZE), random.randint(0, screen_height - FOODSIZE), FOODSIZE, FOODSIZE))




#게임 루프 시키는 부분
    #pygame은 이벤트 루프가 없으면 창이 꺼져버림 
while True:
    #Quit 이벤트 체크하는 부분
    for event in pygame.event.get():
        if event.type ==QUIT:
            pygame.quit()
            sys.exit()     
         
    # 지렁이 부분
        if event.type == pygame.KEYDOWN:  #키가 눌렷는지 확인 
            if event.key == pygame.K_UP:
                    moveUp = True
                    moveDown = False
            elif event.key == pygame.K_DOWN:
                    moveUp = False
                    moveDown = True
            elif event.key == pygame.K_LEFT:
                    moveRight = False
                    moveLeft = True
            elif event.key == pygame.K_RIGHT:
                    moveRight = True
                    moveLeft = False
                    
        if event.type == KEYUP: # 키를 뗏을때 
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT:
                moveLeft = False
            if event.key == K_RIGHT:
                moveRight = False
            if event.key == K_UP:
                moveUp = False
            if event.key == K_DOWN:
                moveDown = False
                    
 # 새로운 푸드  추가하는 부분
    foodCounter += 1
    if foodCounter >= NEWFOOD:
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0, screen_width - FOODSIZE), random.randint(0, screen_height - FOODSIZE), FOODSIZE, FOODSIZE))

    screen.fill(BLACK)

    if moveDown and worm.bottom < screen_height:
        worm.top += MOVESPEED
    if moveUp and worm.top > 0:
        worm.top -= MOVESPEED
    if moveLeft and worm.left > 0 :
        worm.left -= MOVESPEED
    if moveRight and worm.right < screen_width:
        worm.left += MOVESPEED
        
    pygame.draw.rect(screen, WHITE, worm)
                        

   # 푸드랑 지렁이 충돌할 때
    for food in foods[:]:
        if worm.colliderect(food):
            foods.remove(food)
            screen.blit(worm(worm_x, worm_y)
            
            
            

    # 푸드 생성 부분
    for i in range(len(foods)):
        pygame.draw.rect(screen, GREEN, foods[i])

    
    

    
    pygame.display.update()
    mainClock.tick(40)

