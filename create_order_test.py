# Дмитрий Плотницкий, 7-я когорта — Финальный проект. Инженер по тестированию плюс
import data as d
import sender_stand_request as ssr


# Создать заказ
def create_order(body):
    response = ssr.request_create_order(d.headers, body)                   # получить ответ после создания заказа
    if response.status_code == 201:                                        # если ответ соответствует ожиданию (201)
        return response.json()['track']                                    # получить трек
    else:                                                                  # иначе
        print(f'[Ошибка] Получен статус {response.status_code}')           # вывести информацию о фактическом статуссе


# Получить инфо о заказе
def get_order(track):
    order_param = d.param.copy()                                           # скопировать параметры для работы
    order_param['t'] = track                                               # поместить в параметры трек с ключом t
    response = ssr.request_get_order(order_param)                          # получить информацию о заказе
    error_text = f'[Ошибка] Получен статус код: {response.status_code}'    # текст с ошибкой
    assert response.status_code == 200, error_text                         # Проверить, что статус равен 200


# Создание набора тест
def test_create_order():
    body = d.order_dict.copy()                                             # Получить тело запроса на создание заказа
    track = create_order(body)                                             # Создать заказ и получить трек
    get_order(track)                                                       # Получить информацию о заказе
