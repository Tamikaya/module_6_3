# module_6_3

## Множественное наследование

### Задача "Ошибка эволюции"

Вы, наверное, замечали, что некоторые животные в нашем мире обладают необычными и порой противоречивыми чертами? Например, утконос... У него есть клюв, но он не птица. С одной стороны, он милый, с другой — на задних лапах у него шипы. Кроме того, он откладывает яйца... Оставим в стороне тот факт, что утконосы потеют молоком, и попробуем создать нашего удивительного героя не эволюционным путём.

### Классы для реализации задачи

Для решения задачи необходимо разработать пять классов:

1. **Animal** — базовый класс, описывающий всех животных.
   Класс обладает следующими атрибутами:
   – **live** — значение по умолчанию: True
   – **sound** — изначально отсутствует
   – **_DEGREE_OF_DANGER** — степень опасности существа, заданная как 0

Объект этого класса также имеет следующие атрибуты:
   – **_cords** — координаты в пространстве, инициализированные как [0, 0, 0]
   – **speed** — скорость передвижения, определяемая при создании объекта

Методы, которые должен реализовать этот класс:
   – **move(self, dx, dy, dz)** — метод, изменяющий соответствующие координаты в _cords на dx, dy и dz с учетом скорости. Если при попытке изменить координату z в _cords значение окажется меньше 0, выводится сообщение "It's too deep, i can't dive:(" без внесения изменений.
   – **get_cords(self)** — метод, возвращающий координаты в формате "X: <координаты по x>, Y: <координаты по y>, Z: <координаты по z>"
   – **attack(self)** — метод, выводящий "Sorry, i'm peaceful:)", если степень опасности меньше 5, и "Be careful, i'm attacking you 0_0", если равна или больше.
   – **speak(self)** — выводит строку со звуком sound

2. **Bird** — класс, описывающий птиц. Наследуется от **Animal**.
   Класс должен обладать атрибутом **beak** — наличие клюва, и методом **lay_eggs(self)**, который выводит строку "Here are(is) <случайное число от 1 до 4> eggs for you".

3. **AquaticAnimal** — класс, представляющий плавающих животных. Наследуется от **Animal**. В этом классе **_DEGREE_OF_DANGER** установлен как 3.
   Класс должен включать метод **dive_in(self, dz)**, который уменьшает координату z в _cords. Чтобы сделать dz положительным, используйте функцию **abs** для его модуля. Скорость движения при нырянии должна быть уменьшена в два раза по сравнению с обычной скоростью (**speed / 2**).

4. **PoisonousAnimal** — класс, описывающий ядовитых животных. Наследуется от **Animal**. **_DEGREE_OF_DANGER** в этом классе установлен как 8.

5. **Duckbill** — класс, представляющий утконоса. Наследуется от **Bird**, **AquaticAnimal** и **PoisonousAnimal**. Порядок наследования определите самостоятельно, основываясь на примерах выполнения кода, приведенных ниже.
   Объект этого класса должен иметь дополнительный атрибут **sound** — звук, издаваемый утконосом, установленный как "Click-click-click".

### Пример выполнения программы

Пример работы программы:

```python
db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
```

Обратите внимание, что при определении порядка наследования важно учитывать, что утконос атакует с сообщением "Be careful, i'm attacking you 0_0".
