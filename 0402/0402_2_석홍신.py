'''
작성일:2024.4.2
작성자:컴퓨터공학부 202195056 석홍신
    설명 :월을 입력받아 해당 계절을 출력하시오.
        3.4.5=>봄
        6.7.8=>여름
        9.10.11=>가을
        12.1.2=>겨울
        

문제 분석
    입력: 코드가 사용자 입력을 받아야 하는 달, 이 달은 정수 (1-12) 일 수 있습니다.
    분류: 입력한 달에 따라 코드는 해당 계절로 분류해야 합니다.
    출력: 마지막으로 코드는 해당 계절 이름을 출력해야 합니다.
알고리즘
    입력 수신: input() 함수를 사용하여 사용자가 입력한 월을 수신하고 int() 함수를 사용하여 정수로 변환합니다.
    조건판단: if-elif-else 문을 사용하여 월별로 계절을 판단한다.
    출력: print() 함수를 사용하여 계절 이름을 출력합니다.
'''
month = int(input("월을 입력(1-12): "))  
if month>12 or month<1:
    print("올바른 월을 입력하십시오.")
else:
    if 3 <= month <= 5:  
        season = "월는 봄입니다"  
    elif 6 <= month <= 8:  
        season = "월는 여름입니다"  
    elif 9 <= month <= 11:  
        season = "월는 가을입니다"  
    else: 
        season = "월는 겨울입니다"  
    print(month,season)