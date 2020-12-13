#аминь ножница работа...то есть бумаги
#1 это ножница,2 это аминь,3 это бумаги.
'''1 проигрывает 2, выигрывает 3
2 проигрывает 3, выигрывает 1
3 проигрывает 1, выигрывает 2'''
from pyfiglet import Figlet
f = Figlet(font='slant')

import random
import time

#comp = random.randint(1,3)
#comp - второй игрок
comp = int(input('ИГРОК1: введите число: 1 - ножница , 2 - аминь, 3 - бумаги. \n'))
x = int(input('ИГРОК2:  введите число: 1 - ножница , 2 - аминь, 3 - бумаги. \n'))

#если пользователь ввел число больше 3 или меньше 1
while x > 3 or x < 1:
  print("НЕ ПРАВИЛЬНЫЙ ОТВЕТ!!!")
  x = int(input('Введите заново: 1,2 или 3! \n'))

#
#if x >= 4 or x <= 0: 
#  print("НЕ ПРАВИЛЬНЫЙ ОТВЕТ!!!")
#  x = int(input('Введите заново: 1,2 или 3! \n'))

#print('Компьютер выбирает...')
time.sleep(1)  #ждать 1 секунду
print('...')
time.sleep(1)  #ждать 1 секунду
if comp == 1:
  print('Ножницы')
elif comp == 2:
  print('Камень')
else:
  print('Бумагa')
    
print('Да начнется бой!')
time.sleep(1)  #ждать 1 секунду

#случаи, когда выигрывает КОМПЬЮТЕР
if x == 1 and comp == 2:
  print (f.renderText('The user 1 and won! \n'))
elif x == 2 and comp == 3:
  print (f.renderText('The user 1 and won! \n'))
elif x == 3 and comp == 1:
  print (f.renderText('The user 1 and won! \n'))

#случаи, когда выигрывает ИГРОК
elif x == 2 and comp == 1:  
   print('Пользователь выбрал 2', x, 'и выиграл! \n')
   print (f.renderText('The user 2 won! \n'))
elif x == 3 and comp == 2:
   print('Пользователь выбрал', x, 'и выиграл! \n')
   print (f.renderText('The user 2 won! \n'))
elif x == 1 and comp == 3:
   print('Пользователь выбрал', x, 'и выиграл! \n')
   print (f.renderText('The user 2 and won! \n'))
else:
    print (f.renderText('Draw'))
    