from random import randint
from time import sleep
print("Все права принадлижат LehaBezuglov®")
print("Игра в стадии разработки и может содержать ошибки")
print("После значения None надо ввести ответ. Ошибка в процессе исправления")
random_number1_1 = randint(1, 100)
random_number1_2 = randint(1, 100)
random_number1_3 = randint(1, 9)
random_number2_1 = randint(1, 125)
random_number2_2 = randint(1, 125)
random_number2_3 = randint(1, 9)
random_number3_1 = randint(1, 150)
random_number3_2 = randint(1, 150)
random_number3_3 = randint(1, 9)
random_number4_1 = randint(1, 200)
random_number4_2 = randint(1, 200)
random_number4_3 = randint(1, 9)
random_number5_1 = randint(1, 250)
random_number5_2 = randint(1, 250)
random_number5_3 = randint(1, 9)
random_numberdop_1 = randint(1, 500)
random_numberdop_2 = randint(1, 500)
attemps1 = 1
attemps2 = 1
attemps3 = 1
attemps4 = 1
attemps5 = 1
attempsdop = 1
print("Игра начинается!")
result1 = int(input(print(random_number1_1,"+",random_number1_2,"=")))
while result1 != random_number1_1 + random_number1_2 :
    attemps1 += 1
    result1 = input("Попробуйте снова")
print("Ты решил с",attemps1,"попытки")
print("Ну-ну")
if attemps1 == 1:
    print("твоя часть кода", random_number1_3)
else:
    print()

print("Новый уровень!№2")
result2 = int(input(print(random_number2_1,"+",random_number2_2,"=")))
while result2 != random_number2_1 + random_number2_2 :
    attemps2 += 1
    result2 = input("Попробуйте снова")
print("Ты решил с",attemps2,"попытки")
print("Ну давай")
if attemps2 == 1:
    print("твоя часть кода", random_number2_3)
else:
    print()

print("Новый уровень!№3")
result3 = int(input(print(random_number3_1,"+",random_number3_2,"=")))
while result3 != random_number3_1 + random_number3_2 :
    attemps3 += 1
    result3 = input("Попробуйте снова")
print("Ты решил с",attemps3,"попытки")
print("Молодец")
if attemps3 == 1:
    print("твоя часть кода", random_number3_3)
else:
    print()

print("Новый уровень!№4")
result4 = int(input(print(random_number4_1,"+",random_number4_2,"=")))
while result4 != random_number4_1 + random_number4_2 :
    attemps4 += 1
    result4 = input("Попробуйте снова")
print("Ты решил с",attemps4,"попытки")
print("Ладно")
if attemps4 == 1:
    print("твоя часть кода", random_number4_3)
else:
    print()

print("Новый уровень!№5")
result5 = int(input(print(random_number5_1,"+",random_number5_2,"=")))
while result5 != random_number5_1 + random_number5_2 :
    attemps5 += 1
    result5 = input("Попробуйте снова")
print("Ты решил с",attemps5,"попытки")
print("Крутой")
if attemps5 == 1:
    print("твоя часть кода", random_number5_3)
else:
    print()

codeparts = random_number1_3 + random_number2_3 + random_number3_3 + random_number4_3 + random_number5_3
code = int(input("Сложи(+) части кода"))
if code == codeparts:
    print("Дополнительный уровень!")   
    resultdop = int(input(print(random_numberdop_1,"+",random_numberdop_2,"=")))
    if resultdop == random_numberdop_1 + random_numberdop_2 :
        print("Молодец!")
        print("Жди обновлений игры")
        print("Страница игры https://github.com/programmer-L/Game125 !скопируй ссылку!")
        sleep(7)
        exit()
    else:
        print("Не вено :(")
        print("Жди обновлений игры")
        print("Страница игры https://github.com/programmer-L/Game125 !скопируй ссылку!")
        sleep(7)
        exit()
else:
    print("Сегодня без дополнительных уровней :(")
    print("Жди обновлений игры")
    print("Страница игры https://github.com/programmer-L/Game125 !скопируй ссылку!")
    sleep(7)
    exit()