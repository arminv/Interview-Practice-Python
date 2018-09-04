import random

def my_game(a_choice):
  '''
  Takes a choice of 'R' (Rock), 'P' (Paper) or 'S' (Scissors) as 
  argument and returns the result of playing a round against the
  computer (random choice).
  '''

  choices = ['R', 'P', 'S']
  win = '--> You WIN! :)'
  loss = '--> You LOSE! :('
  draw = '--> It\'s a DRAW!'

  # Error handling/validation:
  try:
    choice = a_choice[0].upper()
  except IndexError:
    print('----> No choice (argument) was given! Please try again! <----')
    return

  if choice not in choices:
    print('----> Your choice is not a valid option! <----')
    return

  # Computer chooses (pseudo)randomly:
  computer = random.choice(choices)

  print('  Your choice is: {}'.format(choice))
  print('  Computer\'s choice is: {}'.format(computer))

  # Concluding the result of the game: 
  if choice == computer:
    print(draw)
    return

  else:
    if choice == 'R':
      if computer == 'S':
        print(win)
      else:
        print(loss)

    if choice == 'P':
      if computer == 'R':
        print(win)
      else:
        print(loss)

    if choice == 'S':
      if computer == 'P':
        print(win)
      else:
        print(loss)

# ----------------------------------------------
if __name__ == '__main__':
  # Only use 'raw_input()' if using Python 2.X :
  try: input = raw_input
  except NameError: pass
  your_Choice = input('''
  What Is Your Choice : (R)ock / (P)aper / (S)cissors ?
  ''')
  my_game(your_Choice)