'''
작성일:2024.5.24
작성자:컴퓨터공학부 202195056 석홍신
설명 :사용자로부터 5명의 학생의 이름과 3과목의 성적을 입력 받아
        student .txt 파일에 저장하세요
        
        write()메소드를 사용합니다
        모드 설정:w
        open()+close()
        with open()
    [알고리즘]
    1.학생 이름과 성적을 저장 할 파일을 오픈
'''
with open ("student.txt","w",encoding="UTF-8") as f:
    for i in range(1,6):
        student = input(str(i)+"학생 이름과 3과목 성적 입력(예:홍길동 78 98 100):")
        f.write(student+"\n")