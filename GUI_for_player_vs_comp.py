from tkinter import *
from Fighter import Fighter
from random import choice

root = Tk()
root.title("Fight_club")
root.geometry("250x150")
root.resizable(False,False)

attack_var  = IntVar()
attack_var.set(0)

defence_var = IntVar()
defence_var.set(0)

attack_frame = Frame()
defence_frame= Frame()

attack_frame.pack(side='left')
defence_frame.pack(side='right')

# attack_label = Label(text = 'attack')

rb_attack_head = Radiobutton(attack_frame,text = "Head",variable=attack_var,value=0)
rb_attack_tors = Radiobutton(attack_frame,text = "Tors",variable=attack_var,value=1)
rb_attack_belt = Radiobutton(attack_frame, text= 'belt',variable=attack_var,value=2)
rb_attack_legs = Radiobutton(attack_frame,text = "legs",variable=attack_var,value=3)
rb_def_head = Radiobutton(defence_frame,text = 'head',variable=defence_var,value=0)
rb_def_tors = Radiobutton(defence_frame,text = 'tors',variable=defence_var,value=1)
rb_def_belt = Radiobutton(defence_frame,text = 'belt',variable=defence_var,value=2)
rb_def_legs = Radiobutton(defence_frame,text = 'legs',variable=defence_var,value=3)

rb_attack_head.pack(anchor = 'w')
rb_attack_tors.pack(anchor = 'w')
rb_attack_belt.pack(anchor = 'w')
rb_attack_legs.pack(anchor = 'w')
rb_def_head.pack(anchor = 'w')
rb_def_tors.pack(anchor = 'w')
rb_def_belt.pack(anchor = 'w')
rb_def_legs.pack(anchor = 'w')

me = Fighter('player1')
comp = Fighter("player2")

area_list = ['голову','торс','пояс','ноги']

def attack():
    # Получаем место для удара
    # Получаем место для защиты
    me.block(area_list[defence_var.get()])
    comp.block(choice(area_list))
    me.hit(comp,area_list[attack_var.get()])
    comp.hit(me,choice(area_list))

    print(me.health,comp.health)

btn = Button(root,text='Move',command = attack)
btn.pack(side = 'bottom')
root.mainloop()