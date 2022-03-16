from random import randint
from time import sleep
n1 = 2
n2 = 2
n3 = 4
n4 = int(input("2+2="))
ForScore = 0
while n3 == n4:
	if n3 == n4:
		while n3 == n4:
			print("Дальше!")
			n1 = randint(12,999)
			n2 = randint(12,999)
			n3 = n1 + n2
			print(n1, "+", n2, "=")
			n4 = int(input())
			ForScore += 1
	else:
		print("Ты чё дурак?")
		sleep(2)
print("Не верно, конец игры! Твой счёт -", ForScore)
sleep(2)