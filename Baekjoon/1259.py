#팰린드롬수
#https://www.acmicpc.net/problem/1259

while True:
    number = input()
    if number == '0':
        break
    if number == number[::-1]:
        print('yes')
    else:
        print('no')
