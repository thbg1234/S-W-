'''
작성일:2024.3.19
작성자:컴퓨터공학부 202195056 석홍신
설명:윗변,아랫변,높이를 입력받아
        사다리꼴의 넓이를
        구하는 프로그램 작성하시오
'''

top = float(input("윗변을 입력하세요:"))
bottom = float(input("아랫변을 입력하세요:"))
height = float(input("높이f를 입력하세요:"))

area = ((top+bottom)*height)/2
print("넓이",area,"입니다.")
