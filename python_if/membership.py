# 멤버쉽 연산자 in 

mom_fruits = ['멜론', '수박', '배', '딸기']

favorite_fruits = ['사과', '수박', '배']

eat_list = []

for fruit in mom_fruits:
    if fruit in favorite_fruits:
        print("먹는다!")
        eat_list.append(fruit)
    else:
        print("안먹는다!")
print(eat_list)