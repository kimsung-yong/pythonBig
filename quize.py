# 문제1
# gender = input("성별을 입력하세요 ex 남자 여자")
# age = int(input("나이를 입력하세요"))
#
# human = {"gender": gender, "age": age}
# list1 = [human]
#
# for i in list1:
#     if list1[0].get("gender") == '남자':
#         print("적립금 두배.")
#         # break
#     elif list1[0].get("age") >= 20:
#         print("적립금 두배.")
#         # break
#     else:print("적립금 1.5배")
#     # break


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


# # 문제 3
# a = int(input("1부터 더할값을 입력하세요"))
# temp = 0
# for i in range(1,a+1):
#     temp += i
# print(temp)

# # 문제 4
# word_list = ['scar','kindly','do','learn']
# index = 0
# for i in word_list:
#     word_list[index] = 'un' + i
#     ++index
#     print(word_list[index])

# # 문제 5
# st = 'abcde'
# temp = 0
# for i in st:
#     print(str(temp)+'번째 문자는'+i+'입니다')
#     temp+=1

# # 문제 6
# asf = int(input('팩터리얼을 값을 구할 숫자를 입력하세요'))
# temp = 1
# for i in range(1,asf+1):
#     temp = temp * i
#     if i != asf:
#         print(str(i) + '*', end='')
#     else:print(str(i))
# print(temp)

# # 문제 7
# mList = ['asd','sdse',11,22,44,'11']
# print(mList[2])
# for i in range(len(mList)):
#     if type(mList[i]) == str:
#         print(mList[i] + "는 문자입니다.")
#     else: print(str(mList[i]) + "는 숫자입니다.")

# 문제 8
# for i in range(1,6):
#     star = ''
#     j=1
#     while j<=i:
#         star+='*'
#         j+=1
#     print(star)

# # 문제 9
# aa = 0
# while 1:
#
#     i = int(input('덧셈을 하고 싶은 양의 정수를 입력하세요. 0 입력시 종료'))
#     if i ==0:
#         break
#     else:
#         print(i)
#         aa += i
# print("총 합은 "+ str(aa) + '입니다')

# # 문제 10
# score =[]
# i = 0
# print("점수를 입력하세요")
# while 1:
#     point = int(input())
#     score.append(point)
#
#     if point ==0:
#         break
#     elif score[i] > 60:
#         print(str(i+1) + '번 학생 통과')
#         i += 1
#     elif score[i] <=60:
#         print(str(i+1) + '번 학생 불합격')
#         i += 1

# # 문제 11
# while 1:
#     num = int(input('홀수 짝수 구별 하실 수를 입력하여 주세요.(종료:0)'))
#     if num % 2 == 1:
#         print('%s는 홀수 입니다' % num)
#     elif num == 0:
#         print('EXIT')
#         break
#     else:print('%s는 짝수 입니다.' % num)

# # 문제 12
# print('높이를 입력하세요')
# high = float(input())
# i=0
# while 1:
#    high /=2
#    if high<0.00001:
#        break
#    i += 1
# print('공이 튀긴횟수는 %s입니다'% i)

# # 문제 13
# def is_odd(a):
#     if a%2 ==1:
#         print("홀수")
#     else:print("짝수")
#
# a =int(input("판별할 숫자를 입력하세요"))
# is_odd(a)

# # 문제 14
# def avg(*args):
#     i = 0
#     sum = 0
#     while i <= len(args[0]):
#         sum += args[0][i]
#         i += 1
#         if i == len(args[0]):
#             break
#     agv = sum /len(args[0])
#
#     print('평균은 %d 입니다' % agv)
# print('수를 입력해주세요')
# b = []
# while 1:
#     a = int(input())
#     if a == 0:
#         break
#     else:b.append(a)
#     # print(b)
#
# avg(b)

# # 문저 15 결과가 다른 하나는 ? 3
# print("you" "need" "python")
# print("you"+"need"+"python")
# print("you", "need", "python")
# print("".join(["you", "need", "python"]))

# 문제 16
# 다음은 "test.txt"라는 파일에 "Life is too short" 문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램이다.
#
# f1 = open("test.txt", 'w')
# f1.write("Life is too short")
#
# f2 = open("test.txt", 'r')
# print(f2.read())
# 이 프로그램은 우리가 예상한 "Life is too short"라는 문장을 출력하지 않는다. 우리가 예상한 값을 출력할 수 있도록 프로그램을 수정해 보자.
# f1 = open("test.txt", 'w')
# # f1.write("Life is too short")
# # f1.close()
# # f2 = open("test.txt", 'r')
# # a = f2.read()
# # print(a)

#문제 17
# 사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해 보자. (단 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야 한다.)
# a = input()
# t1 = open("test.txt",'a')
# t1.write(a+"\n")
