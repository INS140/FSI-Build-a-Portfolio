import Monster_SB

# Hello! If you're reading this then you probably clicked on the link to see my combat simulator!
# This is a D&D oriented simulator, so it uses a lot of the vocabulary from that format.
# You'll need to copy all three files to play the game.

# HOW TO PLAY:
# 1. Set number of players. You can set as many as you like, but I recommend no more than 5.
#    Setting the number to 1 will stop the game early.
# 2. Set player types (available types include: player, gnoll, skeleton, and zombie. More to be added soon!).
#    It is not recommended to set combatants to "player" unless you understand how D&D combat works.
#    My advice, stick with the zombies. Makes it way easier.
# 3. If you select "player" as the player type, you'll need to provide an HP and AC, see vocab reference for details.
#    The game presets these stats for "monster" types.
# 4. For both monsters and players, you'll need to set a name. Names will be used in a couple different ways.
# 5. When all your combatants are set up, the game will start.
# 6. The game is a free-for-all and will only end when there is one combatant left.
# 7. At the beginning of each turn you will be asked to type a command. Type "help" for a list of commands.
# 8. Once there is only one combatant left standing, the win message will appear with that combatant's name.
# 9. Enjoy!

# Vocab reference:
# HP = hit points !!!RECOMMENDED 30 OR BELOW!!!
# AC = Armor class, value in D&D that determines defense. !!!MUST BE A VALUE BETWEEN 1-20!!!
# Initiative = Value that determines combatant turn order

# This is still a work in progress, but I hope to eventually develop this into a functional app.

# To shorten variable size, p = player

# This section decides how many players there are and their attributes
p_list_creation = False
while p_list_creation is False:
    try:
        number_of_p = int(input('How many players? > '))
        p_list_creation = True
    except ValueError:
        print('Invalid input')

print(' ')
range_of_p = range(0, number_of_p)
p_list = []
for p_number in range_of_p:
    p_list += [f'{p_number}']
    monster_type = input('Player type > ').lower()
    p_creation_attempt = False
    while p_creation_attempt is False:
        if monster_type == 'player':
            p_list[p_number] = Monster_SB.Player()
            p_list[p_number].set_stats(input('Name > '), int(input('HP > ')), int(input('AC > ')))
            p_creation_attempt = True
        elif monster_type == 'gnoll':
            p_list[p_number] = Monster_SB.Gnoll()
            p_list[p_number].set_stats(input('Name > '))
            p_creation_attempt = True
        elif monster_type == 'skeleton':
            p_list[p_number] = Monster_SB.Skeleton()
            p_list[p_number].set_stats(input('Name > '))
            p_creation_attempt = True
        elif monster_type == 'zombie':
            p_list[p_number] = Monster_SB.Zombie()
            p_list[p_number].set_stats(input('Name > '))
            p_creation_attempt = True
        else:
            print('''
Invalid player type
Valid types: player, gnoll, skeleton, zombie
            ''')
            monster_type = input('Player type > ').lower()
    print(' ')

# This section is to determine initiative
for player in p_list:
    player.roll_initiative()
    p_list.sort(key=lambda p: p.initiative, reverse=True)

# This creates reference lists for in game use
p_list_reference_init = []
for player in p_list:
    p_list_reference_init += [player.initiative]
p_list_reference_name = []
for player in p_list:
    p_list_reference_name += [player.name]

# Intro
print('''

                                    Let the battle
                                        Begin!!!''')
print('-' * 100)
round_num = 0

# This is the actual game
while number_of_p > 1:
    round_num += 1
    for player in p_list:
        if player.hp <= 0 or player.run is True:
            try:
                p_list_reference_init.remove(player.initiative)
                p_list_reference_name.remove(player.name)
            except IndexError:
                pass
            except ValueError:
                pass
    print(f'''
Initiative: {p_list_reference_init}
Player Name: {p_list_reference_name}

Round {round_num}''')
    print('-' * 100)

    for player in p_list:
        if player.hp > 0 and player.run is False:
            player.reference()
            turn_finished = False
            player.temp_ac = 0
            print(' ')
            player.command()
            while turn_finished is False:
                if player.com == 'atk': # The Attack command
                    target = input('target > ')
                    attack_attempt = False
                    while attack_attempt is False:
                        for p_number in range_of_p:
                            try:
                                if target == p_list[p_number].name and p_list[p_number].run is False:
                                    player.attack(p_list[p_number])
                                    if p_list[p_number].hp <= 0:
                                        print(f'{p_list[p_number].name} is dead')

                                        number_of_p -= 1
                                    attack_attempt = True
                                    target = 0
                                else:
                                    pass
                            except IndexError:
                                pass
                        if target == 'help':
                            print('''Type a combatants name to target it
Names can be found in "Player Names" list at beginning of Round''')
                            target = input('target > ')
                        elif target == 0:
                            pass
                        else:
                            print('''Invalid target
Type "help" for options''')
                            target = input('target > ')
                    turn_finished = True
                    print('-' * 100)
                elif player.com == 'def': # The Defend Command
                    player.defend()
                    turn_finished = True
                    print('-' * 100)
                elif player.com == 'run': # The Run Command
                    print(f'{player.name} chickened out ...')
                    player.run = True
                    number_of_p -= 1
                    turn_finished = True
                    print('-' * 100)
                elif player.com == 'help': # The Help Command
                    print('''Options:
    atk - attack a target
    def - temporarily raise AC
    pass - pass turn
    run - forfeit
                    ''')
                    player.command()
                elif player.com == 'pass': #The Pass Command
                    turn_finished = True
                    print('-' * 100)
                else:
                    print('''Invalid input"
Type "help" for options
                    ''')
                    player.command()

        if number_of_p <= 1:
            break
        else:
            pass

# Decides winner after game ends
for player in p_list:
    if player.hp > 0 and player.run is False:
        print(f'***** {player.name} WINS *****')
        break
    else:
        pass
