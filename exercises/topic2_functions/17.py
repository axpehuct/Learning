def read_int(prompt):
    while True:
        value = input(prompt)
        try:
            return int(value)
        except ValueError:
            print(f"«{value}» — не число, попробуйте ещё раз.")

read_int("abc")
read_int("12a")
read_int("42")