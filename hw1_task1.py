def main():
    moscow = {201, 202, 203, 204}
    kazan = {203, 204, 205, 206}

    print('Можно забрать в любом из двух городов:', moscow.intersection(kazan))  # что можно забрать в любом из двух городов
    print('Есть только в Москве:', moscow.difference(kazan))  # что есть только в Москве
    print('Есть только в Казани:', kazan.difference(moscow))  # что есть только в Казани
    print('Всего разных товаров на обоих складах:', len(moscow.union(kazan)))  # сколько разных товаров на обоих складах вместе

if __name__ == '__main__':
    main()