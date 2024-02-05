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

class Object:
    def __init__(self): #생성자
        self.x = 0
        self.y = 0
    def add_img(self,address): # 이미지 로딩
        if address[-3:]=='png':
            self.img = pygame.image.load(address).convert_alpha()
            # 이미지 로딩 주의점 : png 파일은 가져올 경우 convert_alpha()를 써줘야 한다.
        else:
            self.img = pygame.image.load(address)
            # image.load(경로) - 이미지 로딩 메소드
            # \ 는 읽을 수 없다 -> / 로 변환
    def change_size(self,width,height): # 이미지 사이즈 변환
        self.img = pygame.transform.scale(self.img,(width,height))
        # transform.scale(이미지, 크기(너비,높이) )이미지 크기 변환

        self.width,self.height = self.img.get_size()
        # get_size() - 이미지 파일의 크기 반환 ( 가로 , 세로 )
    def show(self): # 이미지 출력
        screen.blit(self.img,(self.x,self.y))
        # blit(이미지,좌표) - 좌표에 이미지를 불러옴
        # 좌표 - 이미지 파일의 왼쪽 상단


player = Object() # Object 객체 : player
player.add_img("C:/Users/최영준/Desktop/Python/Python_Class/PyGame/pyGame_images/player.png")
player.change_size(80,80)
player.x = round(size[0]/2) - round(player.width / 2) # size[0] - size 의 x좌표
player.y = size[1]-player.height-50 # size[1] - size 의 y좌표 ( 캐릭터 높이 만큼 차이주기 + a)

enemy = Object()

black = (0,0,0)
white = (255,255,255)

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

    #  - 4-4. 전사작업(그리기)
    screen.fill(black)
    # fill(color) - 화면을 color 로 채움

    player.show()

    #  - 4-5. 업데이트
    pygame.display.flip()
    # flip() - 화면에 나타냄
# 5. 종료
pygame.quit()
# 반복문 탈출 -> 프로그램 종료
# quit() - 종료