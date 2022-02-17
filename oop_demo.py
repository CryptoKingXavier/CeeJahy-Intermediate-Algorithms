import random
class SmartDevice:
    def __init__(self, name, brand, price, screen_size, memory_space, battery_power, ram_size):
        value = [name, brand, price, screen_size, memory_space, battery_power, ram_size]
        key = ["name", "brand", "price", "screen_size", "memory_space", "battery_power", "ram_size"]
        for k, v in zip(key, value):
            print(f"{k} -> {v} ")


class Phone(SmartDevice):
    def typeOf(self, phoneType):
        self.phoneType = phoneType
        return self.phoneType

myPhone = Phone("iPhone", "iOS", f"${float(random.randint(100000, 150000))}", f"{int(random.randint(15, 21))} inches", "64GB", f"{int(random.randint(5000, 6500))}mAh", "4GB")
print(myPhone.typeOf(phoneType="SmartPhone"))