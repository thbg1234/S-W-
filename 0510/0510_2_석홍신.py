fruits = []

for i in range(5):
    fruit_name = input(str(i+1)+". 좋아하는 과일 이름을 입력하세요:")
    fruits.append(fruit_name)
    
print("입력한 과일 리스트:",fruits)

print()

favo_fruit = input("과일 이름을 입력하세요:")

if favo_fruit in fruits:
    print(f"{favo_fruit}는 당신이 좋아하는 과일입니다.")
else:
    print(f"{favo_fruit}는 당신이 좋아하는 과일이 아닙니다.")