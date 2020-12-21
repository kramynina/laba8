# coding: utf-8

"""
Приспособленец (Flyweight) - паттерн, структурирующий объекты.
Использует разделение для эффективной поддержки множества мелких объектов.
"""

import weakref


class Tape(object):
    # Приспособленец лента
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class TapeFactory(object):
    # Фабрика приспособленцев
    _attribute = weakref.WeakValueDictionary()

    @classmethod
    def get_attribute(cls, name):
        value = cls._attribute.get(name)
        if value is None:
            value = Tape(name)
            cls._attribute[name] = value
        return value


class Posy(object):
    # Букет
    def __init__(self, flower, color, herb, attribute_name):
        # Составляющие букета (цветы, зелень) - внутреннее состояние (т.к. они уникальны для каждой метки)
        self._flower = flower
        self._color = color
        self._herb = herb
        # Атрибут (упаковочная лента) - внешнее состояние которое может быть общим у разных меток
        self._attribute = TapeFactory.get_attribute(attribute_name)
    def __str__(self):
        args = (self._attribute, self._color, self._flower, self._herb)
        return 'Атрибут: {}; Состав букета: ({}, {}, {})'.format(*args)


posy0 = Posy('Белые', 'Розы', 'Гипсофила', 'Упаковочная лента')
posy1 = Posy('Желтые', 'Тюльпаны', 'Папоротник', 'Упаковочная лента')

print (posy0)
print (posy1)

