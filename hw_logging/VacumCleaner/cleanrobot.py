import time
from random import randint


class RobotException(Exception):
    pass


class VacuumMore70(RobotException):
    pass


class VacuumFull(RobotException):
    pass


class Battery0(RobotException):
    pass


class BatteryLess20(RobotException):
    pass


class WaterLess20(RobotException):
    pass


class Water0(RobotException):
    pass


class Robot:
    def __init__(self, water_tank, trash_can, battery):
        self.water_tank = water_tank
        self.trash_can = trash_can
        self.battery = battery

    def wash(self):
        try:
            self.water_tank -= randint(0, 10)
            time.sleep(1)
            if self.water_tank <= 0:
                raise Water0
            if self.water_tank < 20:
                raise WaterLess20
            return f"Washing"
        except Water0:
            return f"Water tank is empty"
        except WaterLess20:
            return f"Water tank's capacity is less then 20%"

    def vacuum_clean(self):
        try:
            self.trash_can += randint(0, 10)
            time.sleep(1)
            if self.trash_can >= 100:
                raise VacuumFull
            if 100 > self.trash_can > 70:
                raise VacuumMore70
            return f"Cleaning"
        except VacuumFull:
            return f"Trash can is full"
        except VacuumMore70:
            return f"Trash can is almost full, please clean the trash can"

    def move(self):
        while True:
            print("\nMove")
            print(self.wash())
            print(self.vacuum_clean())
            try:
                self.battery -= 5
                if self.battery <= 0:
                    raise Battery0
                if self.battery <= 20:
                    raise BatteryLess20
            except Battery0:
                print(f"Battery is empty")
                break
            except BatteryLess20:
                print(f"Battery's capacity less then 20 ")
            time.sleep(1)


robot = Robot(randint(0, 100), randint(0, 100), randint(0, 100))
print(f'Water tank = {robot.water_tank}, Trash can = {robot.trash_can} , Robot battery = {robot.battery}')
robot.move()
