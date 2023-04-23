import random
import time


# TODO: добавить удары и блоки разных частей тела
class Fighter:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.armor = 10
        self.strange = 1
        self.block_area = "торс"

    def hit(self, enemy, area='торс'):

        area = "торс" if area == "" else area

        hit = self.strange * random.randint(1, 10)  # текущий урон
        if enemy.block_area != area:
            enemy.health -= hit
            print(self.name, 'нанёс удар', enemy.name, 'в', area, 'с силой', hit)
        else:
            print(enemy.name, 'отразил удар по', area)
        # Если здоровье противника стало меньше 0, ставим в 0
        if enemy.health < 0:
            enemy.health = 0
        if enemy.health <= 0:
            print(enemy.name, 'Побеждён')

    def block(self, area):
        self.block_area = area


# Если мы запускаем этот файл как главный, то будет выполнен пример ниже
if __name__ == '__main__':
    boy1 = Fighter('Arsenii')
    boy2 = Fighter('Evangelie_ot_Matveya')

    print('Малчык адын', boy1.health)
    print('Малчык две', boy2.health)

    while boy2.health > 0:
        boy1.hit(boy2)
        print('Малчык адын', boy1.health)
        print('Малчык две', boy2.health)
        time.sleep(1)
