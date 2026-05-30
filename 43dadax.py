import random
import turtle
list_greeting = ['Приветствую', 'Добрый день!', 'Здравствуйте']
run = True
command = ''
command_list=["exit","start","eho","help","sum","min","umn","del","calc","flower","random(0,10)","vopros"]
a1=""
true_list=["Я","Гын"]
while run:
    command = input('Введите команду')
    if command == 'exit':
        run = False
    elif command == 'start':
        print(list_greeting[random.randint(0, len(list_greeting)-1)])
    elif command=='eho':
        while a1!="stop":
            a1=input()
            print(a1)
    elif command=="help":
        print(command_list)
    elif command=="sum":
        a2=int(input())
        a3=int(input())
        print(a2+a3)
    elif command=="min":
        a2=int(input())
        a3=int(input())
        print(a2-a3)
    elif command=="umn":
        a2=int(input())
        a3=int(input())
        print(a2*a3)
    elif command=="del":
        a2=int(input())
        a3=int(input())
        print(a2/a3)
    elif command=="calc":
        a2=int(input())
        a4=input()
        a3=int(input())
        print(a2,a4,a3)
    elif command=="random(0,10)":
        print(random.randint(0,11))
    elif command=="vopros":
        d3=input()
        print(true_list[random.randint(0, len(true_list)-1)])
    elif command=="flower":
        r5=input("Цвет 1 (на англиском и маленькими буквами)")
        r4=input("Цвет 2 (на англиском и маленькими буквами)")
        r6=int(input("forward"))
        r7=int(input("left"))
        r8=int(input("speed"))
        r9=int(input("range"))
        tur = turtle.Turtle()
        tur.speed(r8)
        tur.color(r4, r5)
        tur.begin_fill()
        for i in range(r9):
            tur.forward(r6)
            tur.left(r7)
        tur.end_fill()
        turtle.done()
    
    