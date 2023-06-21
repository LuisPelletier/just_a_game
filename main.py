import random

options = ('piedra', 'papel', 'tijera')

computer_wins = 0
user_wins = 0

rounds = 1

while True:

  print(' ')
  print('*' * 10)
  print(' ')
  print('RONDA', rounds)
  print(' ')
  print('*' * 10)
  print(' ')

  print('Marcador:')
  print('Usuario ->', user_wins)
  print('Computadora ->', computer_wins)
  print(' ')

  user_option = input('Elige una opción! piedra, papel o tijera => ')
  user_option = user_option.lower()
  
  if not user_option in options:
    print(' ')
    print('Esa opción no es válida, intenta nuevamente')
    continue
  
  computer_option = random.choice(options)

  print(' ')
  print('Elegiste => ', user_option)
  print(' ')
  print('La computadora escogió => ', computer_option)
  print(' ')
  
  if user_option == computer_option:
    print('Es un empate!')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('piedra gana a tijera')
      print('usuario ganó!')
      user_wins += 1
    else:
        print('papel gana a piedra')
        print('computadora gana')
        computer_wins += 1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('papel gana a piedra')
      print('usuario ganó!')
      user_wins += 1
    else:
        print('tijera gana a papel')
        print('computadora gana')
        computer_wins += 1
  elif user_option == 'tijera':
    if computer_option == 'piedra':
      print('piedra gana a tijera')
      print('computadora ganó!')
      computer_wins += 1
    else:
        print('tijera gana a papel')
        print('usuario gana')
        user_wins += 1

  if computer_wins == 2:
    print(' ')
    print(' ')
    print('= = Te ganó la computadora! FIN DEL JUEGO = =')
    print(' ')
    print(' ')
    break
    
  if user_wins == 2:
    print(' ')
    print(' ')
    print('= = Ganaste! FIN DEL JUEGO = =')
    print(' ')
    print(' ')
    break
    
  rounds += 1

