def sum_digits(number):
    if number < 0:
        return None
    else:
        sumary = 0
        while(number != 0):
            sumary += number % 10
            number = number // 10

        return sumary
