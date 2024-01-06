
def last_portal():
    boat_side='Right'
    missionaries_on_right=3
    cannibals_on_right=3
    missionaries_on_left=0
    cannibals_on_left=0
    b=0
    run = True
    while run:
        missionaries = int(input("M:"))
        cannibals = int(input("C"))
        print(f'M = {missionaries_on_left} C = {cannibals_on_left} |-----B| M = {missionaries_on_right} C = {cannibals_on_right}')
        b = missionaries+cannibals
        if 1 <= b <=2:
            print("valid")
        else:
            print('invalid move')
            continue
        if missionaries_on_right < missionaries or cannibals_on_right < cannibals :
            print('Invalid move')

        if boat_side=='Right':
            missionaries_on_right = missionaries_on_right - missionaries
            cannibals_on_right = cannibals_on_right - cannibals
            missionaries_on_left = missionaries_on_left + missionaries
            cannibals_on_left = cannibals_on_left + cannibals
            boat_side='Left'
            print(f'M = {missionaries_on_left} C = {cannibals_on_left} |B------| M = {missionaries_on_right} C = {cannibals_on_right}')
        else:
            missionaries_on_left = missionaries_on_left - missionaries
            cannibals_on_left = cannibals_on_left - cannibals
            missionaries_on_right = missionaries_on_right + missionaries
            cannibals_on_right = cannibals_on_right + cannibals
            boat_side = 'Right'
            print(f'M = {missionaries_on_left} C = {cannibals_on_left} |------B| M = {missionaries_on_right} C = {cannibals_on_right}')

        if 0 < missionaries_on_right < cannibals_on_right or 0 < missionaries_on_left < cannibals_on_left:
            print("You Lose")
            print("Game over")
            run = False
        if missionaries_on_left == 3 and cannibals_on_left ==3:
            print('You win')
            print("Game over")
            run = False


