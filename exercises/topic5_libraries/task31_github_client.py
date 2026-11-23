import requests

def start():
    while True:
        username = input("Введите никнейм пользователя Github: ")
        if username == "-":
            break
        try:
            response = requests.get(f"https://api.github.com/users/{username}", timeout=5)
        except requests.exceptions.RequestException:
            print("Ошибка сети.")
            break
        if response.status_code == 404:
            print("Пользователь не найден. Попробуйте еще раз")
        elif response.status_code != 200:
            print(f"Ошибка, код ошибки: {response.status_code}")
        else:
            data = response.json()
            print(f"""Имя пользователя:{data["name"] if data["name"] is not None else "Не указано"}
Компания: {data["company"] if data["company"] is not None else "Не указано"}
Число репозиториев: {data["public_repos"]}
Число подписчиков: {data["followers"]}""")
            
if __name__ == "__main__":
    start()