def total(*args):
    summary = 0
    for i in args:
        summary += i
    return summary

print(total(1,2,3,4,5))