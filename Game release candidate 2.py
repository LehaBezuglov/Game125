import time
print("Все права принадлижат LehaBezuglov®")
attemps1 = 1
attemps2 = 1
attemps3 = 1
attemps4 = 1
attemps5 = 1
attempsdop = 1
print("Игра начинается!")
result1 = input("2+2")
while result1 != "4":
    attemps1 += 1
    result1 = input("Попробуйте снова 2+2")
print("Ты решил с",attemps1,"попытки")
if attemps1 == 1:
    print("твоя часть кода x")
else:
    print()
print("Новый уровень!№2")
result2 = input("5+13")
while result2 != "18":
    attemps2 +=1
    result2 = input("Попробуй снова 5+13")
print("Ты решил с",attemps2,"попытки")
if attemps2 == 1:
    print("твоя часть кода 5")
else:
    print()

print("Новый уровень!№3")
result3 = input("23+13")
while result3 != "36":
    attemps3 +=1
    result3 = input("Попробуй  снова 23+13")
print("Ты решил с",attemps3,"попытки твоя часть кода r")
if attemps3 == 1:
    print("твоя часть кода r")
else:
    print()

print("Новый уровень!№4")
result4 = input("65-23")
while result4 != "42":
    attemps4 +=1
    result4 = input("Попробуй  снова 65-23")
print("Ты решил с",attemps4,"попытки")
if attemps4 == 1:
    print("твоя часть кода 2")
else:
    print()

print("Новый уровень!№5")
result5 = input("54-13+15")
while result5 != "56":
    attemps5 +=1
    result5 = input("Попробуй  снова 54-13+15")
print("Ты решил с",attemps5,"попытки")
if attemps5 == 1:
    print("твоя часть кода f")
else:
    print()

code = input("Собери и введи код")
if code == "x5r2f":
    print("Дополнительный уровень!")   
    resultdop = input("125.7+42.5")
    if resultdop == "69.2" or "69,2":
        print("Молодец")
        print("Жди обновлений игры")
        print("Страница игры https://github.com/programmer-L/Game125 !скопируй ссылку!")
        time.sleep(7)
        exit()
    else:
        print("Не вено :(")
        print("Жди обновлений игры")
        print("Страница игры https://github.com/programmer-L/Game125 !скопируй ссылку!")
        time.sleep(7)
        exit()
else:
    print("Сегодня без дополнительных уровней :(")
    print("Жди обновлений игры")
    print("Страница игры https://github.com/programmer-L/Game125 !скопируй ссылку!")
    time.sleep(7)
    exit()
