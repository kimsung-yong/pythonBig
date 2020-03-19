def some_function():
    print("1~10 사이의 수를 입력하세요")
    num = int(input())
    if num < 1 or num > 10:
        raise Exception("유효하지않은 숫자 입니다. : %s" % num)
    else:
        print("입력한수는 {0} 입니다".format(num))


try:
    some_function()
except Exception as err:
    print("예외가 발생했습니다. {0}".format(err))
