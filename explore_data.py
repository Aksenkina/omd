import json

with open('laureates.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# ЧТЕНИЕ СЫРЫХ ДАННЫХ
# # Ключи на самом верхнем уровне
# print("Ключи в файле:", data.keys())

# # Первый лауреат
# first_laureate = data['laureates'][0]
# print("\nПервый лауреат:")
# print(first_laureate)

# ПРОВЕРКА ПРОЦЕССОРОВ
from laureates_configs import person_processor, org_processor

# 5 лауреатов для проверки
laureates = data['laureates'][:5]

# Процессоры 
process_person = person_processor()
process_org = org_processor()

# Проходимся по каждому лауреату
for laureate in laureates:
    # Определяем, человек это или организация
    if 'knownName' in laureate:
        processed = process_person(laureate)
        processed['type_'] = 'person' 
    elif 'orgName' in laureate:
        processed = process_org(laureate)
        processed['type_'] = 'org'
    else:
        continue

    print(f"Тип: {processed['type_']}")
    print(f"Имя/Название: {processed['name']}")
    print(f"Год рождения/основания: {processed.get('birth_year') or processed.get('founded_year')}")
    print(f"Количество призов: {len(processed['prizes_relevant']) if processed['prizes_relevant'] else 0}")
    
    # Первый приз (проверка prize_processor)
    if processed['prizes_relevant']:
        first_prize = processed['prizes_relevant'][0]
        print(f"Первый приз: {first_prize['category_en']}, год {first_prize['award_year']}, сумма {first_prize['prize_amount']}")

