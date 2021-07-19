import random
from abc import abstractmethod
import time


class Animal:

    def __init__(self, power: int, speed: int):
        self.id = None
        self.max_power = power
        self.current_power = power
        self.speed = speed

    @abstractmethod
    def eat(self, victim, forest, own_name):
        pass


class Predator(Animal):
    def __init__(self, power: int, speed: int):
        super().__init__(power, speed)
        self.speed = speed
        self.power = power

    def eat(self, victim, forest, own_name):  # На ввод должны зайти - жертва, лес и ключ словаря(ИД) зверя
        self.own_name = own_name  # ID
        print(f'\nI`m Predator {self.own_name}, my current power = {self.current_power} and speed = {self.speed}')
        if self.current_power < 5:  # Проверка силы, если меньше 5 - умер с голоду
            print(f'I`m dying from starvation \n')
            forest.remove_animal(own_name)
        if forest.animals[victim] == self:  # Если рандом выбрал этого же хищника
            self.current_power -= round(self.current_power * 0.3)
            forest.animals[own_name].current_power = self.current_power
            print(f'No dinner today. Now my power is {self.current_power}\n')
            if self.power < 5:  # Проверка силы, если меньше 5 - умер с голоду
                print(f'I`m dying from starvation \n')
                forest.remove_animal(own_name)
        else:  #
            print(f'My victim is {victim} with current power = {forest.animals[victim].current_power} and'
                  f' speed = {forest.animals[victim].speed}')
            if self.speed > forest.animals[victim].speed:  # Проверка скорости хищника и жертвы
                if self.current_power > forest.animals[victim].current_power:  # если догнал - проверка силы
                    print(f'I ate {victim}')  # он покушал :)
                    forest.remove_animal(victim)
                    self.current_power += round(self.current_power * 0.5)
                    if self.current_power > self.max_power:  # этот if обновляет значения в словаре
                        self.current_power = self.max_power
                        forest.animals[own_name].current_power = self.current_power
                    print(f"Yummy! I had a great meal ! Now my current power is {self.current_power}\n")
                else:
                    if isinstance(forest.animals[victim], Herbivorous):
                        self.current_power -= round(self.power * 0.3)
                        forest.animals[own_name].current_power = self.current_power
                        forest.animals[victim].current_power -= round(forest.animals[victim].current_power * 0.3)
                        if self.power < 5:
                            print(f'I`m dying from starvation \n')
                            forest.remove_animal(own_name)
                        print(f'Bad luck today, my current power is {self.current_power} but his'
                              f' {forest.animals[victim].current_power} \n')
                    else:
                        print("Oh no! That was wrong choice! He eating me!\n")
                        forest.remove_animal(own_name)

            else:
                self.current_power -= round(self.power * 0.3)
                forest.animals[own_name].current_power = self.current_power
                if self.power < 5:
                    print(f'I`m dying from starvation \n')
                    forest.remove_animal(own_name)
                print(f"I had not enough speed! My speed - {self.speed} but his was {forest.animals[victim].speed}")
                print(f'But i still want to eat! Now my power is {self.current_power}\n')


class Herbivorous(Animal):
    def __init__(self, power: int, speed: int):
        super().__init__(power, speed)
        self.speed = speed
        self.power = power

    def eat(self, victim, forest, own_name):
        print(f'\nI`m Herbivore {own_name} and my current power is {self.current_power}')
        if self.power < 5:
            print(f'I`m dying from starvation \n')
            forest.remove_animal(own_name)
        self.current_power += self.current_power // 2
        forest.animals[own_name].current_power = self.current_power
        if self.current_power > self.max_power:
            self.current_power = self.max_power
            forest.animals[own_name].current_power = self.current_power
        print(f"Good grass! Now my current power is {self.current_power}\n")


class Forest:

    def __init__(self):
        self.animals = dict()

    def add_animal(self, animal: object, animal_id):
        self.animals[animal_id] = animal

    def remove_animal(self, animal_id):
        del self.animals[animal_id]

    def is_there_any_predators(self):  # Если эта функция вернет тру то игра закончена
        lst = []
        for animal in self.animals.keys():
            if isinstance(self.animals[animal], Herbivorous):
                lst.append(0)
            else:
                lst.append(1)
        b = 0
        for i in lst:
            if i == 1:
                b += 1
        if b > 0:
            return True

    def random_pick(self):  # Рандомно выбирает животное из словаря
        return random.choice(list(self.animals.keys()))

    def last_predator(self):  # Если эта функция вернет тру то игра закончена
        if len(self.animals.keys()) == 1:
            for animal in self.animals.keys():
                if isinstance(self.animals[animal], Predator):
                    return True

    def print_forest(self):
        print('=======================================================')
        for each in forest1.animals:
            print(f"|Animal id = {each}, speed = {self.animals[each].speed}, power = {self.animals[each].power} "
                  f"type = {'Predator|' if not isinstance(self.animals[each], Herbivorous) else 'Herbivore|'}")
        print('=======================================================')

    def hunt_auto(self):
        lst_of_forest_keys = list(self.animals.keys())
        for animal_num in lst_of_forest_keys:
            try:
                self.animals[animal_num].eat(self.random_pick(), self, animal_num)
                time.sleep(1)
            except KeyError:
                continue

    def hunt_manual(self):
        global type_of_exec
        lst_of_forest_keys = list(self.animals.keys())
        for animal_num in lst_of_forest_keys:
            try:
                self.animals[animal_num].eat(self.random_pick(), self, animal_num)
                time.sleep(1)
                type_of_exec = int(input('Write [1] if you want to automatically proceed till the end of program \n'
                                         "Write [2] if you want to stop after every animal's move\n"
                                         "Write [3] if you want to execute program without pauses - "))
                return
            except KeyError:
                continue

    def hunt_auto_fast(self):
        lst_of_forest_keys = list(self.animals.keys())
        for animal_num in lst_of_forest_keys:
            try:
                self.animals[animal_num].eat(self.random_pick(), self, animal_num)
            except KeyError:
                continue


# Генератор животных
nature = (random.choice([Predator, Herbivorous])(random.randint(25, 100), random.randint(25, 100)) for i in
          range(1, 100))

forest1 = Forest()

for k in range(int(input("How many Animals in your forest? "))):
    animal_1 = next(nature)
    forest1.add_animal(animal_1, k)

forest1.print_forest()
type_of_exec = int(input('Write [1] if you want to automatically proceed till the end of program \n'
                         "Write [2] if you want to stop after every animal's move\n"
                         "Write [3] if you want to execute program without pauses - "))
while True:
    if not forest1.is_there_any_predators():
        print("There are no predators left")
        break
    if forest1.last_predator():
        print('Only one predator left.')
        break
    if type_of_exec == 1:
        forest1.hunt_auto()
    elif type_of_exec == 2:
        forest1.hunt_manual()
    elif type_of_exec == 3:
        forest1.hunt_auto_fast()
forest1.print_forest()
