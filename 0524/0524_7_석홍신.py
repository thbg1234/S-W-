'''
작성일:2024.5.24
작성자:컴퓨터공학부 202195056 석홍신
설명 :readlines()메소드 사용법
        readlines()메소드는 파일의 모든 읽어 들인다
        readline()메소드와 다른점은 각각 줄을 읽어 리스트로 반환한다
        readlines()메소드는 파일로부터 읽어 들인
        한 줄을 리스트 한 항목으로 만든다.
'''


with open("test2.txt", "r", encoding="UTF-8") as f:
    textlist = f.readlines()
    
    print(textlist)
    print("textlist의 타입:", type(textlist))