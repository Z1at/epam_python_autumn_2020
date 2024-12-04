# Декораторы в Python — это функции, которые принимают другую функцию в качестве аргумента,
# добавляют к ней дополнительную функциональность и возвращают функцию с изменённым поведением
# С помощью декораторов мы можем изменять поведение декорируемой функции
from typing import Callable


def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper
# По сути, для этого и используются декораторы, мы можем делать определённую надстройку над нашей функцией


# Декоратор для того, чтобы параметры, которые уже были когда-то переданы в нашу функцию не выполняли функцию ещё раз,
# А просто возвращает уже сохранённое значение
def cache(func: Callable) -> Callable:
    used_parameters = {}

    def cache_func(*args, **kwargs):
        parameters = args + tuple(kwargs.keys()) + tuple(kwargs.values())
        if parameters not in used_parameters:
            used_parameters[parameters] = func(*args, **kwargs)

        return used_parameters[parameters]

    return cache_func