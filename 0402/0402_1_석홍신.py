'''
작성일:2024.4.2
작성자:컴퓨터공학부 202195056 석홍신
    설명 :오늘의 날씨를 입력받아 나의 기분을 표현해 보자
    날씨는 맑음,맑은 후 흐림,흐림,비 4가지이다.
'''

print("=====[보기]=====")
print("맑음,맑은 후 흐림,흐림,비")
print("================")

weather = input("보기를 참고하여 날씨를 입력하세요:")

if weather == "맑음":
    print("산책 가고 싶다")
elif weather =="맑은 후 흐림"or weather =="맑은후 흐림" or weather =="맑은 후흐림" or weather =="맑은후흐림":
    print("쇼핑 가고 싶다")
elif weather =="흐림":
    print("낚시 가고 싶다")
elif weather =="비":
    print("영화를 보고 싶다")
else:
    print("입력 오류")