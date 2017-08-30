def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
        print("Da number is" + str(number))
    if number == 1:
        print("Da number is" + str(number))
