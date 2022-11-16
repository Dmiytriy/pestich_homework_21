from exceptions import BaseError
from logistics.courier import Courier
from logistics.request import Request
from logistics.shop import Shop
from logistics.store import Store



shop = Shop(
    items={
        'печенька': 3,
        'ноутбук': 2,
        'пылесос': 2,

    },
)

store = Store(
    items={
        'печенька': 10,
        'компьютер': 20,
    },
)

storages = {
    'магазин': shop,
    'склад': store,
}


def main():
    while True:
        for storage_name in storages:
            print(f'В {storage_name} хранится: {storages[storage_name].get_items()}')

        user_input = input(
            'Введите строку в формате "Доставить 3 печенька из склад в магазин".\n'
            'Введите "stop" или "стоп", чтобы завершить:\n'

        )

        if user_input in ('stop', 'стоп'):
            break

        try:
            request = Request(request_str=user_input, storages=storages)
        except BaseError as error:
            print(error.message)
            continue

        courier = Courier(request=request, storages=storages)

        try:
            courier.move()
        except BaseError as error:
            courier.cancel()
            print(error.message)


if __name__ == '__main__':
    main()

