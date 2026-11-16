import json

def extract_nested_value(obj, keys):  # Извлекает значение из вложенных структур данных по цепочке ключей
    current = obj
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return None
    return current

def process_dictionary_with_config(dictionary, config):  # Обрабатывает один словарь согласно словарю-конфигу
    result = {}
    for attribute, path_info in config.items():
        if isinstance(path_info, list):
            value = extract_nested_value(dictionary, path_info)
            result[attribute] = value
        elif isinstance(path_info, tuple):
            path = path_info[0]
            func = path_info[1]
            value = extract_nested_value(dictionary, path)
            if value is not None:
                result[attribute] = func(value)
            else:
                result[attribute] = None
    return result

def process_list_of_dicts_with_config(list_of_dicts, config):  # Обрабатывает список словарей
    result_list = []
    for dictionary in list_of_dicts:
        processed_dict = process_dictionary_with_config(dictionary, config)
        result_list.append(processed_dict)
    return result_list

def create_processor(config, list_processor=False):  # Создает готовый процессор с предзагруженной конфигурацией
    if list_processor:
        def processor_for_list(data):
            return process_list_of_dicts_with_config(data, config)
        return processor_for_list
    else:
        def processor_for_dict(data):
            return process_dictionary_with_config(data, config)
        return processor_for_dict

# Валидация (проверка)
if __name__ == "__main__":
    test_dict = {"id": "102", "nested": {"data": {"value": 42}}, "name": "Aage N. Bohr"}
    test_config = {"test_id": ["id"], "test_value": ["nested", "data", "value"]}
    
    assert extract_nested_value(test_dict, ["nested", "data", "value"]) == 42
    result = process_dictionary_with_config(test_dict, test_config)
    assert result["test_id"] == "102"
    print("Все тесты пройдены")