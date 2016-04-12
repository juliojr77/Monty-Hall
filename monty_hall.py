import random

doors = ['goat', 'car' ,'goat']


def get_stay():
    return random.randint(1, 3)


def get_switch():
    return random.randint(1, 2)


#------------------------------------------------------
wins = 0
losses = 0

for _ in range(10000):
    wininning = random.randint(1, 3)
    only_choice = random.randint(1, 3)

    if only_choice == wininning:
        wins += 1

    else:
        losses += 1

    #input()
print('\n\n')
print(wins)
print(losses)
print('\n\n')


#-----------------------------------------------------------------------

wins_2 = 0
losses_2 = 0

for _ in range(10000):
    wininning_2 = random.randint(1,3)

    choice_1 = random.randint(1,3)

    if choice_1 == wininning_2:
#---------
        if wininning_2 == 1:
            choice_2 = random.randint(1,2)

            if choice_2 == wininning_2:
                 wins_2 += 1
            else:
                 losses_2 += 1

        elif wininning_2 == 2:
            choice_2 = random.randint(2,3)

            if choice_2 == wininning_2:
                 wins_2 += 1
                #  choice_2 = random.randint(1,2)
                #  if choice_2 == wininning_2:
                #       wins_2 += 1
                #  else:
                #       losses_2 += 1
            else:
                 losses_2 += 1

        elif wininning_2 == 3:
            choice_2 = random.randint(2,3)

            if choice_2 == wininning_2:
                wins_2 += 1
            else:

                losses_2 += 1
#------------------------------------------------------------------------------
    else:

        if wininning_2 == 1:
            choice_2 = random.randint(1,2)

            if choice_2 == wininning_2:
                 wins_2 += 1
            else:
                 losses_2 += 1

        elif wininning_2 == 2:
            choice_2 = random.randint(2,3)

            if choice_2 == wininning_2:
                 wins_2 += 1
                #  choice_2 = random.randint(1,2)
                #  if choice_2 == wininning_2:
                #       wins_2 += 1
                #  else:
                #       losses_2 += 1
            else:
                 losses_2 += 1

        elif wininning_2 == 3:
            choice_2 = random.randint(2,3)

            if choice_2 == wininning_2:
                wins_2 += 1
            else:

                losses_2 += 1


print('\n\n')
print(wins_2)
print(losses_2)
print('\n\n')
