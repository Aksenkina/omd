days = [
    {"day": "пн", "orders": 20, "revenue": 40_000, "returns": 2},
    {"day": "вт", "orders": 16, "revenue": 19_200, "returns": 4},
    {"day": "ср", "orders": 25, "revenue": 55_000, "returns": 1},
    {"day": "чт", "orders": 10, "revenue": 12_000, "returns": 3},
    {"day": "пт", "orders": 30, "revenue": 48_000, "returns": 3},
]

#Выручка за всю неделю
revenue_for_week = sum(day['revenue'] for day in days)
print(f'Выручка за всю неделю: {revenue_for_week}')

#День с самой большой выручкой
best_revenue_day = max(days, key=lambda day: day['revenue'])
print(f'День с самой большой выручкой: {best_revenue_day}')

#Средняя выручка на один заказ в каждый день
print('Средняя выручка на один заказ:')
for day in days:
    avg_revenue = day['revenue'] / day['orders']
    print(f"{day['day']}: {avg_revenue}")

#Дни, где возвратов больше 20% заказов
returns_twenty_percents = [day['day'] for day in days if day['returns'] / day['orders'] > 0.2]
print(f'Дни, где возвратов больше 20% заказов: {returns_twenty_percents}')
