# 문제 : 리스트에 각 달의 끝 날짜들을 담고, '1월은 31일까지'와 같은 양식으로 출력, len 사용

end_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(len(end_days)):
    print("{}월은 {}일까지".format(i+1,end_days[i]))