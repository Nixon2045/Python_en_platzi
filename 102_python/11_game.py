import random



def choose_option():
    options = ('piedra', 'tijeras', 'papel')
    user_option = input ('piedra, papel o tijeras => ')
    computer_option = random.choice(options)

    user_option = user_option.lower() 

    print('user_option =>', user_option)
    print('computer_option =>', computer_option)
    if  not user_option in options:
        print('Inserta una respuesta valida')
        return None, None
    #continue
    return user_option, computer_option

def check_rules(user_option, computer_option, users_wins, computer_wins):
        if user_option == computer_option:
            print('empate!')
        elif user_option == 'piedra':
            if computer_option == 'tijeras':
                print('piedra gana a tijeras')
                print('user gana!')
                users_wins += 1
            else:
                print('papel gana a piedra')
                print('computer gano!')
                computer_wins += 1
        elif user_option == 'papel':
            if computer_option == 'piedra':
                print('papel gana a piedra')
                print('gana user!')
                users_wins += 1
            else:
                print('tijeras gana a papel')
                print('computer gana')
                computer_wins += 1
        elif user_option == 'tijeras':
            if computer_option == 'papel':
                print('tijeras gana a papel')
                print('user gana!')
                users_wins += 1
            else:
                print('piedra gana sobre tijeras')
                print('computer gana!')
                computer_wins += 1
                
        return users_wins, computer_wins
def run_game():
    computer_wins = 0
    users_wins = 0
    rounds = 1 
    while True:

        print('*' * 10)
        print('ROUND ', rounds )
        print('*' * 10)

        print('computer_wins=> ', computer_wins)
        print('users_wins=> ', users_wins)

        rounds += 1

        user_option, computer_option = choose_option()
        users_wins, computer_wins = check_rules(user_option, computer_option,users_wins,computer_wins)    


        if computer_wins == 2:
            print('ganador supremo el computador!!!')
            break
        if users_wins == 2:
            print('ganador supremo el userrrrr!!!')
            break
run_game()

   

    