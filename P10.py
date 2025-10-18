from abc import ABC, abstractmethod
class Animal(ABC):    
    def __init__(self, name):
        self.name = name      
        self._sound = None    
    @abstractmethod
    def make_sound(self):
        pass
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.__breed = breed   
    def make_sound(self):
        self._sound = "Bark"
        return f"{self.name} ({self.__breed}) says {self._sound}"
class Cat(Animal):
    def make_sound(self):
        self._sound = "Meow"
        return f"{self.name} says {self._sound}"
dog1 = Dog("Buddy", "Labrador")
cat1 = Cat("Kitty")

print(dog1.make_sound())
print(cat1.make_sound())
