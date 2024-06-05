'''Напишите функцию принимающую на вход только ключевые
параметры и возвращающую словарь, где ключ — значение
переданного аргумента, а значение — имя аргумента.
Если ключ не хешируем, используйте его строковое представление.'''

def get_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        try:
            hash(value)
            result[value] = key
        except TypeError:
            result[str(value)] = key
    return result

result = get_dict(one=11, two="str", three=True, four=None, five={2: 5}, six=[2, 6])
print(result)