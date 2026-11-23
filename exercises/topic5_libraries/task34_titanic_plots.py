import pandas as pd
import matplotlib.pyplot as plt

def start(filename):
    plt.figure(figsize=(15, 4))
    df = pd.read_csv("titanic.csv")
    survivor_percent_by_category = df.groupby("Pclass")["Survived"].mean()
    make_survivor_rate_graph(survivor_percent_by_category)
    age_rate = df["Age"].dropna()
    make_age_rate_graph(age_rate)
    sex_rate = df.groupby("Sex")["Survived"].mean()
    make_sex_rate_graph(sex_rate)
    plt.tight_layout()
    plt.savefig(filename)
    plt.show()
    print(f"Графики сохранены в {filename}")
    
def make_survivor_rate_graph(survivor_rate):
    plt.subplot(1, 3, 1)
    plt.bar(["1 класс", "2 класс", "3 класс"], survivor_rate)
    plt.title("Доля выживших по классам")
    plt.ylabel("Доля выживших")
    
def make_age_rate_graph(age_rate):
    plt.subplot(1, 3, 2)
    plt.hist(age_rate, bins=30)
    plt.title("Распределение возрастов пассажиров")
    plt.xlabel("Возраст")
    plt.ylabel("Кол-во")

def make_sex_rate_graph(sex_rate):
    plt.subplot(1, 3, 3)
    plt.bar(sex_rate.index.map({"female":"Женщины", "male":"Мужчины"}), sex_rate.values)
    plt.title("Доля выживших по полу")
    plt.ylabel("Доля выживших")
    

if __name__ == "__main__":
    start("titanic_plots.png")
