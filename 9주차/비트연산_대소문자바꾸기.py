word = input()

#대문자 A는 65, 소문자 a는 97
#대문자 A는 0100 0001 소문자 a는 0110 0001
#대문자 D는 0100 0100 소문자 d는 0110 0100
#대소문자는 이진표현의 6번째 자리만 다른 패턴이 있음
#6번째 자리인 32를 XOR 하면 대문자->소문자, 소문자->대문자가 됨

for i in word:
    print(chr(ord(i)^32), end="")
