import pandas as pd

def start():
    df = pd.read_csv("titanic.csv")
    total_passengers = df.shape[0]
    total_survive = df[df["Survived"] == 1].shape[0]
    print(f"Количество пассажиров: {total_passengers}")
    print(f"Количество выживших: {total_survive}")
    print(f"Доля выживших: {round((total_survive / total_passengers), 4)}")
    print(df.info())
    mean_age = df["Age"].mean()
    print(f"Средний возраст пассажиров: {round(mean_age, 4)}")
    survivor_percent_by_category = df.groupby("Pclass")["Survived"].mean()
    print(f"Доля выживших по классам: {survivor_percent_by_category}")
    oldest_passenger_idx = df.idxmax()["Age"]
    youngest_passenger_idx = df.idxmin()["Age"]
    print(f"Самый старый пассажир: {df.loc[oldest_passenger_idx, "Name"]} Возраст:{df.loc[oldest_passenger_idx, "Age"]}")
    print(f"Самый молодой пассажир: {df.loc[youngest_passenger_idx, "Name"]} Возраст:{df.loc[youngest_passenger_idx, "Age"]}")

if __name__ == "__main__":
    start()
