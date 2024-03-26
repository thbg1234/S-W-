'''
작성일:2024.3.26
작성자:컴퓨터공학부 202195056 석홍신
설명:점수를 입력받아 학점을 출력하시오
    90~100:A
    80~89:B
    70~79:C
    60~69:D
    0~59:F
    아니면 =>else
    아니고 만약 =>elif
    [알고리즘]
    1.점수를 입력 받는다
    2.점수가 90~100 이면
        2.1A학점 출력한다
    3.아니고 만약 점수가 90~89이면
        3.1B학점 출력한다.
    
'''


score = int(input("점수를 입력하시오:"))
if (score>100) or (score<0):
    print("유효하지 않은 점수입니다.")
elif 90<=score:
    print("{}점은 A학점입니다.".format(score))
elif 80<=score:
    print("{}점은 B학점입니다.".format(score))
elif 70<=score:
    print("{}점은 C학점입니다.".format(score))
elif 60<=score:
    print("{}점은 D학점입니다.".format(score))
else:
    print("{}점은 F학점입니다.".format(score))
    