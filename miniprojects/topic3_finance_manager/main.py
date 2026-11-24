import storage

def program():
    JSON_data = storage.load_JSON()
    while True:
        menu_string = (f"Меню программы:\n"
                       "1. Добавить доход\n"
                       "2. Добавить расход\n"
                       "3. Показать баланс\n"
                       "4. Отчет по категориям\n"
                       "5. Выход\n")
        choose = storage.read_int(menu_string)
        match choose:
            case 1: add_income(JSON_data)
            case 2: add_expense(JSON_data)
            case 3: print(storage.get_balance(JSON_data))
            case 4: print(storage.report_by_category(JSON_data))
            case 5: break


def add_income(data):
    operation_type = input("Введите тип дохода: ")
    value = storage.read_int("Введите значение: ")
    storage.add_record(data, "income", operation_type, value)

def add_expense(data):
    operation_type = input("Введите тип расхода: ")
    value = storage.read_int("Введите значение: ")
    storage.add_record(data, "expense", operation_type, value)

if __name__ == "__main__":
    program()
