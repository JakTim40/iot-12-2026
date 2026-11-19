
class Car:
    def __init__(self, brand, age, max_speed, horse_power, parked_time):
        self.brand = brand
        self.age = age
        self.max_speed = max_speed
        self.horse_power = horse_power
        self.parked_time = parked_time

    def __del__(self):
        print("Машину", self.brand, "видалено з пам'яті")

    def show_info(self):
        print("Марка:", self.brand, "| Вік:", self.age, 
              "| Швидкість:", self.max_speed, "| Час на парковці:", self.parked_time, "год.")

class Parking:
    def __init__(self, max_places, price_per_hour):
        self.max_places = max_places
        self.price_per_hour = price_per_hour
        self.cars = [] 

    def __del__(self):
        print("Паркінг закрито")


    def park_car(self, car):
        if len(self.cars) >= self.max_places:
            print("Переповнення стоянки! Немає місця для", car.brand)
        else:
            self.cars.append(car) 
            print("Машину", car.brand, "успішно припарковано.")

  
    def leave_parking(self, car):
        if car in self.cars:
            self.cars.remove(car) 
            print("Машина", car.brand, "виїхала з парковки.")
        else:
            print("Такої машини немає на парковці.")

   
    def sort_cars(self):

        def get_time(c):
            return c.parked_time
            
        self.cars.sort(key=get_time, reverse=True)
        print("Машини відсортовано за часом стоянки.")

    # калькулятор вартоості
    def calculate_price(self):
        print("--- Розрахунок вартості ---")
        for car in self.cars:
            price = car.parked_time * self.price_per_hour
            print("До оплати за", car.brand, "-", price, "грн.")

    # очистка
    def show_all_cars(self):
        print("--- Всі машини на парковці ---")
        for car in self.cars:
            car.show_info()



my_parking = Parking(3, 20)
 
car1 = Car("BMW", 5, 250, 300, 2)
car2 = Car("Toyota", 2, 200, 150, 5)
car3 = Car("Ford", 10, 180, 110, 1)
car4 = Car("Audi", 1, 280, 400, 3)

print("\n--- Паркуємо машини ---")
my_parking.park_car(car1)
my_parking.park_car(car2)
my_parking.park_car(car3)

my_parking.park_car(car4)


print("\n--- Стан парковки ---")
my_parking.show_all_cars()


my_parking = Parking()

car1 = Car("Mazda", 5)
car2 = Car("MINI", 2)
car3 = Car("Shkoda", 10)

my_parking.park_car(car1) 
my_parking.park_car(car2)
my_parking.park_car(car3)

for car_ in my_parking.cars:
    print(f"Марка: {car_.brand}, вік авто: {car_.age}")


    

print("\n--- Сортування ---")
my_parking.sort_cars()
my_parking.show_all_cars()

print("\n--- Оплата ---")
my_parking.calculate_price()

print("\n--- Виїзд ---")
my_parking.leave_parking(car2)
my_parking.show_all_cars()

print("\n--- Кінець програми ---")