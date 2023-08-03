import requests
import configuration as c


# Запрос на создание заказа
def request_create_order(headers, body):
    return requests.post(c.URL + c.CREATE_NEW_ORDER_PATH, headers=headers, json=body)


# Получить инфо о заказе
def request_get_order(param):
    return requests.get(c.URL + c.GET_ORDER_PATH, params=param)
