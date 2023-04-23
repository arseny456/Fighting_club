import Fighter as F
import time
from random import choice

girl1 = F.Fighter('Розалия')
girl2 = F.Fighter('Диана')

area_list = ["голову", "торс", "пояс", "ноги"]

# Пока хотя бы у одного бойца есть запас здоровья
while girl1.health > 0 and girl2.health > 0:

    # Выбираем случайное место для удара
    girl1.block(choice(area_list))
    girl2.block(choice(area_list))

    # Бьём в случайное место противника
    girl1.hit(girl2, choice(area_list))
    girl2.hit(girl1, choice(area_list))

    print(girl1.health, girl2.health)
    time.sleep(0.5)
