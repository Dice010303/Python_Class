#1부터 1000까지의 수중 짝수의 합

sum=0
i=1
while i<=1000 :
    i+=1
    if i%2 == 0 :
        sum+=i
print("{}".format(sum))
