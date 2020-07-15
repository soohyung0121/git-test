import random

def odd_number(number):
    number = random.randrange(1, 100)
    if number & 2 == 0:
        print("2의 배수.")
    else:
        print("숫자입니다.")