def filter_data(data, conditions):  # Аналог SQL WHERE
    filtered = []
    for row in data:
        match = True
        for key, expected_value in conditions.items():
            if row.get(key) != expected_value:
                match = False
                break
        if match:
            filtered.append(row)
    return filtered


def group_by(data, keys):  # Аналог SQL GROUP BY
    grouped = {}
    for row in data:
        group_key = tuple(row.get(k) for k in keys)
        
        if group_key not in grouped:
            grouped[group_key] = []
        grouped[group_key].append(row)
    return grouped