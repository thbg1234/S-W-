'''
작성일:2024.3.26
작성자:컴퓨터공학부 202195056 석홍신
설명:숫자와 연산자를 입력 받아 사칙연산의 결과 출력
    
    [문제분석]
        사칙 연산은 +, -, *, / 이다.
        사칙 연산에 따라 계산하고, 출력한다.
        두 개의 정수와 연산자를 입력 받는다.

'''


num1 = int(input("첫 번째 수를 입력하시오 : "))
op = input("연산자를 입력하시오. :")  # 연산자는 문자.
num2 = int(input("두 번째 수를 입력하시오 : "))

if op == '+' :
    print(f"{num1} + {num2} = {num1 + num2}")
elif op == '-' :
    print(f"{num1} - {num2} = {num1 - num2}")
elif op == '*' :
    print(f"{num1} * {num2} = {num1 * num2}")
elif op == '/' :
    if num2 != 0 :  # 두 번째 수가 0이 아니면
        print(f"{num1} / {num2} = {num1 / num2}")
    else :  # 두 번째 수가 0이면
        print("0으로 나눌 수 없다.")
else :
    print("연산자를 잘 못 입력하셨습니다.")
