''' 
14:49PM 15/11/2021
#1: Парадигма ООП, классы, экземпляры классов, атрибуты.
'''


class Point3D:
    x = 15
    y = 10
    z = 50



class Point:
    "Класс для представления координт точек на плоскости"
    x = 1
    y = 12


# print(Point.__doc__)
# print(Point.__name__)
# print(dir(Point))

pt = Point()
pt.x = 100
pt.y = 10
# print(pt.__dict__)
# print(Point.__dict__)
# print(pt.x, pt.y, id(pt), id(Point), sep="\n")

print(getattr(pt, "y")) # получает атрибут
print(getattr(pt, "z", False)) # возвращает False если атрибута нет
print(hasattr(pt, "y")) # проверяет наличие атрибута
setattr(pt, "z", 7) # создаёт атрибут
print(getattr(pt, "z"))
delattr(pt, "z")
print(getattr(pt, "z", False))

Point.g = 100
pt.msg = "hello"
res = getattr(pt, "sss", False)
del pt.x
print("___________________________\n")
print(isinstance(pt, Point3D)) # проверяет является ли 
# экзепляр pt экземпляром класса Point
print(getattr(pt, "x"))

print("\n---------------------------\n")
pt3D = Point3D()
pt3D1 = Point3D()
pt3D2 = Point3D()
print(pt3D1.x, pt3D1.y, pt3D1.z, sep="\n")
print("-------------")
print(pt3D2.x, pt3D2.y, pt3D2.z, sep="\n")
print("-------------")
print(pt3D.x, pt3D.y, pt3D.z, sep="\n")
setattr(pt3D, "x", 1234)
print("-------------")
print(pt3D.x, pt3D.y, pt3D.z, sep="\n")
print("\n\n----------\n")
print("sdfghjklkuytrfd")
print(pt3D.x, sep="\n")
delattr(pt3D, "x")
print(pt3D1.x, pt3D1.y, pt3D1.z, sep="\n")
print("-------------")
print(pt3D2.x, pt3D2.y, pt3D2.z, sep="\n")
print("-------------")
print(pt3D.x, pt3D.y, pt3D.z, sep="\n")