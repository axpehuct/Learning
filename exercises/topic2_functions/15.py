nums = list(range(1,21))

print(list(map(lambda x : x**2, list(filter(lambda x : (x % 2), nums)))))

print(list(filter(lambda x : not (x % 3) and (x % 5), nums)))

print(list(map(lambda x : str(x), nums)))



