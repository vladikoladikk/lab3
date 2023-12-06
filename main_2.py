file_path = "goods.txt"

try:
    with open(file_path, "r") as file:
        lines = file.readlines()
except FileNotFoundError:
    print(f"Файл {file_path} не найден.")
    exit()

products = []

total_cost = 0

for line in lines:
    parts = line.strip().split()
    if len(parts) == 2:
        product_name, cost = parts[0], float(parts[1])
        products.append((product_name, cost))
        total_cost += cost

print("Товары с ценой от 10 до 50 рублей:")
for product, cost in products:
    if 10 <= cost <= 50:
        print(f"{product}: {cost} рублей")

average_cost = total_cost / len(products)
print(f"Средняя стоимость всех товаров: {average_cost:.2f} рублей")
