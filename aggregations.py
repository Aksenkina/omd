import statistics

def get_mean(data, field=None):  # Среднее
    if field is None:
        values = data 
    else:
        values = [row[field] for row in data if row.get(field) is not None]
        
    if not values:
        return 0
    return statistics.mean(values)

def get_median(data, field=None):  # Медиана
    if field is None:
        values = data
    else:
        values = [row[field] for row in data if row.get(field) is not None]
        
    if not values:
        return 0
    return statistics.median(values)

def get_top_n(data, field, n=5, reverse=True):  # Топ-n объектов 
    counts = {}
    for row in data:
        value = row.get(field)
        if value is not None:
            counts[value] = counts.get(value, 0) + 1    
    # Сортировка
    sorted_items = sorted(counts.items(), key=lambda item: item[1], reverse=reverse)
    return sorted_items[:n]
