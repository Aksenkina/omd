import json
import matplotlib.pyplot as plt
from laureates_configs import person_processor, org_processor
from dataset_helpers import filter_data, group_by
from aggregations import get_mean, get_median, get_top_n

# ЗАГРУЗКА И ПОДГОТОВКА ДАННЫХ

with open('laureates.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

process_person = person_processor()
process_org = org_processor()

laureates_data = []

for laureate in data['laureates']:
    if 'knownName' in laureate:
        processed = process_person(laureate)
        processed['type_'] = 'person'
        laureates_data.append(processed)
    elif 'orgName' in laureate:
        processed = process_org(laureate)
        processed['type_'] = 'org'
        laureates_data.append(processed)

persons = filter_data(laureates_data, {'type_': 'person'}) 

# ТЕХНИЧЕСКИЙ АНАЛИЗ

print(f"\n1. Всего записей: {len(laureates_data)}")

# Пропуски в данных
print("\n2. Пропуски в полях (и их доля):")
fields_to_check = ['name', 'gender', 'birth_year', 'country_birth', 'country_now']
for field in fields_to_check:
    missing = sum(1 for row in laureates_data if row.get(field) is None)
    share = (missing / len(laureates_data)) * 100
    print(f"  - {field}: {missing} пропусков ({share:.1f}%)")

# Анализ ID
print("\n3. Анализ ID:")
ids = [row['id'] for row in laureates_data if row.get('id')]
int_ids = [int(i) for i in ids if str(i).isdigit()]
if int_ids:
    print(f"Мин. ID: {min(int_ids)}, Макс. ID: {max(int_ids)}")
    
    # Проверка на дубликаты
    if len(ids) != len(set(ids)):
        print("Есть повторяющиеся ID")
    else:
        print("Повторяющихся ID нет")
        
    # Проверка на разрывы в отсортированном массиве
    sorted_ids = sorted(int_ids)
    gaps = []
    for i in range(len(sorted_ids) - 1):
        if sorted_ids[i+1] - sorted_ids[i] > 1:
            gaps.append((sorted_ids[i], sorted_ids[i+1]))
    print(f"Пар ID, различающихся более чем на 1 (разрывы): {len(gaps)}")
    if gaps:
        print(f"Примеры разрывов: {gaps[:3]}")

# 3. АНАЛИТИЧЕСКИЕ ФУНКЦИИ

def analyze_1_age():  # Средний и медианный возраст при награждении
    ages = []
    for p in persons:
        if p.get('birth_year') and p.get('prizes_relevant'):
            first_award_year = p['prizes_relevant'][0]['award_year']
            age = first_award_year - p['birth_year']
            if 0 < age < 100:
                ages.append(age)
    print("\nАнализ возраста при награждении")
    print(f"Средний возраст: {get_mean(ages):.1f} лет")
    print(f"Медианный возраст: {get_median(ages):.1f} лет")
    return ages

def analyze_2_top_countries():  # Топ-5 стран по рождению
    print("\nТоп-5 стран по рождению")
    top_countries = get_top_n(persons, 'country_birth', n=5)
    for country, count in top_countries:
        print(f"{country}: {count} лауреатов")
    return top_countries

def analyze_3_gender():  # Гендерное распределение лауреатов
    print("\nГендерное распределение")
    genders = {}
    for p in persons:
        g = p.get('gender')
        if g:
            genders[g] = genders.get(g, 0) + 1
    print(f"Мужчины: {genders.get('male', 0)}")
    print(f"Женщины: {genders.get('female', 0)}")
    return genders

def analyze_4_refusals():  # Отказы от премий
    print("\nОтказы от премий")
    refusals = []
    for p in laureates_data:
        if p.get('prizes_relevant'):
            for prize in p['prizes_relevant']:
                if prize.get('prize_status') == 'declined':
                    refusals.append(p['name'])
                    break
    print(f"Всего отказов: {len(refusals)}")
    if refusals:
        print(f"Примеры: {refusals[:3]}")

def analyze_5_categories_by_country():  # Топ-3 страны по количеству лауреатов по физике
    print("\nТоп-3 страны по физике")
    physics_persons = []
    for p in persons:
        if p.get('prizes_relevant'):
            if any(prize['category_en'] == 'Physics' for prize in p['prizes_relevant']):
                physics_persons.append(p)
    top_phys = get_top_n(physics_persons, 'country_birth', n=3)
    for country, count in top_phys:
        print(f"{country}: {count} физиков")

def analyze_6_dynamics_by_decade():  # Количество награждений по десятилетиям
    print("\nДинамика награждений по десятилетиям")
    decades = {}
    for p in persons:
        if p.get('prizes_relevant'):
            year = p['prizes_relevant'][0]['award_year']
            decade = (year // 10) * 10
            decades[decade] = decades.get(decade, 0) + 1
    sorted_decades = dict(sorted(decades.items()))
    for dec, count in sorted_decades.items():
        print(f"{dec}-е: {count} чел.")
    return sorted_decades

# 4. ЗАПУСК ВСЕГО АНАЛИЗА И ГРАФИКИ

analyze_1_age()
top_countries = analyze_2_top_countries()
analyze_3_gender()
analyze_4_refusals()
analyze_5_categories_by_country()
decades_data = analyze_6_dynamics_by_decade()

# Сетка графиков
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

if top_countries:
    countries = [item[0] for item in top_countries]
    counts = [item[1] for item in top_countries]
    ax1.bar(countries, counts, color='skyblue')
    ax1.set_title('Топ-5 стран по рождению')
    ax1.set_ylabel('Количество лауреатов')

if decades_data:
    decs = [str(k) for k in decades_data.keys()]
    dec_counts = list(decades_data.values())
    ax2.plot(decs, dec_counts, marker='o', color='orange', linewidth=2)
    ax2.set_title('Количество награждений по десятилетиям')
    ax2.set_xlabel('Десятилетие')
    ax2.set_ylabel('Количество')
    ax2.tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()