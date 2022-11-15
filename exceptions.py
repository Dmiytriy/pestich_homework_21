class BaseError(Exception):
    message = 'Неизвестная ошибка'


class NotEnoughSpaceError(BaseError):
    message = 'Недостаточно места'

class UnknownItemError(BaseError):
    message = 'Неизвестный товар'

class NotEnoughGoodsError(BaseError):
    message = 'Недостаточно товара'

class BadRequestError(BaseError):
    message = 'Неправильный запрос'

class UnknownWarehouseError(BaseError):
    message = 'Неизвестный склад'

class TooMuchNamesError(BaseError):
    message = 'Слишком много наименований'
