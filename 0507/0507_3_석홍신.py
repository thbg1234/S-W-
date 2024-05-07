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