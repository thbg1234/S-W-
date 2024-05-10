'''
리스트=>리스트가 생성 된 후 추가,삭제,삽입이 가능하다
'''
#과잉 리스트가 생성
fruits = ['딸기','사과','바나나']
print("과일 목록:",fruits)

fruits.append('수박')
print("과일 목록(수박 추가)",fruits)
fruits.append('망고')
print("과일 목록(망고 추가)",fruits)

fruits = fruits + ["포도"]
print("과일 목록에 망고가 있나요?",'망고'in fruits)

print("과일의 개수는 ?",len(fruits))

print("재일 좋아하는 과일은?",fruits[0])
print("제일 싫어하는 과일은?",fruits[-1])

fruits.append('두리안')

print("과일 줄 가장 큰 과일은?",max(fruits))
print("과일 줄 가장 작은 과일은?",min(fruits))


fruits.sort()
print("과일 오름차순:",fruits)

fruits.sort(reverse = True)
print("과일 내림치순",fruits)


'''
리스트를 원하는 모양으로 자르 슬라이상
순서가 있다 =>index(위치)가 있다
'''

print("과일 리스트 중 2,3,4번 과일은 ?",fruits[1:4])
print("과일 리스트 중 1~3번 과일은 ?",fruits[0:3])
print("과일 리스트 중 1~3번 과일은 ?",fruits[:3])
print("과일 리스트 중 3번부터 마지막까지 과일은 ?",fruits[2:])

print("과일을 거꾸로 출력하면:",fruits[::-1])

'''
리스트의 원소 값 조작
'''

print ()
print("과일 목록 :",fruits)

fruits.insert(3,'사과')
print("과일목록(3번지에 사과 삽업:)",fruits)

print("사과 위치는?",fruits.index('사과'))

print("사과 개수는?",fruits.count('사과'))

'''
리스트 항목 삭제
'''

print()

fruits.remove('사과')
print('과일 목록(사과 삭제)',fruits)

fruits.pop()
print("과일 목롤(마지막 항목 삭제):",fruits)

del fruits[0]










