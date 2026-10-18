orders = [
    {"id": 1, "buyer": "anya", "status": "delivered", "amount": 900},
    {"id": 2, "buyer": "boris", "status": "returned", "amount": 4_500},
    {"id": 3, "buyer": "anya", "status": "delivered", "amount": 1_500},
    {"id": 4, "buyer": "vera", "status": "delivered", "amount": 3_200},
    {"id": 5, "buyer": "boris", "status": "delivered", "amount": 700},
    {"id": 6, "buyer": "gleb", "status": "returned", "amount": 2_100},
]

#На какую сумму оформили возвраты
returned_amounts = [order['amount'] for order in orders if order['status'] == 'returned']
returned_sum = sum(returned_amounts)
print(f'На какую сумму оформили возвраты: {returned_sum}')

#Кто хотя бы раз вернул заказ
buyers_with_returns = {order['buyer'] for order in orders if order['status'] == 'returned'}
print(f'Кто хотя бы раз вернул заказ: {buyers_with_returns}')

#Cколько заказов доставлено покупателю
delivered_orders = [order for order in orders if order['status'] == 'delivered']
delivered_orders_count = len(delivered_orders)
print(f'Cколько заказов доставлено покупателю: {delivered_orders_count}')

#Средний чек доставленных заказов
delivered_amounts = [order['amount'] for order in orders if order['status'] == 'delivered']
delivered_sum = sum(delivered_amounts)
avg_cheсk_delivered = delivered_sum / delivered_orders_count
print(f'Cредний чек доставленных заказов: {avg_cheсk_delivered}')