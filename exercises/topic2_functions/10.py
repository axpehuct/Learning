def plural(n, one, few, many):
    if n % 10 == 1 and n % 100 != 11:
        return one
    elif (n % 10 >= 2 and n % 10 <= 4) and not (n % 100 >= 12 and n % 100 <= 14):
        return few
    else:
        return many