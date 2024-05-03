'''
작성일:2024.5.3
작성자:컴퓨터공학부 202195056 석홍신
설명 :시퀀스 자료형 실습
    
[문제분석]
    
'''
#문자열
name = "석홍신"
#리스트
city = ["서울시",800,"부산시",400]
#튜플
num = (100,200,300,400)

'''
1.인덱싱(indexing)


'''
surName = name[0]
print("name[0]:",surName)
surName = name[1]
print("name[0]:",surName)
surName = name[2]
print("name[0]:",surName)

print("city[-2]:",city[-2])

city[-4] = "서울특별시"
print("city:",city)

#print("num[5]:",num[5])

'''
2.슬라이링(slicing)
'''
giveName = name[1:3]
print("name[1:3]",giveName)

print("city[2:]",city[2:])

print("num[1:3]:",num[1:3])

print("num[:]:",num[:])
print("num[::]:",num[::])
print("num[::2]:",num[::2])


print("num[-10:10]",num[-10:10])

'''
3.연결
'''
text1 = "I like"
text2 = text1 + "Python Language"
print("text1+문자열 = ",text2)

#num1 = {1,2,3,4,5}
#num2 = {6,7,8,9}
#num = num1+num2
#print("num1+num2=",num)

#result= num1+city
#print("num1+city = ",result)

'''
4.반복
'''
'''
language= ("C","JAVA","Python")
languages = language * 3
print("languages = ",languages)'''

feel = 'happy'*10
print("feel=",feel)

contury = ["대한민국"]*10
print("countury=",contury)

'''
멤비 유무 검사
'''

color = ["red","green","blue","yellow"]
print("리스트에 black이 있나요?","black" in color)
print("리스트에 black이 있나요?","red" in color)

text3 = "python"
print("문자열에 't'가 있나요?",t in text3)
print("문자열에 소문자 'P'가 있나요?","P" in text3)
print("문자열에 대문자 'p'가 있나요?","p" in text3)

for i in text3:
    print(i)

'''
6.길이 정보
'''

#문자열 text2의 길이
print("문자열 text2의 길이:",len(text2))

#리스트 city의 길이
print("리스트 city의 길이:",len(city))











