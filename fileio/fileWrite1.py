#f=open("a.txt","w")
#f.write("Welcome Python\npythonpython\n")
#f=open("a.txt","a")
#f.writelines(["\nlist4,list5,list6\n"])
a=0
f=open("a.txt",'a')
while a<10:
    data="%d 숫자\n" %a
    f.write(data)
    a+=1
f.close()