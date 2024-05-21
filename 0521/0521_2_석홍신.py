'''
작성일:2024.5.21
작성자:컴퓨터공학부 202195056 석홍신
설명 :
'''



students = {}
for i in range(5):
    id_num = int(input(f"{i+1}번 학생 학번을 입력하세요: "))
    phone = int(input(f"{i+1}번 학생 전화번호를 입력하세요: "))
    students[id_num] = phone

print("학생 정보가 완성되었습니다")
print()

for id_num, phone in students.items():
    print(id_num, ":", phone)

while True:
    id_num = int(input("검색할 학번을 입력하세요 (종료: 0): "))

    if id_num == 0:
        print("프로그램을 종료합니다")
        break
    
    if id_num in students:
        print("입력한 학생의 전화번호 :", students[id_num])
    else:
        print("입력한 학생의 정보가 없습니다")

