# global_var = 100

# def my_func(global_var):

#     local_var = 50
#     global_var += 50

#     print("전역 변수:", global_var)
#     print("지역 변수:", local_var)

#     return global_var

# global_var = my_func(global_var)
# print("전역 변수:", global_var)

def get_person():
    return "박세용", 29, "parksae0428@gmail.com"

name, age, email = get_person()
print(f"이름: {name}, 나이 {age}, 이메일: {email}")