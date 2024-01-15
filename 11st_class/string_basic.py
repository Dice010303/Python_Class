print("== 예제 1 ==")
s = "안녕하세요."

print("s의 길이 출력")
# 구현
print(len(s))
print("s를 이루는 문자 중에서 앞에꺼, 2개 출력")
# 구현
print(s[0:2])
print("s를 이루는 문자 중에서 앞에서 문자 하나 건너 뛰고 1개 출력")
# 구현
print(s[1:2])
print("s를 이루는 문자 중에서 앞에서 문자 4개 출력, 첫 인덱스 생략")
# 구현
print(s[:4])
print("s를 이루는 문자 중에서 앞에서 문자 3개 건너뛰고, 나머지 전부 출력, len")
# 구현
print(s[3:len(s)])
print("s를 이루는 문자 중에서 앞에서 문자 3개 건너뛰고, 나머지 전부 출력, 뒤 인덱스 생략, 방법 2")
# 구현
print(s[3:])
print("== 예제 2 ==")
s = "안녕하세요"
print("s를 이루는 문자를 하나씩 출력, while")
# 구현
num=0
while num<len(s):
    print(s[num])
    num+=1
print("s를 이루는 문자를 역순으로 하나씩 출력, while")
# 구현
num=len(s)-1
while num>-1:
    print(s[num])
    num-=1
print("s를 이루는 문자를 하나씩 출력, for")
# 구현
for i in s:
    print(i)
print("== 예제 3 ==")
s = "a안b녕c하d세e요f"

print("s를 이루는 문자 중에서 한글만 출력")
# 구현
for i in range(len(s)):
    if i%2!=0:
        print(s[i])
print("s를 이루는 문자 중에서 한글만 출력, for, if or, continue")
# 구현
for c in s:
    if c=='a' or c=='b' or c=='c' or c=='d' or c=='e' or c=='f':
        continue
    print(c)
print("s를 이루는 문자 중에서 한글만 출력, for, if and, 방법 2")
# 구현
for c in s:
    if c!='a' and c!='b' and c!='c' and c!='d' and c!='e' and c!='f':
        print(c)
print("s를 이루는 문자 중에서 한글만 출력, for, not in, 방법 3")
for c in s:
    if c not in ['a','b','c','d','e','f']:
        print(c)
# 구현