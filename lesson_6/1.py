# генерируем i,j заново
# генерируем i,j
# while pole[i][j] != '-':
# генерируем i,j заново

# lists = [text[i] for i in range(len(text))]


# 41. Создайте программу для игры в "Крестики-нолики".
# import random 
# x = random.randint(0,10)
# ls = []
# ls1 =[]
# def printBoard(f):
#   for item in range(3):
#     if 
#   result = []
# result = [["."] * 3 for i in range(3)]
# for item in range(3):
#   y = 0
#   result = []
# result = [["."] * 3 for i in range(3)]
# print(result)
# (0, 3)
# # def main(board):
# #     counter = 0
# #     win = False
# #     while not win:
# #         draw_board(board)
# #         if counter % 2 == 0:
# #             take_input("X")
# #         else:
# #             take_input("O")
# #         counter += 1


# def print_matrix(result):
#     for i in range(0, len(result)):
#         for i2 in range(0, len(result[i])):
#             print(result[i][i2], end=" ")
#         print()
        
# print_matrix(result)



board = range(1,10)
def draw_board(board):
  print ("-------------")
  for i in range(3):
    print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
print("-------------")

def take_input(player_token):
  valid = False
  while not valid:
    player_answer = raw_input("Куда поставим " + player_token+"? ")
    try:
      player_answer = int(player_answer)
    except:
      print("Некорректный ввод. Вы уверены, что ввели число?")
      continue
    if player_answer >= 1 and player_answer <= 9:
      if (str(board[player_answer-1]) not in "XO"):
        board[player_answer-1] = player_token
        valid = True
      else:
        print("Эта клеточка уже занята")
    else:
      print("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")
    def check_win(board):
      win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
      for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False
  def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print tmp, "выиграл!"
                win = True
                break
        if counter == 9:
            print "Ничья!"
            break
    draw_board(board)