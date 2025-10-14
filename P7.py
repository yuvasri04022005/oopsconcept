class Bird:
    def fly(self):
        print("Bird is flying")

class Airplane:
    def fly(self):
        print("Airplane is flying")

for obj in (Bird(), Airplane()):
    obj.fly()