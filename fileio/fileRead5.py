#hp=280
hit=""
try:
    f=open("save.txt","r")
    hp=int(f.read())
    f.close()
    print("저장된 파일을 읽어오는중...")
except NameError:
    print(str(hp))
except:
    print("저장된 파일을 찾을 수 없음...")



print("현재 체력은 %d 입니다" %hp)
#while hit != "save" and hp > 0:
while hp > 0:
    hit=input("데이미지를 몇 입었습니까:")
    if hit=="save":
        f=open("save.txt","w")
        f.write(str(hp))
        f.close()
        break
    else:
        hit=int(hit)
        hp=hp-hit
        print("체력이 %d 남았습니다" %hp)