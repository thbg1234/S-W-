'''
작성일:2024.5.24
작성자:컴퓨터공학부 202195056 석홍신
설명 :학생 정보 입력되 파일의 애용을 출력하시오

    읽이 모드 => r
    파일 읽기 = readline() =>while True 사용
'''


with open("student.txt", "r", encoding="UTF-8") as f:
    while True:
        student = f.readline()
        if student == "":
            break
        
        print(student)
