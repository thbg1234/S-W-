'''
작성일:2024.5.21
작성자:컴퓨터공학부 202195056 석홍신
설명 :키와 값을 가지는 딕셔너리
'''

#빈 딕셔너리 생성
phone_book1 = {}

#딕셔너리에 값 저장
#1)[key] = value
phone_book1['석홍신'] = '010-1234-5678'  
print("phone_book1:", phone_book1) 

#2){key:value}
phone_book2 = {'석홍신': "010-1234-5678", "홍길동": "010-4567-6789"}  
print("phone_book2:", phone_book2)

#5멍의 이름과 전화번호 저장
phone_book3 = {}
phone_book3['010-1234-5678'] = '석홍신'
phone_book3['010-3456-7890'] = '홍길동'
phone_book3['010-1267-9542'] = '김길동'
phone_book3['010-6521-9852'] = '정길동'
phone_book3['010-2544-3587'] = '박길동'

print("phone_book3:",phone_book3)

print("phone_book3의 전화번호:",phone_book3.keys())
print("phone_book3의 이름:",phone_book3.values())
print("phone_book3의 이름과 연락처:",phone_book3.items())

print("전화번호부의 모든 내용 출력")
for phone_num,name in phone_book3.items():
    #key와 value가 저장되 변수
    print(name,":",phone_num)

print()
print("전화번호 의 key로 접근하여 출력")
for key in phone_book3.keys():
    print(phone_book3[key],":",key)
print()

person_dict = {'name':'석홍신','age':'23','class':'4학년'}
print("name:",person_dict['name'])

print("age:",person_dict['age'],"세")
print()

print("phone_book3 정렬")
print(sorted(phone_book3))

print("키를 기준으로 전체 정렬")
sort_phone_book3 = sorted(phone_book3.items(),key = lambda x : x[0])
print(sort_phone_book3)

print("값을 기준으로 전체 정렬")
sort_phone_book3 = sorted(phone_book3.items(),key = lambda x : x[1])
print(sort_phone_book3)

print()

print("항목 삭제")
del phone_book3['010-1234-5678']
print(phone_book3)

print("전체 삭제")
phone_book3.clear()
print(phone_book3)

print()
dict1 = {1:'one',2:'two',3:'three'}
print("사전 내용:",dict1)

print("사전의 모든 키 출력")
for num in dict1.keys():
    print(num,end = ' ')
    
print()
print("사전의 모든 값 출력")
for alpanum in dict1.values():
    print(alpanum,end=' ')
    
print()

for num,alpanum in dict1.items():
    print(num,"은(는) 영어로",alpanum)