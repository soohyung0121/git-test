import random

def odd_number(number):
    number = random.randrange(1, 100)
    if number & 2 == 0:
        print("2의 배수.")
    elif number & 3 == 0:
        print("3의 배수")
    elif number & 5 == 0:
        print("5의 배수")
    elif number & 7 == 0:
        print("7의 배수")
    elif number & 9 == 0:
        print("그냥 넣어봤습니다.")
    else:
        print("숫자입니다.")