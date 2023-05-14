import random
import time
from tkinter import Text, END
# from GUI_for_player_vs_comp import text_field

class Fighter:
    def __init__(self, name: str, health=100, text_log: Text = None):
        self.name = name
        self.health = health
        self.armor = 10
        self.strange = 1
        self.block_area = "торс"
        self.text_log = text_log

    def hit(self, enemy, area='торс'):

        area = "торс" if area == "" else area

        hit = self.strange * random.randint(1, 10)  # текущий урон
        if enemy.block_area != area:
            enemy.health -= hit
            self.text_log.config(state='normal')
            self.text_log.insert(0.0, f"{self.name} нанёс удар {enemy.name} в {area} с силой {hit}\n\n")
            self.text_field.config(state='disabled')
        else:
            self.text_log.config(state='normal')
            self.text_log.insert(0.0, f"{enemy.name} отразил удар по {area}\n\n")
            self.text_log.config(state='disabled')
        # Если здоровье противника стало меньше 0, ставим в 0
        if enemy.health < 0:
            enemy.health = 0
        if enemy.health <= 0:
            self.text_log.config(state='normal')
            self.text_log.insert(0.0, f"{enemy.name}, Побеждён\n\n")
            self.text_log.config(state='disabled')
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
