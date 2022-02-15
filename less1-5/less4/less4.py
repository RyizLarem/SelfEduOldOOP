''' 
16:48PM 15/11/2021
#4: Объекты свойста (property) и дескрипторы классов.
'''


class NoDataDescr:
    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return "NoDataDescr __get__"



class CoordValue:
    # def __init__(self, name):
    #     self.__name = name

    def __set_name__(self, owner, name):
        print(name)
        self.__name = name


    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value

    # def __delete__(self, obj):
    #     del self.__value


# Объекты-свойства (property)
class Point:
    noData = NoDataDescr()

    coordX = CoordValue()
    coordY = CoordValue()


    def __init__(self, x = 0, y = 0):
        self.coordX = x
        self.coordY = y


    # def __checkValue(x):
    #     if isinstance(x, int) or isinstance(x, float):
    #         return True
    #     return False

    # @property
    # def coordX(self):
    #     print("вызов __getCoordx")
    #     return self.__x

    # @coordX.setter
    # def coordX(self, x):
    #     if Point.__checkValue(x):
    #         self.__x = x
    #         print("вызов __setCoordX")
    #     else:
    #         raise ValueError("Неверный формат данных")
        
    # @coordX.deleter
    # def coordX(self):
    #     print("Удаление свойства")
    #     del self.__x


    # coordX = property(__getCoordX, __setCoordX, __delCoordX)


pt = Point(1, 2)
pt2 = Point(10, 20)
print(pt.coordX, pt.coordY)
pt.coordX = 100
print(pt2.coordX, pt2.coordY)

pt.noData = "hello"