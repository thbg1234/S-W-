'''
작성일:2024.5.3
작성자:컴퓨터공학부 202195056 석홍신
설명 :시퀀스 자료형 실습
    
'''

text1 = "안녕하세요."

text2 = ""
text3 = str()

text4 = "오늘은 화요일입니다."
print(text4)


'''
str()함수를 사용하여 다른 자료형을 문자열로 변환하여 세로운 문자열 생성
'''
#정수를 문자열로 생성
text5 = str(12345)
print("text5 = ",text5)
print("text5의 자료형:",type(text5))

#list[]로 문자열 생성
text6 = str([1,2,3])
print("text6 = ",text6)

#text6에 있는 문자열의 첫 번째 문자를 출력
print("text6[0] = ",text6[0])

#튜플()을 문자열 생성
text7 = str((1,2,3))
print("text7 = ",text7)

#text7에서 문자열의 세 번째 문자 출력
print("text7[2] = ",text7[2])

'''
대소문자 변환
'''
text8 = 'i like python language'
#문자열의 첫 문자만 대문자로 변환
print("첫 문자만 대소문자 변환 :",text8.capitalize())  #首字母大写

#모든 단어의 첫 문자만 대문자로 변환
print("모든 단어의 첫 문자만 대소문자 변환:",text8.title())  #全部首字母大写

#모든 대문자로 변환
text9 = text8.upper()
print("모든 대소문자 변환:",text9)  #全部字母变大写

#모든 소문자로 변환
text10 = text9.lower()
print("text10 = text9.lower():",text10)  #全部首字母小写

'''
문자열 찾기
'''
print(text10)
print("문자열에 'a'가 몇 개있나?",text10.count('a'))
print("문자열 인덱스 0~12사이에 'a'가 몇 개있나? ",text10.count('a',0,12))
print("문자열 인덱스 12번지 이후에 'a'가 몇 개있나?",text10.count('a',12))

'''
print("문자열 내의 '1'의 인덱스(위치)는?",text10.index('1'))
print("문자열 내의 '1'의 인덱스(위치)는?",text10.find('1'))

print("문자여ㅕㄹ 내의 '1'의 오른쪽부터 검색하면?",text10.rindex('1'))
print("문자여ㅕㄹ 내의 '1'의 오른쪽부터 검색하면?",text10.rfind('1'))
'''

#문자열에서 python의 위치는?
print("문자열 내의 python의 위치는?",text10.index('python'))

#대문자 python은 없으므로 발생
#print("문자열 내의 python의 위치는?",text10.index('python'))

#find 사용하면 없으면 -1값을 출력
print("문자열 내의 'python'의 위치는?",text10.find('Python'))

print("'i like'로 시작하는가?",text10.startswith("i like"))
print("'title'로 끝나는가?",text10.endswith("title"))

'''
문자열 결합
'''

list1 = ['1','2','3','4']
print("list1 = ",list1)

join1 = '-'.join(list1)
print("'-'와 리스트 결합(연결)",join1)

list2 = [1,2,3,4]
#join2 = '-'.join(list2)
#print("'-'와 리스트 결합(연결):",join2)

'''
문자열 분리
'''
text10 = 'i like python language'
print('text10:',text10)

list3 = text10.split()
print("문자열을 분리(스페이스로 분리):",list3)

text11 = 'i-like-python-language'
print('text11:',text11)
list4 = text11.split('-')
print("문자열을 분리('-'로 분리):")

#'python'을 기준으로 문자열을 나누어 튜프로 변환
tuple1 = text10.partition('python')
print("문지 변환:",tuple1)

print("'like'를'love'로 대체:",text10.replace('like','love'))

'''
문자열 검사
'''
text12 = 'I Like Python language'
print("모든 단어의 첫 문자가 대문자인가?",text12.istitle())

text13 = 'abc123'
print("문자열이 숫자와 문자로 구성되어 있나?",text13.isalnum())

text14 = '123456789'
print("문자열이 숫자만 구성되어 있나?",text14.isdigit())
print("문자열이 문자만 구성되어 있나?",text14.isalpha())


print("모든 문자가 대문자 인가?", text12.isupper())
print("모든 문자가 소문자 인가?", text12.islower())