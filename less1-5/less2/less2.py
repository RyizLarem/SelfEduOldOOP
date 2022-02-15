'''
15:23PM 15/11/2021
#2: методы класса, параметр self, конструктор и деструктор.
'''


class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __del__(self):
        print("Удаление экземпляра: " + self.__str__())



    x = 1; y = 1
    def setCoords(self, x, y):
       self.a = x 
       self.b = y 


pt = Point()
pt = 0






