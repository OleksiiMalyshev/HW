from collections import namedtuple

import dataclasses
from dataclasses import dataclass


# 1.
# class Laptop:
#     Make the class with composition.
# class Battery:
#     Make the class with composition.


class Laptop:
    def __init__(self):
        battery_1 = Battery(500)
        battery_2 = Battery(700)
        self.batteries = [battery_1, battery_2]


class Battery:
    def __init__(self, capacity):
        self.capacity = capacity


laptop = Laptop()


# print(laptop)
# print(laptop.batteries)

# 2.
# class Guitar:
# Make the class with aggregation
# class GuitarString:
#  Make the class with aggregation

class Guitar:
    def __init__(self, guitar_string):
        self.guitar_string = guitar_string


class GuitarString:
    def __init__(self):
        pass


guitar_string = GuitarString()
guitar = Guitar(guitar_string)


# print(guitar_string)
# print(guitar)


# 3.
# class Calc:
#     Make class with one method "add_nums" with 3 parameters, which returns sum of these parameters.
#     Note: this method should be static
class Calc:
    def __init__(self):
        pass

    @staticmethod
    def add_nums(s1, s2, s3):
        return s1 + s2 + s3


# print(Calc.add_nums(1, 2, 3))

# 4*.
# class Pasta:
#     """
#     Make class which takes 1 parameter on init - list of ingredients and defines instance attribute ingredients.
#     It should have 2 methods:
#     carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
#     which should create Pasta instances with predefined list of ingredients.
#     Example:
#         pasta_1 = Pasta(["tomato", "cucumber"])
#         pasta_1.ingredients will equal to ["tomato", "cucumber"]
#         pasta_2 = Pasta.bolognaise()
#         pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']
#     """

class Pasta:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pasta > ({self.ingredients})'

    @classmethod
    def carbonara(cls):
        return cls(['forcemeat', 'tomatoes'])

    @classmethod
    def bolognaise(cls):
        return cls(['bacon', 'parmesan', 'eggs'])


pasta_1 = Pasta(['tomato', 'cucumber'])


# print(pasta_1)
# pasta_2 = Pasta.carbonara()
# print(pasta_2)
# pasta_3 = Pasta.bolognaise()
# print(pasta_3)

# 5*.
# class Concert:
#     """
#     Make class, which has max_visitors_num attribute and its
#     instances will have visitors_count attribute.
#     In case of setting visitors_count - max_visitors_num
#     should be checked, if visitors_count value is bigger
#     than max_visitors_num - visitors_count should be assigned
#     with max_visitors_num.
#     Example:
#         Concert.max_visitor_num = 50
#         concert = Concert()
#         concert.visitors_count = 1000
#         print(concert.visitors_count)  # 50
#     """

class Concert:
    max_visitor_num = 0

    def __init__(self):
        self.num = 0

    @property
    def visitors_count(self):
        return self.num

    @visitors_count.setter
    def visitors_count(self, new):
        if new <= Concert.max_visitor_num:
            self.num = new
        else:
            self.num = Concert.max_visitor_num


Concert.max_visitor_num = 50
concert = Concert()
concert.visitors_count = 1000


# print(f'There are {concert.visitors_count} visitors in Concert hall')

# 6.
# class AddressBookDataClass:
#     Create dataclass with 7 fields - key (int), name (str),
#     phone_number (str), address (str), email (str), birthday (str), age (int)

@dataclasses.dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


address_book = AddressBookDataClass(1, "Alex", '+333333333', "Ukraine Kiyv",
                                    "blabla@bla.bla", "15.05.95", 25)
# print(address_book)


# 7. Create the same class (6) but using NamedTuple
AddressBookNamedTuple = namedtuple('AdressBook', ['key', 'name', 'phone_number', 'address',
                                                  "email", 'birthday', 'age'])
a = AddressBookNamedTuple(1, "Alex", '+333333333', "Ukraine Kiyv",
                          "blabla@bla.bla", "15.05.95", '25')


# print(a)

# 8.
# class AddressBook:
#     Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
#     Make its str() representation the same as for AddressBookDataClass defined above.

class AddressBook:

    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return f'Adress Book {self.key}, {self.name}, {self.phone_number},' \
               f'{self.address}, {self.email}, {self.birthday}, {self.age}'

    def __repr__(self):
        return f'Adress Book {self.key}, {self.name}, {self.phone_number},' \
               f'{self.address}, {self.email}, {self.birthday}, {self.age}'

book_info = AddressBook('1', 'Alex', '+333333333', 'Ukraine', "blabla@bla.bla", "15.05.95", "25")

# print(book_info)
# print(book_info.__str__())
# print(str(book_info))
# print(book_info.__repr__())

# 9.
# class Person:
#     Change the value of the age property of the person object
#     name = "John"
#     age = 36
#     country = "USA"

class Person:
    name = "John"
    age = 36
    country = "USA"

b = Person()
setattr(b,'age',50)
# print(getattr(b,'age'))

# 10.
# class Student:
#     Add an 'email' attribute of the object student and set its value
#     Assign the new attribute to 'student_email' variable and print it by using getattr
#     id = 0
#     name = ""

class Student:
    id = 0
    name = ''

    def __init__(self, id, my_name):
        self.id = id
        self.my_name = my_name

me = Student(10, 'Alex')
setattr(me, 'my_email', "blabla@bla.bla")
# print('I am ',getattr(me,'my_name'),'and my email is',getattr(me,'my_email'))


# 11*.
# class Celsius:
#     By using @property convert the celsius to fahrenheit
#     Hint: (temperature * 1.8) + 32)

#     def __init__(self, temperature=0):
#         self._temperature = temperature
#
# # create an object
# {obj} = ...
#
# print({obj}.temperature)
class Celsius:
    def __init__(self, temp):
        self.temp = temp

    @property
    def temperature(self):
        self.temp = ((self.temp * 1.8) + 32)
        return f'Now it is {self.temp} Fahrenheit'

    def __repr__(self):
        return f'Now it is {self.temp} Celsius'

today = Celsius(35)
print(today)
print(today.temperature)