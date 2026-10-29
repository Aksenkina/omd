def main():
    reviews = [
        {"id": 1, "product": "Чехол", "stars": 5},
        {"id": 1, "product": "Чехол", "stars": 3},
        {"id": 1, "product": "Чехол", "stars": 4},
        {"id": 2, "product": "Наушники", "stars": 2},
        {"id": 2, "product": "наушники", "stars": 2},
        {"id": 2, "product": "НАУШНИКИ", "stars": 5},
        {"id": 3, "product": "Планшет", "stars": 5},
        {"id": 4, "product": "Колонка", "stars": 4},
        {"id": 4, "product": "Колонка", "stars": 4},
        {"id": 5, "product": "Кабель", "stars": 1},
    ]

    # Приведение названий к одному регистру
    print('Данные после преведения названий к одному регистру:')
    for review in reviews:
        review['product'] = review['product'].lower()
        print(review)
    print('-' * 45)

    # Средняя оценка каждого товара
    rating_by_product = {}
    for review in reviews:
        rating_by_product.setdefault(review['product'], []).append(review['stars'])

    print('Средняя оценка каждого товара:')
    for product, stars in rating_by_product.items():
        avg = sum(stars) / len(stars)
        print(f'{product}: {avg}')

    # Худший товар по средней оценке среди тех, у кого хотя бы два отзыва
    products_with_two_reviews = {
        product: stars 
        for product, stars in rating_by_product.items() 
        if len(stars) >= 2
        }

    worst_product = min(products_with_two_reviews, key=lambda product: sum(products_with_two_reviews[product]) / len(products_with_two_reviews[product]))
    print(f'Худший товар по средней оценке среди тех, у кого хотя бы два отзыва: {worst_product}')

    # Сколько отзывов на 1 или 2 звезды
    one_two_stars_reviews_count = len([review for review in reviews if review['stars'] <= 2])
    print(f'Сколько отзывов на 1 или 2 звезды: {one_two_stars_reviews_count}')

    # Какую долю всех отзывов они составляют
    share_one_two_stars_reviews = one_two_stars_reviews_count / len(reviews)
    print(f'Какую долю всех отзывов они составляют: {share_one_two_stars_reviews}')

if __name__ == '__main__':
    main()