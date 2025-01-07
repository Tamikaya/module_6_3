import random

class Animal: # класс описывающий животны

    # Атрибуты класса
    live = True
    sound = None # звук (изначально отсутствует)
    _DEGREE_OF_DANGER = 0 # степень опасности существа

    # Объект этого класса обладает следующими атрибутами:
    _cords = [0, 0, 0] # координаты в пространстве.

    def __init__(self, speed):
        self.speed = speed #  скорость передвижения существа (определяется при создании объекта), множитель

    # И методами:
    def move(self, dx, dy, dz):
         self._cords = [int(dx) * int(self.speed), int(dy) * int(self.speed), int(dz) * int(self.speed)] # множетелем будет являтся speed
         if self._cords[2] < 0: # Если при попытке изменения координаты z [2] в _cords значение будет меньше 0
             print(f"It's too deep, i can't dive :(") # "Здесь слишком глубоко, я не могу нырнуть"
             self._cords[2] = 0 # при этом изменения не вносяться

    def get_cords(self):
         print(f"X:X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")# "X: <координаты по x>, Y: <координаты по y>, Z: <координаты по z>"

    def attack(self):
         if self._DEGREE_OF_DANGER <= 5:
           print("Be careful, i'm attacking you 0_0") # "Извините, я настроен миролюбиво :)
         else:
           print("Sorry, i'm peaceful :)") # Будь осторожен, я нападаю на тебя 0_0

    def speak (self):
         print(self.sound) # выводит строку со звуком sound


class Bird(Animal): #класс описывающий птиц

    # Должен обладать атрибутом:
    beak = True  # наличие клюва

    # И методом:
    def lay_eggs(self):
        egg = random.randint(1, 4)
        print(f"Here is(are) {egg} egg(s) for you")


class AquaticAnimal(Animal): # класс описывающий плавающего животного. Наследуется от Animal.
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._cords[2] = abs(int(self._cords[2]) // int(self.speed)) - dz // 2


class PoisonousAnimal(Animal): # класс описывающий ядовитых животных. Наследуется от Animal.
    _DEGREE_OF_DANGER = 8.


class Duckbill (Bird, AquaticAnimal, PoisonousAnimal): # класс описывающий утконоса
    sound = "Click-click-click" # звук, который издаёт утконос


db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()