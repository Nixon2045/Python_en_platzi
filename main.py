user_option = input ('piedra, papel o tijera =>')
computer_option = 'papel'

user_option = user_option.lower()

if user_option == computer_option:
    print('empate!')
elif user_option == 'piedra':
    if computer_option == 'tijeras':
        print('piedra gana a tijeras')
        print('user gana!')
    else:
        print('papel gana a piedra')
        print('computer gano!')
elif user_option == 'papel':
    if computer_option == 'piedra':
        print('papel gana a piedra')
        print('gana user!')
    else:
        print('tijeras gana a papel')
        print('computer gana')
elif user_option == 'tijeras':
    if computer_option == 'papel':
        print('tijeras gana a papel')
        print('user gana!')
    else:
        print('piedra gana sobre tijeras')
        print('computer gana!')
else:
    print('sigue intentando algo valido')