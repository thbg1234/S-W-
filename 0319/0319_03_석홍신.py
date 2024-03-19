'''
작성일:2024.3.19
작성자:컴퓨터공학부 202195056 석홍신
설명:5과목의 점수를 입력받아
        총정과 평균을 출력하는 프로그램
kor,eng,math,com,sci,total,avg

'''

kor = int(input("국어 점수를 입력하세요:"))
eng = int(input("영어 점수를 입력하세요:"))
math = int(input("수학 점수를 입력하세요:"))
com = int(input("컴퓨터 점수를 입력하세요:"))
sci = int(input("과학 점수를 입력하세요:"))

total = kor + eng + math + com + sci
avg = (kor + eng + math + com + sci)/5

print("총점은 {} 입니다".format(total))
print("평균은 {} 입니다".format(avg))
print("평균 점수{:.2f}".format(avg))
print(f"평균 점수{avg:.2f}")