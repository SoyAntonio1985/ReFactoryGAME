import random

def choice_option():
  options = ('piedra','papel','tijera')
  user_opt = input('piedra, papel, tijera ==> ').lower().strip()
  
  if not user_opt in options:
    print('Elige una opción válida')
    return None, None
  
  comp_opt = random.choice(options)
  
  print(f'El usuario eligió ==> {user_opt}')
  print(f'La maquina eligió ==> {comp_opt}')
  return user_opt, comp_opt

def check_rules(user_opt,comp_opt,user_wins,comp_wins):
  if user_opt == comp_opt:
    print('Empate')
  
  elif user_opt == 'piedra':
    if comp_opt == 'tijera':
      print('piedra gana a tijera')
      print('user gano')
      user_wins += 1
    else:
      print('papel gana a piedra')
      print('comp gano')
      comp_wins += 1
  
  elif user_opt == 'papel':
    if comp_opt == 'piedra':
      print('papel gana a piedra')
      print('user gano')
      user_wins += 1
    else:
      print('tijera gana a papel')
      print('comp gano')
      comp_wins += 1
  
  else:
    if user_opt == 'tijera' and comp_opt == 'papel':
      print('tijera gana a papel')
      print('user gano')
      user_wins += 1
    else:
      print('piedra gana a tijera')
      print('comp gano')
      comp_wins += 1

  return user_wins, comp_wins

  print('*' * 10)
  print(f'Puntos USER {user_wins}')
  print(f'Puntos COMPU {comp_wins}')
  print('*' * 10)

def check_winner(user_wins,comp_wins):
  if comp_wins == 2:
    print('GANADOR COMPU')
    print('*' * 10)
    print(f'Puntos USER {user_wins}')
    print(f'Puntos COMPU {comp_wins}')
    print('*' * 10)
    exit()
  elif user_wins == 2:
    print('GANADOR USER')
    print('*' * 10)
    print(f'Puntos USER {user_wins}')
    print(f'Puntos COMPU {comp_wins}')
    print('*' * 10)
    exit()


def run_game():
  comp_wins = 0
  user_wins = 0
  rounds = 1

  while True:
  
    print('*' * 10)
    print(f'ROUND {rounds}')
    print('*' * 10)
    print(f'Puntos USER {user_wins}')
    print(f'Puntos COMPU {comp_wins}')
    print('*' * 10)
    rounds += 1
  
    user_opt, comp_opt = choice_option()
    user_wins, comp_wins = check_rules(user_opt,comp_opt,user_wins,comp_wins)
    check_winner(user_wins,comp_wins)

if __name__ == '__main__':
  run_game()