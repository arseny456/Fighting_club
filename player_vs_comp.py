import Fighter as F
import time
from random import choice

me = F.Fighter('Руслан')
bot = F.Fighter('Бот')

area_list = ["голову", "торс", "пояс", "ноги"]

# Пока хотя бы у одного бойца есть запас здоровья
while me.health > 0 and bot.health > 0:

    # Выбираем место, которое будем защищать
    print("Выберите место для блока (0, 1, 2, 3): ")
    area = input()

    if int(area) in (0,1,2,3):
        me.block(area_list[int(area)])

    # Выбираем случайное место для блока
    bot.block(choice(area_list))

    # выбираем место куда ударим противника
    print("Выберите место для удара (0, 1, 2, 3):\n ")
    area = input()
    if int(area) in (0,1,2,3):
        me.hit(bot, area_list[int(area)])

    # Бьём в случайное место противника
    bot.hit(me, choice(area_list))

    print(me.health, bot.health)
    time.sleep(0.5)
