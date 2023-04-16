import random
import time


# TODO: добавить удары и блоки разных частей тела
class Fighter:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.armor = 10
        self.strange = 1

    def hit(self, enemy):
        '''

        :param enemy:
        :return:
        '''
        hit = self.strange * random.randint(1, 10)  # текущий урон
        enemy.health -= hit
        print(self.name, 'нанёс удар', enemy.name, 'с силой', hit)
        if enemy.health < 0:
            enemy.health = 0
        if enemy.health <= 0:
            print(enemy.name, 'Побеждйон')


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
