# КНБ - вы играете с ботом, варианты раунда игры - победа
# 1 очко, проигрыш 0 очков, ничья 0.5 балла

# чтоб статистика сохранялась, и можно было играть неограниченное количество раундов

# from os import sep
# from random import random


# my_list = ['k', 'n', 'b']
# my_var = input(" введите ваш вариант: ")
# winner = 1
# fall= 0
# draw =0.5 

# def check(my_var):
#   bot_var = random.choice(my_list)
#   if bot_var == "k" and my_var == "b"
#   elif 
# my ==

 

# # КНБ - вы играете с ботом, варианты раунда игры - победа 1 очко, проигрыш 0 очков, ничья 0.5 балла
# import random

# a = input('введите К или Н или Б (либо q для выхода): ')

# result1 = 0
# result2 = 0

# # def knb(a):
# # 	global result1, result2
# #
# # 	if a == 'q':
# # 		print(result1, result2)
# # 	else:
# # 		while


# x = random.randint(0, 3)

# while True:
# 	x = random.randint(0, 3)
# 	if x != 'q':
# 		if x == 0:
# 			if a == 'К':
# 				result1 += 0
# 				result2 += 0
# 			if a == 'Н':
# 				result1 += 1
# 				result2 += 0
# 			if a == 'Б':
# 				result1 += 0
# 				result2 += 1
# 		if x == 1:
# 			if a == 'К':
# 				result1 += 0
# 				result2 += 1
# 			if a == 'Н':
# 				result1 += 0
# 				result2 += 0
# 			if a == 'Б':
# 				result1 += 1
# 				result2 += 0
# 		if x == 2:
# 			if a == 'К':
# 				result1 += 1
# 				result2 += 0
# 			if a == 'Н':
# 				result1 += 0
# 				result2 += 1
# 			if a == 'Б':
# 				result1 += 0
# 				result2 += 0
# 		else:
# 			break
# print(result1, result2)





import random

num = None
def knb(num):
    bot = 0
    user = 0
    while bot < 1000 or user < 1000:
        num = input('Введите камень или ножницы или бумага\n')
        num_bot = random.randrange(1, 4)
        if num_bot == 1:
            print('Бот выбрал КАМЕНЬ')
            if num == 'камень':
                print('Ничья, каждый заработал по 0.5 очков')
                bot = bot + 0.5
                user = user + 0.5
                print(f'У Вас {user} - очков. У бота {bot} - очков')
            elif num == 'ножницы':
                print('Бот выиграл и получает 1 очко')
                bot = bot + 1
                print(f'У Вас {user} - очков. У бота {bot} - очков')
            elif num == 'бумага':
                print('Вы выиграли и получаете 1 очко')
                user = user + 1
                print(f'У Вас {user} - очков. У бота {bot} - очков')

        elif num_bot == 2:
            print('Бот выбрал НОЖНИЦЫ')
            if num == 'ножницы':
                print('Ничья, каждый заработал по 0.5 очков')
                bot = bot + 0.5
                user = user + 0.5
                print(f'У Вас {user} - очков. У бота {bot} - очков')
            elif num == 'бумага':
                print('Бот выиграл и получает 1 очко')
                bot = bot + 1
                print(f'У Вас {user} - очков. У бота {bot} - очков')
            elif num == 'камень':
                print('Вы выиграли и получаете 1 очко')
                user = user + 1
                print(f'У Вас {user} - очков. У бота {bot} - очков')

        elif num_bot == 3:
            print('Бот выбрал БУМАГУ')
            if num == 'бумага':
                print('Ничья, каждый заработал по 0.5 очков')
                bot = bot + 0.5
                user = user + 0.5
                print(f'У Вас {user} - очков. У бота {bot} - очков')
            elif num == 'камень':
                print('Бот выиграл и получает 1 очко')
                bot = bot + 1
                print(f'У Вас {user} - очков. У бота {bot} - очков')
            elif num == 'ножницы':
                print('Вы выиграли и получаете 1 очко')
                user = user + 1
                print(f'У Вас {user} - очков. У бота {bot} - очков')

knb(num)