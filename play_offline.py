import Fighter as F
import time

boy1 = F.Fighter('Ars')
boy2 = F.Fighter('Mat')
mrSuper = F.Fighter('Ruslan')
mrSuper.health = 10000
mrSuper.strange = 10

print(boy2.__doc__)

# Пока хотя бы у одного бойца есть запас здоровья
while boy1.health > 0 and \
    boy2.health > 0 and \
    mrSuper.health > 0:

    boy1.hit(boy2)
    boy1.hit(mrSuper)
    boy2.hit(boy1)
    boy2.hit(mrSuper)
    mrSuper.hit(boy1)
    mrSuper.hit(boy2)

    print(boy1.health, boy2.health, mrSuper.health)
    time.sleep(0.5)
