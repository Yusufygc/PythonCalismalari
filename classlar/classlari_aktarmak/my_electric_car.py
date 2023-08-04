from car import ElectricCar

my_togg = ElectricCar("togg","tx10",2022)

print(my_togg.isim_ata())
my_togg.battery.describe_battery(100)
my_togg.battery.get_range()