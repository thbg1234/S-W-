'''
작성일:2024.4.2
작성자:컴퓨터공학부 202195056 석홍신
    설명 :
    정수를 입력 받아 그 정수의 팩토리얼 값을 출력하시오
    
    [문제 분석]
        5! = 5*4*3*2*1 =>120
    
    
    
'''

input_num = int(input("알고 싶은 백토리얼 값을 입력:"))
fac = 1
num = input_num
while input_num >= 1:
    fac = fac * input_num
    input_num = input_num - 1
'''

for num in range(input_num,0,-1):
    fac *= num
    '''
print(f"{num}!={fac}")

