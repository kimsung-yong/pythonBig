try:
    f=open("test.txt","r")
except FileNotFoundError:
    print("파일이 존재하지 않음!!!")