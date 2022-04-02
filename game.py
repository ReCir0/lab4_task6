'''Lab 4.6'''

class Entity():
    '''
    Class Entity
    '''
    def __init__(self, name, main_text):
        self.name = name
        self.main_text = main_text

    def talk(self):
        print(self.main_text)

class Villager(Entity):
    '''
    Class Villager
    '''
    def __init__(self, name, main_text, some_wisdom):
        Entity.__init__(self, name, main_text)
        self.some_wisdom = some_wisdom

    def say_wisdom(self):
        print(self.some_wisdom)

class Enemy(Entity):
    '''
    Class Enemy
    '''
    def __init__(self, name, main_text, weekness, drop):
        Entity.__init__(self, name, main_text)
        self.weekness = weekness
        self.drop = drop

class Boss(Enemy):
    '''
    Class Boss
    '''
    def __init__(self, name, main_text, weekness, drop):
        Enemy.__init__(self, name, main_text, weekness, drop)
        self.weekness = []
        self.is_defeated = False
        self.is_in_game = True

class Place():
    '''
    Class Place
    '''
    def __init__(self, name):
        self.name = name
        self.linked_rooms = []
        self.villager = None
        self.enemy = None
        self.items = []

    def link_room(self, room, direction):
        '''
        Links a room
        '''
        self.linked_rooms.append((room, direction))

    def set_villager(self, character):
        self.villager = character

    def set_enemy(self, character):
        self.enemy = character

    def set_item(self, item):
        self.items.append(item)

class Weapon():
    '''
    Class Item
    '''
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
