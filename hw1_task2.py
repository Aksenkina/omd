def main():
    from collections import Counter
    queries = [
        "чехол",
        "iphone",
        "чехол",
        "наушники",
        "iphone",
        "iphone",
        "кабель",
        "чехол",
        "iphone",
    ]

    # Считает, сколько раз встретился каждый запрос
    count_queries = Counter(queries)

    # Какаой запрос самый популярный
    most_frequent_query = count_queries.most_common(1)[0]

    # Какую долю из всех запросов составляет самый популярный
    share_of_most_frequent_query = most_frequent_query[1] / len(queries)

    # Запросы, которые встретились один раз
    single_queries = [query for query, count in count_queries.items() if count == 1]
    
    print('Cколько всего поисковых запросов в ленте:', len(queries)) #сколько всего поисковых запросов в ленте
    print('Cколько раз ввели каждый запрос:', count_queries) #сколько раз ввели каждый запрос
    print(f'Какой запрос вводили чаще всего: {most_frequent_query[0]}, всего его ввели {most_frequent_query[1]} раз(а)') #какой запрос вводили чаще всего
    print(f'Какую долю всех поисков он занимает: {share_of_most_frequent_query}') #какую долю всех поисков он занимает
    print(f'Какие запросы встретились один раз: {single_queries}') #какие запросы встретились один раз

if __name__ == '__main__':
    main()