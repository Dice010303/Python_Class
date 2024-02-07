import pygame
import random
# 난수 발생

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

black = (0,0,0)
white = (255,255,255)

class Object:
    def __init__(self): #생성자
        self.x = 0
        self.y = 0
        self.distance = 0
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

# Object 객체 : player
player = Object()
player.add_img("C:/Users/최영준/Desktop/Python/Python_Class/PyGame/pyGame_images/player.png")
player.change_size(80,80)
player.x = round(size[0]/2) - round(player.width / 2) # size[0] - size 의 x좌표
player.y = size[1]-player.height-50 # size[1] - size 의 y좌표 ( 캐릭터 높이 만큼 차이주기 + a)
player.distance = 15 # 움직이는 단위


left_move = False
right_move = False
# 이동 변수(검사)
space_move = False
# 행동 변수(발사 검사)

missile_list = []
enemy_list = []
# 많은 수의 객체를 소화하기 위하여 list객체가 필요함.

k = 0  # 미사일 간격 변수

# 4. 메인 이벤트 ( 코드 상에서 봤을 때의 이벤트)
system_exit = 0  # 종료 시점 변수
while system_exit == 0:

    #  - 4-1. FPS(Frame Per Second) 설정
    clock.tick(60)
    # tick(frame) - ms(밀리 세컨드) 로 반환 60-> 1초에 60번 움직임(FPS)

    #  - 4-2. 입력(키보드, 마우스) 감지
    for event in pygame.event.get():
    # event.get() - 발생하는 이벤트 반환
    # event에 발생하는 이벤트들을 저장
        if event.type == pygame.QUIT: # [x]버튼을 누른 이벤트
            system_exit = 1  # 반복문 탈출 (break)

        # print(event) event 를 출력 하여 유니코드 확인
        if event.type == pygame.KEYDOWN: # 키가 눌린 경우
            if event.key == pygame.K_LEFT: # event.key - key 값 반환
                left_move = True
            if event.key == pygame.K_RIGHT:
                right_move = True
            if event.key == pygame.K_SPACE:
                space_move = True
                k = 0
        elif event.type == pygame.KEYUP: # 키가 떼진 경우
            if event.key == pygame.K_LEFT:
                left_move = False
            if event.key == pygame.K_RIGHT:
                right_move = False
            if event.key == pygame.K_SPACE:
                space_move = False

    #  - 4-3. 입력, 시간에 따른 변화
    if left_move == True:
        player.x-=player.distance
        if player.x <= 0 : # 화면의 좌측 상한 0~
            player.x = 0
    elif right_move == True:
        player.x+=player.distance
        if player.x >= size[0] - player.width: # 화면의 우측 상한 - 객체의 가로 길이
            player.x = size[0] - player.width
    # 이동 범위를 제한 하여야 화면을 안 벗어난다.

    if space_move == True and k % 6 == 0:
        # 60번씩 실행될 때 6의 배수 일때만 실행
        missile = Object() # Object 객체 : missile (space를 눌렀을때 생성)
        missile.add_img("C:/Users/최영준/Desktop/Python/Python_Class/PyGame/pyGame_images/missile.png")
        missile.change_size(40,40)
        missile.x = player.x + round(player.width/2) - round(missile.width/2)
        # player 의 반만큼 오른쪽으로 missile 의 반만큼 왼쪽으로
        missile.y = player.y - missile.height
        # missile 의 높이만큼 위로
        missile.distance = 7
        missile_list.append(missile)

    k += 1

    delete_list=[]
    # 삭제할 객체 list
    for i in range(len(missile_list)):
        # i 에는 miisile_list의 인덱스가 들어감
        m = missile_list[i]
        m.y -= m.distance
        if m.y <= -m.height:
            delete_list.append(m)

    try:
        delete_list.reverse() # 가장먼저 list에 추가된것부터 삭제하기 위해 역순으로 순회
        for d in delete_list: # delete_list 순회(역순임)
            del missile_list[d]
        # d 객체를 인덱스 자리에 써서 오류 발생! (Runtime Error) - 예외(exception)
    except:
        pass
    # 예외 처리

    if random.random() > 0.97: # 3% 확률
        # Object 객체 : enemy
        enemy = Object()
        enemy.add_img("C:/Users/최영준/Desktop/Python/Python_Class/PyGame/pyGame_images/enemy.png")
        enemy.change_size(50,50)
        enemy.x = random.randrange(round(player.width/2),size[0]-enemy.width - round(player.width/2))
        # random.randrange - 인자로 주어진 범위 내의 난수를 리턴
        enemy.y = 15
        enemy.distance = 5
        enemy_list.append(enemy)

    for i in range(len(enemy_list)):
        # i 에는 miisile_list의 인덱스가 들어감
        e = enemy_list[i]
        e.y += e.distance
        if e.y >= size[1]: # enemy 객체의 y값이 화면을 벗어날 경우
            delete_list.append(e) # 삭제 list 에 추가

    try:
        delete_list.reverse() # 가장먼저 list에 추가된것부터 삭제하기 위해 역순으로 순회
        for d in delete_list: # delete_list 순회(역순임)
            del missile_list[d]
        # d 객체를 인덱스 자리에 써서 오류 발생! (Runtime Error) - 예외(exception)
    except:
        pass

#  - 4-4. 전사작업(그리기)
    screen.fill(black)
    # fill(color) - 화면을 color 로 채움

    player.show()

    for m in missile_list: # missile_list 순회 -> 화면에 출력
        m.show()

    for e in enemy_list: # enemy_list 순회 -> 화면에 출력
        e.show()

    #  - 4-5. 업데이트
    pygame.display.flip()
    # flip() - 화면에 나타냄
# 5. 종료
pygame.quit()
# 반복문 탈출 -> 프로그램 종료
# quit() - 종료