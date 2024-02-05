import pygame

# 1. 초기화
pygame.init()

# 2. 게임 화면 설정 -> 크기 고정
size = [400, 850]
screen = pygame.display.set_mode(size)
# display.set_mode - 화면의 크기를 설정 해주는 메소드

title = "pygame"
pygame.display.set_caption(title)
# display.set_caption - 화면의 제목을 설정 해주는 메소드

# 3. 인게임 설정 -> 변수
clock = pygame.time.Clock()
# time.Clock - 시간 변수 설정

player = pygame.image.load("C:/Users/최영준/Desktop/Python/Python_Class/PyGame/pyGame_images/player.png").convert_alpha()
# 이미지 로딩 주의점 : png 파일은 가져올 경우 convert_alpha()를 써줘야 한다.
# image.load(경로) - 이미지 로딩 메소드
# \ 는 읽을 수 없다 -> / 로 변환

player = pygame.transform.scale(player,(100,100))
# transform.scale(이미지, 크기(너비,높이) )이미지 크기 변환

player_width,player_height = player.get_size()
# get_size() - 이미지 파일의 크기 반환 ( 가로 , 세로 )

player_x = round(size[0]/2) - round(player_width / 2) # size[0] - size 의 x좌표
player_y = size[1]-player_height-50 # size[1] - size 의 y좌표 ( 캐릭터 높이 만큼 차이주기 + a)
black = (0,0,0)
white = (255,255,255)

k = 0

# 4. 메인 이벤트 ( 코드 상에서 봤을 때의 이벤트)
system_exit = 0  # 종료 시점 변수
while system_exit == 0:

    #  - 4-1. FPS(Frame Per Second) 설정
    clock.tick(3)
    # tick(frame) - ms(밀리 세컨드) 로 반환 60-> 1초에 60번 움직임(FPS)

    #  - 4-2. 입력(키보드, 마우스) 감지
    for event in pygame.event.get():
    # event.get() - 발생하는 이벤트 반환
    # event에 발생하는 이벤트들을 저장
        if event.type == pygame.QUIT: # [x]버튼을 누른 이벤트
            system_exit = 1  # 반복문 탈출 (break)

    #  - 4-3. 입력, 시간에 따른 변화

    # k += 1 # 화면에 색을 번갈아 나오게 하기 위한 변수
    #
    # if k%2 == 0 :
    #     color = black
    # else :
    #     color = white

    #  - 4-4. 전사작업(그리기)
    screen.fill(black)
    # fill(color) - 화면을 color 로 채움

    screen.blit(player,(player_x,player_y))
    # blit(이미지,좌표) - 좌표에 이미지를 불러옴
    # 좌표 - 이미지 파일의 왼쪽 상단

    #  - 4-5. 업데이트
    pygame.display.flip()
    # flip() - 화면에 나타냄
# 5. 종료
pygame.quit()
# 반복문 탈출 -> 프로그램 종료
# quit() - 종료