import random

game = "Лес"

name = ""

def intro():
    print(f"[{game}]\n\n")
    name = input("Введите имя игрока: ")
    print("За вами бежит маньяк, вы в тёмном лесу, вам необходимо сбежать.")

def first():
    input("Маньяка нет в поле зрения..")
    return

def second():
    print("Перед вами ловушка. Угадайте число для прохождения дальше (от 1 до 3)")
    answer = input("Ваше число: ")
    if answer != random.randint(1, 3):
         print("Вы проиграли")
         exit()
    else:
        print("Вы угадали число.")

def third():
    flag = 1
    while flag < random.randint(1, 15):
        if flag == 1:
            print("Вас поймал маньяк, хотите ли вы попробовать выбраться?")
        else:
            print("Вас всё ещё не отпускает маньяк, попробуете выбраться?")
        
        answer = input("да/нет: ")

        if answer == "нет":
            print("Вы проиграли")
            exit()

        flag += 1
    return

def game():
    situation = random.randint(0, 5)
    match situation:
        case 0:
            first()
        case 1:
            second()
        case 2:
            third()

def main():
    intro()

    for i in range(10):
        game()
    
    print("Вы выиграли")

main()