#PyGame 그래픽표현(선, 사각형, 원...)
import pygame 
from pygame.locals import QUIT
from pygame.draw import *
# from pygame.image import * 밑에가 더 짧게 쓸 수 있음 pygame.image.load() -> image.load(), 충돌은 고려하기
import pygame.image as image
import sys 

# 기본 변수
pygame.init()
Surface = pygame.display.set_mode((400, 400))
FPSCLOCK = pygame.time.Clock()
pygame.display.set_caption('Pygame Graphic')

def main():
    # 이미지 로드
    snake = image.load('./image/snake.png')
    # 텍스트 변수
    myfont = pygame.font.SysFont('NanumGothic', 50)
    message1 = myfont.render('This is my message', True, (255, 150, 255))
    message2 = myfont.render('This is PyGame', False, (255, 150, 255))

    while True: # while True 안은 계속 변경
        Surface.fill(color='black')
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # 화면 표현은 요기, start_pos=(x,y)
        for x in range(10, 400, 10):
            line(Surface, 'white', (x,0), (x,400))
        for y in range(10, 400, 10):
            line(Surface, 'white', (0,y), (400,y))

        # 선
        pygame.draw.line(Surface, color=(255,0,0), start_pos=(30, 30), end_pos=(150, 30), width=3)
        line(Surface, (0,255,0), (30,60), (150,60), 5)
        line(Surface, (0,0,255), (30,90), (150,150), 7)

        # 사각형
        pygame.draw.rect(Surface,color='white',rect=(200,30,50,50))
        rect(Surface, 'red', (260, 30, 100, 50), 4)

        # 원 (중심을 시작점으로)
        pygame.draw.circle(Surface, (255,255,0), (40, 180), 10)
        circle(Surface, (255,255,255), (80, 180), 20)
        circle(Surface, (255,112,20),(280, 160), 30, 10)

        # 타원
        pygame.draw.ellipse(Surface, color=(255,255,255), rect=(280, 180, 100, 50))
        ellipse(Surface, (255,255,0), (280, 300, 100, 50), 10)

        # polygon 다각형(별 ...)

        # 이미지 (flaticon.com)
        Surface.blit(snake, (336,336))
        Surface.blit(snake, (0, 336), (0,0,64,32))

        # 텍스트
        Surface.blit(message1, (20, 230))
        Surface.blit(message2, (20, 280))


        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == '__main__':
    main()