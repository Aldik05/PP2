import re

# Открываем файл и читаем содержимое
with open(r"C:\Users\ACER\Desktop\PP2\PP2-1\Lab5\row.txt", "r", encoding="utf-8") as file:
    receipt_text = file.read()


# Извлекаем БИН
bin_pattern = r"БИН\s(\d+)"
bin_match = re.search(bin_pattern, receipt_text)
bin_number = bin_match.group(1) if bin_match else "Не найдено"

# Извлекаем дату и время
date_pattern = r"Время:\s([\d.]+)\s([\d:]+)"
date_match = re.search(date_pattern, receipt_text)
purchase_date, purchase_time = date_match.groups() if date_match else ("Не найдено", "Не найдено")

# Извлекаем итоговую сумму
total_pattern = r"ИТОГО:\s([\d\s]+,\d{2})"
total_match = re.search(total_pattern, receipt_text)
total_amount = total_match.group(1).strip() if total_match else "Не найдено"

# Извлекаем товары
item_pattern = r"\d+\.\s(.+?)\n(\d+,\d+)\s[xX]\s([\d\s]+,\d+)\n([\d\s]+,\d+)"
items = re.findall(item_pattern, receipt_text)

# Формируем список товаров
parsed_items = []
for item in items:
    name, qty, price, total = item
    parsed_items.append({
        "Название": name.strip(),
        "Количество": qty.replace(",", "."),
        "Цена за единицу": price.replace(" ", "").replace(",", "."),
        "Общая стоимость": total.replace(" ", "").replace(",", ".")
    })

# Вывод результатов
print("БИН:", bin_number)
print("Дата покупки:", purchase_date)
print("Время покупки:", purchase_time)
print("Итоговая сумма:", total_amount)
print("\nТовары:")
for item in parsed_items:
    print(f"{item['Название']} — {item['Количество']} шт. x {item['Цена за единицу']} = {item['Общая стоимость']}")

