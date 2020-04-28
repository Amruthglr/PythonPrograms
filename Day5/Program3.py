class Vehicle():
    wheel = 4
    color = 'Red'

    def start(self):
        print("Start the vehicle")

    def stop(self):
        print("Stop the vehicle")


maruti = Vehicle()
print(maruti.color)
print(maruti.start())
print(maruti.wheel)
print(maruti.stop())


class Person:
    willDie = True
    age = 20
    color = 'White'

    def walk(self, speed):
        print("Walks {}".format(speed))

    def talk(self, action):
        print("Talks {}".format(action))

    def agesetter(self, age):
        self.age = age


amit = Person()
print(amit.age)
amit.age = 30
print("new age of Amit")
print(amit.age)
amit.color = "Wheatish"
print(amit.color)
amit.agesetter(45)
print("New Age of Amit")
print(amit.age)