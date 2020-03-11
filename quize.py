#문제1
gender = input("성별을 입력하세요 ex 남자 여자")
age = input("나이를 입력하세요")

human = {"gender": gender, "age": age}
list1 = [human]

print(list1.index(0))
for i in list1:
    if human["gender"] == '남자':
        print("적립금 두배.")
        # break
    elif int(human["age"]) >= 20:
        print("적립금 두배.")
        # break
    else:print("적립금 1.5배")
    # break



# # 문제2
# num1,num2,num3 = int(input("첫번째수를 입력하세요")), int(input("두번째수를 입력하세요")), int(input("세번째수를 입력하세요"))
#
# nList = [num1,num2,num3]
# nList.sort()
# # nList.reverse()
# sList = nList[-1]
# print(sList)
# # sList = nList(0)
# # print(sList)


