# class Car:

#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color
#         self.speed = 0
#         self.fuel = 100
#         self.engine_on = False

#     def start(self):
#         self.engine_on = True
#         print("Engine Started")

#     def accelerate(self):
#         if self.engine_on:
#             self.speed += 20
#             print("Speed:", self.speed)
#         else:
#             print("Start the engine first")

#     def brake(self):
#         self.speed -= 10
#         print("Speed:", self.speed)

#     def stop(self):
#         self.engine_on = False
#         self.speed = 0
#         print("Car Stopped")


# bmw = Car("BMW", "Black")

# print(bmw.brand)
# print(bmw.color)

# bmw.brake()

class Mobile:
    pass

    def __init__(self,brand,price):
        self.brand = brand
        self.price = price

    def display(self):
        print(f"{self.brand},{self.price}")

    
Nokia = Mobile("Nokia",20)
Nokia.display()





