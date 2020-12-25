'''Мост (Bridge) - паттерн, структурирующий объекты.
Основная задача - отделить абстракцию от её реализации так,
чтобы то и другое можно было изменять независимо.
'''


class Pupil(object):
    # Базовый класс Учащиеся
    def current_class_pupil(self, age_pupil):
        raise NotImplementedError()


class Schoolchild(Pupil):
    # Подкласс Школьник
    def current_class_pupil(self,name, age_pupil):
        print(name,' выбран класс школьник' )
        print('''Школьник:
Получение начального образования
Получение неполного среднего образования
Получение полного среднего образования''')


class Student(Pupil):
    # Подкласс Студент
    def current_class_pupil(self,name, age_pupil):
        print(name,' выбран класс студент' )
        print('''Студент:
Получение степени бакалавр
Получение степени магистр
Получение степени исследователь''')


class ClassPupilBase(object):
    # Абстрактный Учащиеся
    def __init__(self, age_pupil):
        self._plan = self.get_plan(age_pupil)

    def get_plan(self, age_pupil):
        raise NotImplementedError()

    def current_class_pupil(self,name, age_pupil):
        self._plan.current_class_pupil(name,age_pupil)


class ClassPupil(ClassPupilBase):
    # Учащиеся
    def __init__(self, age_pupil):
        super(ClassPupil, self).__init__(age_pupil)
        self._age_pupil = 0  # текущий канал

    def get_plan(self, age_pupil):
    
        if 7 <= age_pupil < 18:
            return Schoolchild()
        if  age_pupil >= 18:
            return Student()
        
        
    def current_class_pupil(self, name, age_pupil):
        super(ClassPupil, self).current_class_pupil(name, age_pupil)
        self._age_pupil = age_pupil



name = 'Антон Калинин'
remote_control = ClassPupil( 18)
remote_control.current_class_pupil(name, 18)