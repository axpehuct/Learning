products = ["хлеб", "молоко", "сыр"]
prices = [45, 89, 320]

enums = zip(products, prices)

for i, enum in enumerate(enums, 1):
    product, price = enum
    print(f"{i}. {product} - {price} руб.")