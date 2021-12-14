import pygame, sys, random, time
from pygame.locals import *


#윈도우 설정 
screen_width= 800
screen_height = 600



#색상 설정
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# 푸드와 지렁이 정보 셋업
foodCounter = 0
NEWFOOD = 60
FOODSIZE = 15

worm= pygame.

worm_posX=(screen_width / 2) - (15/2)
# 화면 가로에 중간지점에 캐릭터의 가로 위치
worm_posY= screen_height - 15
# 화면 세로 크기 가장 아래에 캐릭터의 세로 위치

#이동용 좌표 
worm_x=0
worm_y=0


is_wormCrash = False #지렁이 충돌상태

if __name__ == '__name__': #메인 함수부분 같은 거임
    pygame.init() #초기화 코드 반드시 필요
    #윈도우 창 생성
    screen = pygame.display.set_mode((screen_width, screen_height),0,32)
    #타이틀 제목 설정
    pygame.display.set_caption("지렁이 키우기?")
    #파이게임 창 위에 게임적인 요소를 주기 위한 부분
    surface = pygame.Surface(window.get_size()) #윈도우 창 사이즈를 주면됨
    surface = surface.convert()
    surface.fill(BLACK)
    clock = pygame.time.Clock() #시간사용
    pygame.key_set_repeat(1,40) # 키의 리핏 셋팅
    
     

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
                    to_y -= 6
            elif event.key == pygame.K_DOWN:
                    to_y += 6
            elif event.key == pygame.K_LEFT:
                    to_x -= 6
            elif event.key == pygame.K_RIGHT:
                    to_x += 6
                    
        if event.type == pygame.KEYUP: # 키를 뗏을때 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    screen.blit(worm, (worm_posX, worm_posY))

    worm_posX += to_x
    worm_posY += to_y
    
                
                    
 # 새로운 푸드  추가하는 부분
    foodCounter += 1
    if foodCounter >= NEWFOOD:
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0, screen_width - FOODSIZE), random.randint(0, screen_height - FOODSIZE), FOODSIZE, FOODSIZE))



        
   

    if is_wormCrash == True:
        screen.blit(worm,(worm_posX,worm_posY))
        










    # 푸드 생성 부분
    for i in range(len(foods)):
        pygame.draw.rect(screen, GREEN, foods[i])



    pygame.display.update()
    mainClock.tick(40)
    
