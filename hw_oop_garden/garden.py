from abc import abstractmethod
import random


class GardenMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Garden(metaclass=GardenMeta):
    def __init__(self, vegetables, fruits):
        self.vegetables = vegetables
        self.fruits = fruits

    def show_the_garden(self):
        print(f'I have such vegetables {self.vegetables}')
        print(f'I have such fruits {self.fruits}')


class Vegetables:
    def __init__(self, vegetable_type):
        self.vegetable_type = vegetable_type

    states = {"0": "None", "1": "Flowering", "2": "Green", "3": "Red"}

    @abstractmethod
    def growth(self):
        raise NotImplementedError('You missed me.')

    @abstractmethod
    def is_ripe(self):
        raise NotImplementedError("You missed me")


class Fruits:
    def __init__(self, fruits_type):
        self.fruits_type = fruits_type

    states = {0: "None", 1: "Flowering", 2: "Green", 3: "Red"}

    @abstractmethod
    def growth(self):
        raise NotImplementedError('You missed me.')

    @abstractmethod
    def is_ripe(self):
        raise NotImplementedError("You missed me")


class Tomato(Vegetables):

    def __init__(self, vegetable_type, number_of_tomatoes):
        Vegetables.__init__(self, vegetable_type)
        self.number_of_tomatoes = number_of_tomatoes
        self.states = 0
        self.vegetable_type = vegetable_type

    def growth(self):
        if self.states < 1:
            if random.randint(1, 10) == 5:  # 10% что цветок завял
                self.states = 0
            else:
                self.states = 1
        elif random.randint(1, 3) == 1:  # 30% что плод созреет позже
            self.states = 1
        elif self.states == 3:  # Защита что бы 3 не стала 2
            self.states = 3
        else:
            self.states = random.randint(2, 3)  # выбираем стадию созревания 2 или 3
        self.print_state()

    def print_state(self):
        print(f"{self.vegetable_type}, {self.number_of_tomatoes} , {self.states}")

    def is_ripe(self):
        return self.states == 3

    def eaten(self):
        self.states = 0


class Apple(Fruits):

    def __init__(self, fruits_type, number_of_apples):
        Fruits.__init__(self, fruits_type)
        self.number_of_apples = number_of_apples
        self.states = 0
        self.fruits_type = fruits_type

    def print_state(self):
        print(f"{self.fruits_type}, {self.number_of_apples} , {self.states}")

    def growth(self):
        if self.states < 1:
            if random.randint(1, 10) == 5:  # 10% что цветок завял
                self.states = 0
            else:
                self.states = 1
        elif random.randint(1, 3) == 1:  # 30% что плод созреет позже
            self.states = 1
        elif self.states == 3:  # Защита что бы 3 не стала 2
            self.states = 3
        else:
            self.states = random.randint(2, 3)  # выбираем стадию созревания 2 или 3
        self.print_state()

    def is_ripe(self):
        return self.states == 3

    def eaten(self):
        self.states = 0

class TomatoBush:
    def __init__(self, number_of_tomatoes):
        self.tomatoes = [Tomato('Cherry', index) for index in range(0, number_of_tomatoes - 1)]

    def growth_all(self):
        for tomato in self.tomatoes:
            tomato.growth()

    # def all_are_ripe(self):
    #   lst = []
    #   for tomato in self.tomatoes:
    #     ripe_state = tomato.is_ripe()
    #       lst.append(ripe_state)
    #   return all(lst)

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []

    def insects_attack(self):
        for tomato in self.tomatoes:
            if tomato.states == 2 or tomato.states == 3:
                tomato.eaten()

class AppleTree:
    def __init__(self, number_of_apples):
        self.apples = [Apple('White', index) for index in range(0, number_of_apples - 1)]

    def growth_all(self):
        for apple in self.apples:
            apple.growth()

    def all_are_ripe(self):
        return all([apple.is_ripe() for apple in self.apples])

    def give_away_all(self):
        self.apples = []

    def insects_attack(self):
        for apple in self.apples:
            if apple.states == 3 or apple.states == 2:
                apple.eaten()


class Gardener:
    def __init__(self, name, plants):
        self.name = name
        self.plants = plants

    def work(self):
        for plant in self.plants:
            plant.growth_all()

    def harvest(self):
        for plant in self.plants:
            if plant.all_are_ripe():
                plant.give_away_all()
            else:
                print('Too early to harvest')

    def kill_pests(self ,pest):
        self.pest = pest
        print(f'Damn ,{pest.type} eat my garden! There are {pest.quantity} of them!')
        pest.quantity = 0
        print(f'I killed em all! Now the are {pest.quantity} of them here!')



class Pests:

    def __init__(self, type, quantity):
        self.type = type
        self.quantity = quantity

    def eat(self, plants):
        self.plants = plants
        if self.quantity > 23:
            for plant in self.plants:
                plant.insects_attack()
                print("Yummy")
        else:
            print(f'Sorry , pests quantity is only {self.quantity}')
            self.quantity += 4


    def pests_quantity(self):
        print(self.quantity)


tomato_bush = TomatoBush(10)
apple_tree = AppleTree(10)
pests = Pests('worm', 21)
John = Gardener('John', [tomato_bush, apple_tree])

garden = Garden(tomato_bush, apple_tree)

pests.pests_quantity()

John.work()
pests.eat([tomato_bush, apple_tree])
pests.pests_quantity()
John.work()
pests.eat([tomato_bush, apple_tree])

for i in tomato_bush.tomatoes:
    i.print_state()

pests.eat([tomato_bush])

for i in tomato_bush.tomatoes:
    i.print_state()

pests.pests_quantity()

John.kill_pests(pests)

pests.pests_quantity()






