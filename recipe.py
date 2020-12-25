# coding: utf-8

"""
Декоратор (Decorator, Wrapper) - паттерн, структурирующий объекты.
Динамически добавляет объекту новые обязанности.
Является гибкой альтернативой порождению подклассов с целью расширения функциональности.
"""

class Time(object):
    # Срок хранения
    def __init__(self, time):
        self._time = time
        print ('Срок хранения 3 месяца')

    def __getattr__(self, item):
        return getattr(self._time, item)

    def long(self):
        # расширяем функциональность объекта добавляя возможность продлить рецепт
        print('%s, срок хранения продлен на 1 месяц' % self._time._name)

class Recipe(object):
    # Назначение врача
    def __init__(self, name):
        self._name = name

    def say(self):
        print('Принимать 2 раза в день по одной таблетке %s' % self._name)

recipe = Recipe('Лекарство Арбидол')

recipe_time = Time(recipe)
recipe_time.long()  # Лекарство Арбидол срок хранения на 1 месяц
recipe_time.say()  # Принимать 2 раза в день по одной таблетке

