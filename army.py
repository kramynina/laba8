def main():

    class GrandElement:

        def __init__(self, *args):
            self.name = args[0]

        def printDetails(self):
            print("\t", end="")
            print(self.name)

    class ChildElement:

        def __init__(self, *args):
            self.name = args[0]
            self.grandren = []

        def printDetails(self):
            print("\t", end="")
            print(self.name)
            for grand in self.grandren:
                print("\t\t", end="")
                grand.printDetails()

        def appendGrand(self, grand):
            self.grandren.append(grand)

        def removeGrand(self, grand):
            self.grandren.remove(grand)

    class CompositeElement:

        def __init__(self, *args):
            self.name = args[0]
            self.children = []

        def appendChild(self, child):
            self.children.append(child)

        def removeChild(self, child):
            self.children.remove(child)

        def printDetails(self):
            print(self.name)
            for child in self.children:
                print("\t", end="")
                child.printDetails()



    print("\nСоздаем главную папку проекта, называем 'Армия'\n")
    project = CompositeElement("Армия")
    print("Создаем папки 'Отряд','Отряд эльфов'' и файл 'Циклоп'\n")
    sub1 = CompositeElement("Отряд")
    sub2 = CompositeElement("Отряд эльфов")
    projectsub = CompositeElement("Циклоп")
    print("Для папки 'Отряд' создаем вложенные файлы, папку 'Отряд кентавров', файл 'Минотавр' и файл 'Дракон'\n")
    sub11 = ChildElement("Отряд кентавров")
    sub12 = ChildElement("Минотавр")
    sub13 = ChildElement("Дракон")
    print("Для папки 'Отряд кентавров' создаем вложенные файлы, файл 'Кентавр 1' и файл 'Кентавр 2'\n")
    sub111 = GrandElement ("Кентавр 1")
    sub112 = GrandElement("Кентавр 2")
    print("Для папки 'Отряд эльфов' создаем вложенные файлы, файл 'Эльф Халдир', файл 'Эльфийка Арвен', файл 'Эльф Леголас' и файл 'Эльфийка Тауриэль'\n")
    sub21 = ChildElement("Эльф Халдир")
    sub22 = ChildElement("Эльфийка Арвен")
    sub23 = ChildElement("Эльф Леголас")
    sub24 = ChildElement("Эльфийка Тауриэль")
    print("Вкладываем наши файлы в папки\n")
    sub1.appendChild(sub11)
    sub1.appendChild(sub12)
    sub1.appendChild(sub13)
    sub2.appendChild(sub21)
    sub2.appendChild(sub22)
    sub2.appendChild(sub23)
    sub2.appendChild(sub24)
    print("Вкладываем наши полученные папки с отрядами и бойцами в главную папку Армии и файл Циклоп\n")
    project.appendChild(sub1)
    project.appendChild(sub2)
    project.appendChild(projectsub)
    print("Вкладываем файл Кентавр 1 и файл Кентавр 2 в папку Отряд кентавров")
    sub11.appendGrand(sub111)
    sub11.appendGrand(sub112)
    print("Структура организации армии: \n")
    project.printDetails()
    
    
    
main()