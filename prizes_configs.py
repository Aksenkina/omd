from json_dict_processing import create_processor

# Вспомогательная функция, чтобы превратить год в число (если он пришел строкой)
def to_int(value):
    if value is not None:
        return int(value)
    return None

# Конфиг для призов
CONFIG_PRIZE = {
    "prize_amount": ["prizeAmount"],
    "prize_amount_adjusted": ["prizeAmountAdjusted"],
    "award_year": (["awardYear"], to_int),
    "category_en": ["category", "en"],
    "prize_status": ["prizeStatus"]
}

# Функция, которая возвращает готовый процессор для списка призов
def prize_processor():
    return create_processor(CONFIG_PRIZE, list_processor=True)