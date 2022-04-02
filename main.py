import game
import sys

light_room = game.Place("Light room")
beach = game.Place("Beach")
street = game.Place("Street")
dark_house = game.Place("Dark house")
waterfall = game.Place("Waterfall")
lava_mountain = game.Place("Lava mountain")
the_darkest_room = game.Place("THE DARKEST ROOM")
crystal_kingdom = game.Place("Crystal kingdom")

light_room.link_room(beach, 'east')
beach.link_room(light_room, 'west')

light_room.link_room(street, 'north')
street.link_room(light_room, 'south')
street.link_room(dark_house, 'north')

dark_house.link_room(the_darkest_room, 'north')
dark_house.link_room(waterfall, 'west')
dark_house.link_room(crystal_kingdom, 'east')
dark_house.link_room(street, 'south')

waterfall.link_room(dark_house, 'east')
waterfall.link_room(lava_mountain, 'south')

lava_mountain.link_room(waterfall, 'north')

crystal_kingdom.link_room(dark_house, 'west')

the_darkest_room.link_room(dark_house, 'north')

text_1 = 'Hey dear friend! I found you yesterday lying on a beach around some \
shipwrecks and be aware walking out, bad guys are everywhere'
villager_1 = game.Villager('Anthony', text_1, 'Listen what they say')
light_room.set_villager(villager_1)

text_2 = 'Hey, look at this beautiful beach! It\'s so great here. Three elements will defeat him, \
find them, abc or die'
villager_2 = game.Villager('Alex', text_2, 'Beach is relaxing')
beach.set_villager(villager_2)

text_3 = 'There may be dangerous on the streets, be aware. The sword is not enough, it needs more accurate \
weapon, where you can see yourself in it'
villager_3 = game.Villager('Robert', text_3, 'Never give up!')
street.set_villager(villager_3)

hairdryer = game.Weapon("Hairdryer")
white_crystal = game.Weapon("White crystal")
a_drop_of_water = game.Weapon("A drop of water")
hot_stuff = game.Weapon("Hot stuff")
cake = game.Weapon("Cake")

street_monster = game.Enemy('Street monster', 'Do you have some money? Yes/no, I don\'t care', 'Little knife', hairdryer)
street.set_enemy(street_monster)

darkest_monster = game.Enemy('Darkest monster', 'Light? I don\'t know about light. You won\'t too', 'Great lantern', cake)
dark_house.set_enemy(darkest_monster)

crystal_monster = game.Enemy('Crystal monster', 'You don\'t know anything about being rich!', 'A penny', white_crystal)
crystal_kingdom.set_enemy(crystal_monster)

water_monster = game.Enemy('Water monster', 'Did you drink enough water? Cause now you will have too much of it!', 'Hairdryer', a_drop_of_water)
waterfall.set_enemy(water_monster)

lava_monster = game.Enemy('Lava monster', 'You are nothing compared to the sun!', 'Suncream', hot_stuff)
lava_mountain.set_enemy(lava_monster)

main_bossa = game.Boss('The BOSS', 'Who are you? A joke?', ['A drop of water', 'Hot stuff', 'White crystal'], 'GG')
the_darkest_room.set_enemy(main_bossa)
main_bossa.weekness = ['A drop of water', 'Hot stuff', 'White crystal']

little_knife = game.Weapon("Little knife")
bad_ass_pillow = game.Weapon("Bad ass pillow")
light_room.set_item(little_knife)
light_room.set_item(bad_ass_pillow)

sand = game.Weapon("Just sand")
a_stick = game.Weapon("Stick, not magic")

beach.set_item(sand)
beach.set_item(a_stick)

gun = game.Weapon("Gun")
suncream = game.Weapon("Suncream")
street.set_item(gun)
street.set_item(suncream)

dark_yalo = game.Weapon("Dark yalo")
a_piece_of_nothing = game.Weapon("Nothing")
dark_house.set_item(a_piece_of_nothing)
dark_house.set_item(dark_yalo)

gogo = game.Weapon("GOGO")
lantern = game.Weapon("Great lantern")
waterfall.set_item(lantern)
waterfall.set_item(gogo)

dollar = game.Weapon("Dollar")
penny = game.Weapon("A penny")
lava_mountain.set_item(penny)
lava_mountain.set_item(dollar)

current_room = light_room
backpack = []

def print_backpack():
    if len(backpack) == 0:
        print("Backpack is empty")
    else:
        i = 0
        for item in backpack:
            print(f"[{i + 1}] {item}")
            i += 1
            
print("Welcome to the travel game in the village of Unknown!")
print("----------------")
print("Your main goal is unknown, but it's to free the village!")
print("You will have one life")
print("While traveling through the places in the game you would find monsters, villlagers and items that would help you to win the game!")
print("You can exit the game at any time")
print("Press 'Enter' to continue")
input(">>> ")
print("------------")
print("There are all the comands that may be used in the game:")
print("- go")
print("- take")
print("- drop")
print("- fight")
print("- hear a wisdom")
print("- talk to villager")
print("- talk to enemy")
print("- exit")
print("- backpack")
print("-----------")
print("Good luck!", end = ' ')


while main_bossa.is_in_game:
    print("Press 'Enter' to continue")
    input(">>> ")
    print("----------")
    print(f"You are in the {current_room.name}")
    print()
    if len(current_room.items) != 0:
        print(f"There are items in this place! {len(current_room.items)} in total")
    try:
        print(f"There is a calm villager {current_room.villager.name}")
    except AttributeError:
        pass
    try:
        print(f"There is a scary enemy {current_room.enemy.name}")
    except AttributeError:
        pass
    print()
    for room in current_room.linked_rooms:
        print(f'{room[0].name} is {room[1]}')
    print("----------")
    print("Make a move:")
    while True:
        move = input(">>> ").strip()
        if move in ['hear a wisdom', 'talk to villager', 'talk to enemy', 'go', 'drop', 'take', 'fight', 'exit', 'backpack']:
            break
        print("Try again :(")

    if move == 'talk to villager':
        if current_room.villager != None:
            current_room.villager.talk()
        else:
            print("There isn't a villager here")
    elif move == 'talk to enemy':
        if current_room.enemy != None:
            current_room.enemy.talk()
        else:
            print("There isn't an enemy here")
    elif move == 'hear a wisdom':
        if current_room.villager != None:
            current_room.villager.say_wisdom()
        else:
            print("There isn't a villager here")
    elif move == 'go':
        print("Where do you want to go?")
        while True:
            goo = input(">>> ")
            if goo in ['north', 'south', 'west', 'east']:
                br = False
                for room in current_room.linked_rooms:
                    if goo == room[1]:
                        current_room = room[0]
                        br = True
                        print('You have moved!')
                        break
                if br:
                    break
            print("Please try again")
    elif move == 'drop':
        if len(backpack) == 0:
            print('You can\'t drop anything from an empty backpack')
        else:
            print("What do you want to drop?")
            print_backpack()
            while True:
                try:
                    index = int(input(">>> ")) - 1
                except:
                    print("The index should be integer")
                    continue
                if index >= 0 and index < len(backpack):
                    current_room.set_item(backpack[index])
                    backpack.pop(index)
                    print("The item was dropped")
                    break
                print("The index is incorrect")
    elif move == 'take':
        if len(current_room.items) == 0:
            print("There is nothing to take (")
            continue
        if len(backpack) != 5:
            i = 0
            print("What item do you want to pick up?")
            for item in current_room.items:
                print(f'[{i + 1}] {item}')
                i += 1
            print("Enter the index:")
            while True:
                try:
                    index = int(input(">>> ")) - 1
                except:
                    print("The index should be integer")
                    continue
                if index >= 0 and index < len(current_room.items):
                    backpack.append(current_room.items[index])
                    current_room.items.pop(index)
                    print("The item was picked up")
                    break
                print("The index is incorrect")
        else:
            print("The backpack is full, drop something before picking up")
    elif move == 'fight':
        if current_room.enemy == None:
            print("The is no enemy in the room :(")
        elif isinstance(current_room.enemy, game.Boss):
            print('Be ready to face the boss!')
            print("-----------")
            print("You need to fight with him in the right order, remember that!")
            print("Type in the weapons you will use:")
            counter = 0
            fight_mass = []
            while True:
                print("-----------")
                print("Here is your backpack:")
                print_backpack()
                print("-----------")
                if counter == 3:
                    break
                if len(backpack) == 0:
                    print("You don't have any more items in your backpack. ", end = '')
                    main_bossa.is_in_game = False
                    break
                try:
                    index = int(input(">>> ")) - 1
                except:
                    print("The index should be integer")
                    continue
                if index >= 0 and index < len(backpack):
                    fight_mass.append(backpack[index].name)
                    backpack.pop(index)
                    counter += 1
                    continue
                print("Please, enter the item you have in a backpack")
            print(fight_mass)
            print(main_bossa.weekness)
            if fight_mass == main_bossa.weekness:
                main_bossa.is_in_game = False
                main_bossa.is_defeated = True
            else:
                print("You chose the wong items or the order was wrong", end = ' ')
                main_bossa.is_in_game = False
        else:
            if len(backpack) == 0:
                print("The backpack is empty, you can't fight")
                continue
            print("------------")
            print("Here is your backpack. Choose the item to fight with:")
            print_backpack()
            print(f"Type in what do you choose to fight with {current_room.enemy.name}")
            while True:
                try:
                    index = int(input(">>> ")) - 1
                except:
                    print("The index should be integer")
                    continue
                if index >= 0 and index < len(backpack):
                    if backpack[index].name == current_room.enemy.weekness:
                        print(f"You successfully defeated the {current_room.enemy.name}!")
                        backpack.pop(index)
                        if current_room.enemy.drop != None:
                            backpack.append(current_room.enemy.drop)
                        current_room.enemy = None
                        break
                    else:
                        print("The item was incorrect. ", end ='')
                        main_bossa.is_in_game = False
                        break
                else:
                    print("This item isn't in your backpack")
    elif move == 'exit':
        print("Thanks for playing!")
        sys.exit()
    elif move == 'backpack':
        print("Here is your backpack:")
        print_backpack()
    else:
        print("Please, try again")

if main_bossa.is_defeated == True:
    print("CONGRATULATIONS! The game was won! GG!")
else:
    print("Sorry, you are dead :(")
