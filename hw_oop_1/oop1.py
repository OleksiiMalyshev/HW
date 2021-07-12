# 1. Create a Vehicle class with max_speed and mileage instance attributes

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


# 2. Create a child class Bus that will inherit all of the variables and methods
# of the Vehicle class and will have seating_capacity own method

class Bus(Vehicle):
    def __init__(self, capacity, max_speed, mileage):
        super().__init__(max_speed, mileage)
        self.capacity = capacity

    def seating_capacity(self):
        print(f"Capacity of the Bus  = {self.capacity}")


# 3. Determine which class a given Bus object belongs to (Check type of an object)

honda = Bus(10, 100, 1000)

# print("And the object 'honda' belongs to",type(honda))

# 4. Determine if School_bus is also an instance of the Vehicle class

School_bus = Bus(60, 95, 60000)


# print(isinstance(School_bus,Vehicle))

# 5. Create a new class School with get_school_id and number_of_students instance attributes

class School:
    def __init__(self, get_shool_id, number_of_students):
        self.get_shool_id = get_shool_id
        self.number_of_students = number_of_students


# 6*. Create a new class SchoolBus that will inherit all of the methods from School and Bus and will have its own - bus_school_color

class SchoolBus(School, Bus):
    def __init__(self, color, get_shool_id, number_of_students, capacity, max_speed, mileage):
        School.__init__(self, get_shool_id, number_of_students)
        Bus.__init__(self, capacity, max_speed, mileage)
        self.color = color

    def bus_school_color(self):
        print("I`m yellow")

    def blabla(self):
        print(self.max_speed, self.color)


scbs = SchoolBus('red', 15, 100, 55, 10, 10000)


# scbs.blabla()


# 7. Polymorphism: Create two classes: Bear, Wolf. Both of them should have
# make_sound method. Create two instances, one of Bear and one of Wolf,
# make a tuple of it and by using for call their action using the same method.

class Bear:
    def make_sound(self):
        print("Rawr")


class Wolf:
    def make_sound(self):
        print("Grrr")


bear = Bear()
wolf = Wolf()


# for beasts in (bear,wolf):
#     beasts.make_sound()

# 8. Create class City with name, population instance attributes, return a new instance only when population > 1500,
# otherwise return message: "Your city is too small".
class City:
    def __new__(cls, name, population):
        if population > 1500:
            return super().__new__(cls)
        else:
            return 'Your city is too small'

    def __init__(self, name, population):
        self.name = name
        self.population = population


city_1 = City('London', 10)
print(city_1)
city_2 = City('Paris', 1501)
print(city_2)
print(city_2.population)



# 9. Override a printable string representation of the City class and return: The population of the city {name} is {population}

class CityV2:

    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __str__(self):
        if self.population > 1500:
            return f"The population of the city {self.name} is {self.population}"
        else:
            return "Your city is too small"


central = CityV2("Central", 1499)
star = CityV2("Star", 1501)

print(central)
print(star)


# 10*. Override magic method __add__() to perform the additional action as 'multiply' (*)
# the value which is greater than 10. And perform this add (+) of two instances.

class Add:
    def __init__(self, first):
        self.first = first

    def __add__(self, other):
        if self.first > 10 or other.first > 10:
            return self.first * other.first
        else:
            return self.first + other.first


a = Add(10)
b = Add(10)
c = a + b


# print(c)

# 11. The __call__ method enables Python programmers to write classes where the instances behave like functions and can be called like a function.
# Create a new class with __call__ method and define this call to return sum.

class Call:
    def __call__(self, a, b):
        return a + b


c = Call()
# print(c(10, 20))


# 12*. Making Your Objects Truthy or Falsey Using __bool__().
# Create class MyOrder with cart and customer instance attributes.
# Override the __bool__magic method considered to be truthy if the length of the cart list is non-zero.
# e.g.:
# order_1 = MyOrder(['a', 'b', 'c'], 'd')
# order_2 = MyOrder([], 'a')
# bool(order_1)
# True
# bool(order_2)
# False

class MyOrder:
    def __init__(self, cart, customer):
        self.cart = cart
        self.customer = customer

    def __bool__(self):
        len_chk = len(self.cart)
        return len_chk > 0


order_1 = MyOrder(['a', 'b', 'c'], 'd')
order_2 = MyOrder([], 'a')
# print(bool(order_1))
# print(bool(order_2))
