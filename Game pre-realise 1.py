attemps = 1
attemps2 = 1
attemps3 = 1
attemps4 = 1
attemps5 = 1
print("Игра начинается!")
result1 = input("2+2")
while result1 != "4":
    attemps += 1
    result1 = input("Попробуйте снова 2+2")
print("Ты решил с",attemps,"попытки")
print("Новый уровень!№2")
result2 = input("5+13")
while result2 != "18":
    attemps2 +=1
    result2 = input("Попробуй снова 5+13")
print("Ты решил с",attemps2,"попытки")
result3 = input("23+13")
while result3 != "36":
    attemps3 +=1
    result3 = input("Попробуй  снова 23+13")
print("Ты решил с",attemps3,"попытки")
result4 = input("65-23")
while result4 != "42":
    attemps4 +=1
    result4 = input("Попробуй  снова 23+13")
print("Ты решил с",attemps4,"попытки")
result5 = input("54-13+15")
while result5 != "56":
    attemps5 +=1
    result5 = input("Попробуй  снова 23+13")
print("Ты решил с",attemps5,"попытки")
print("Жди обновлений игры")
import time
time.sleep(3)
exit()
