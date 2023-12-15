# 1부터 100까지의 수중 짝수이고 3의 배수가 아닌 수의 합 출력

sum=0
i=1
while i<=100 :
    if i%2==0 and i%3!=0 :
        sum+=i
    i+=1
print("{}".format(sum))
