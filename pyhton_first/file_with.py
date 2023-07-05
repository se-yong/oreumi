with open("a.txt", "r") as f:
    content = f.read()
    print(content)
# <--------------------------------
print(content)
    
#  file.close() 안해도 됨 -> with 사용시 자동으로 파일 닫아줌
#  여러개의 파일을 반복적으로 열때는 .open() 
#  for i in range(0,50):
#       f[i].open()