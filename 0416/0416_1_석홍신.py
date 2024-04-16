'''
작성일:2024.4.12
작성자:컴퓨터공학부 202195056 석홍신
설명 :두 수를 입력받아 두 수 사이의 모든 수의 합을 계산하시오
    입력 받은 두 수 포함하여 합계를 계산합니다
    
[문제분석]
    첫번쩨 수가 1이고 ,두벙째 수가 10이고
    1~10합 계산하시오
    초기값(시작):첫번쩨 수부터
    초건식(종료):두번쩨 수까지
    증가식:1씩 증가
    
    1)첫번쩨 수가 작은 수이고 ,두번쩨 수가 큰 수이면
    첫번쩨 수부터 두번쩨 수까지 1씩 증가하면서 반복
    
    2)첫번쩨 수가 큰은 수이고 ,두번쩨 수가 작 수이면
    첫번쩨 수부터 두번쩨 수까지 1씩 감소하면서 반복
'''

num1 = int(input("첫번쩨 수자를 입력하시오:"))
num2 = int(input("두번쩨 수자를 입력하시오:"))

sum = 0


if num1>num2:
    for num in range(num2,num1+1):
        sum +=num
    print(f"{num1}부터 {num2}까지 합:{sum}")
    
elif num1<num2:
    for num in range(num1,num2+1):
        sum +=num
    print(f"{num1}부터 {num2}까지 합:{sum}")

else:
    print(f"{num1}부터 {num2}까지 합:{num1}")
    
'''
if num1>num2:
    temp = num1
    num1=num2
    num2=temp

for num in range(num1,num2+1)
    sum +=num
    
print(f"{num11}부터 {num22}까지 합:{num1}")

'''