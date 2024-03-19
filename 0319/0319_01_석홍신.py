'''
작성일:2024.3.19
작성자:컴퓨터공학부 202195056 석홍신
설명:입력을 위한 input()함수 사용하기
'''

#이름 입력받기=>이름을 입력받아 변수에 저장
name = input("이름을 입력하세요:")
#입력 받은 이름 출력하세요
print(name,"님 환영합니다.")
print("{}님 환영합니다.".format(name))
print(f"{name}님 환영합니다.")

#국어 점수를 입력 받아 변수에 저장
kor = input("국어 점수를 입력하세요:")
#수학 점수를 입력 받아 변수에 저장
math = input("수학 점수를 입력하세요:")
#input()함수로 입력 받은 값은 문자열입니다

#두 과목의 점수를 합하여 변수에 저장
total = kor + math

#합계 출력
#두 과목 점수의 합계는 00점입니다

print("두 과목 점수의 합계는" ,total,"점입니다")
print("두 과목 점수의 합계는 {}점입니다".format(total))
print(f"두 과목 점수의 합계는 {total}점입니다")

eng = int(input("영어 점수 입력하세요:"))
com = int(input("컴퓨터 점수 입력하세요:"))

total = eng + com 
print("두 과목 점수의 합계는" ,total,"점입니다")
print("두 과목 점수의 합계는 {}점입니다".format(total))
print(f"두 과목 점수의 합계는 {total}점입니다")

print("kor 변수에 저장된 자료형",type(kor))
print("math 변수에 저장된 자료형",type(math))
print("eng 변수에 저장된 자료형",type(eng))
print("com 변수에 저장된 자료형",type(com))