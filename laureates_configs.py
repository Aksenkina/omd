from json_dict_processing import create_processor
from prizes_configs import prize_processor

# Вспомогательная функция для извлечения года из строки даты (формат "YYYY-MM-DD")
def process_year(date_string):
    if date_string is None:
        return None
    # Берем первые 4 символа (год) и превращаем в число
    year_str = date_string[:4]
    return int(year_str)

# Конфиг для человека-лауреата
CONFIG_PERSON = {
    "id": ["id"],
    "name": ["knownName", "en"],
    "gender": ["gender"],
    "birth_year": (["birth", "date"], process_year),
    "country_birth": ["birth", "place", "country", "en"],
    "country_now": ["birth", "place", "countryNow", "en"],
    # Список призов обрабатываем функцией prize_processor()
    "prizes_relevant": (["nobelPrizes"], prize_processor())
}

# Конфиг для организации-лауреата
CONFIG_ORG = {
    "id": ["id"],
    "name": ["orgName", "en"],
    "founded_year": (["founded", "date"], process_year),
    "country_founded": ["founded", "place", "country", "en"],
    "country_now": ["founded", "place", "countryNow", "en"],
    "prizes_relevant": (["nobelPrizes"], prize_processor())
}

# Функции-процессоры для удобного вызова в ноутбуке
def person_processor():
    return create_processor(CONFIG_PERSON, list_processor=False)

def org_processor():
    return create_processor(CONFIG_ORG, list_processor=False)