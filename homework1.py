a = int(input())
b = str(input())

try:
    if(b == 0):
        raise ZeroDivisionError("привет 0")
    elif(type(a) != type(b)):
        raise TypeError("")
    else:
        print(a / b)
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
